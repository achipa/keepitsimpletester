#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QInputDialog>
#include <QtNetwork/QNetworkCookieJar>
#include <QtNetwork/QNetworkReply>
#include <QDebug>
#include <QWebPage>
#include <QWebFrame>
#include <QWebElement>
#include <QDeclarativeContext>
#include <QtCore/QProcess>

#define QAPAGEURL "http://maemo.org/packages/repository/qa/fremantle_extras-testing/?org_openpsa_qbpager_packages_in_repo_page=%0"
#define LOGINURL "http://maemo.org"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    progress(new QProgressDialog()),
    settings(new QSettings("kisstester", "main")),
    nam(new QNetworkAccessManager(this)),
    qapages(0),
    loadedpages(0)
{
    ui->setupUi(this);
    viewer = new QmlApplicationViewer();
//    QGraphicsView* qgv=new QGraphicsView(ui->qml);
    viewer = new QmlApplicationViewer(ui->qml);
//    viewer->setOrientation(QmlApplicationViewer::ScreenOrientationLockLandscape);
    viewer->setMainQmlFile(QLatin1String("qml/kisstester/main.qml"));
    viewer->showExpanded();
    viewer->setResizeMode(QDeclarativeView::SizeRootObjectToView);
    QWebSettings::globalSettings()->setAttribute(QWebSettings::JavascriptEnabled, false);
    startLogin();
}


MainWindow::~MainWindow()
{
    foreach (QObject* p, packages)
        delete p;
    delete ui;
}

void MainWindow::startLogin()
{
    progress->setWindowTitle(tr("Logging in to maemo.org"));
    progress->setRange(0,0);
    progress->setValue(0);
    bool ok;
    if (settings->value("username","").toString().isEmpty()) {
        QString uname;
        while (uname.isEmpty()) {
            uname = QInputDialog::getText(this,"Login parameters", "maemo.org username", QLineEdit::Normal, settings->value("username","").toString(), &ok);
            if (!ok) return;
        }
        settings->setValue("username", uname);
    }

    if (settings->value("password","").toString().isEmpty()) {
        QString pword;
        while (pword.isEmpty()) {
            pword = QInputDialog::getText(this,"Login parameters", "maemo.org password", QLineEdit::Password, settings->value("password","").toString(), &ok);
            if (!ok) return;
        }
        settings->setValue("password", pword);
    }
    progress->show();
    settings->sync();
    QByteArray postData = QString("username=%0&password=%1&midcom_services_auth_frontend_form_submit=Login").arg(settings->value("username").toString().toLower()).arg(settings->value("password").toString()).toUtf8();
    qDebug() << postData;
    connect(nam, SIGNAL(finished(QNetworkReply*)), this, SLOT(finishLogin(QNetworkReply*)));
    nam->setCookieJar(new QNetworkCookieJar()); // NAM takes ownership of the cookie jar
    nam->post(QNetworkRequest(QUrl(LOGINURL)), postData);
}

void MainWindow::finishLogin(QNetworkReply* rep)
{
    qDebug () << rep->error() << rep->size();
    progress->hide();
    QByteArray data(rep->readAll());

    if (data.contains("http://static.maemo.org/style_maemo2009/img/logged.png")) { // check if login successful. I know - I take patches
        qDebug() << "Login OK" ;
        nam->disconnect();
        connect(nam, SIGNAL(finished(QNetworkReply*)), this, SLOT(pageLoaded(QNetworkReply*)));
        nam->get(QNetworkRequest(QUrl(QString(QAPAGEURL).arg(1))));
        progress->show();
        progress->setWindowTitle(tr("Checking testing repository for packages"));
        return;
    }
    else qDebug () << data;
    settings->setValue("username", "");
    settings->setValue("password", "");
    settings->sync();
    startLogin();
}

void MainWindow::pageLoaded(QNetworkReply* rep)
{
  /*
    Yeah, this breaks if there are 10+ pages. In that case, this should be the least of your extras-testing worries

    <div class="repository_list_item">
    <div class="package_icon">
        <img src="http://static.maemo.org/static/8/8b8aa518afaa11dfbecb9fc2a192d92dd92d_cmd-shortcuts_icon" />
    </div>
        <div class="title"><a title="QA test page for cmd-shortcuts" href="/packages/package_instance/view/fremantle_extras-testing_free_armel/cmd-shortcuts/0.0.4-3/">Cmd Shortcuts</a></div>

        <div class="version"><a title="QA test page for 0.0.4-3 of cmd-shortcuts" href="/packages/package_instance/view/fremantle_extras-testing_free_armel/cmd-shortcuts/0.0.4-3/">0.0.4-3</a></div>
        <div class="karma">Karma: <span style="color:#00aa00">8</span> </div>

        <div class="waiting_since">2010-09-05 14:45 UTC</div>
    </div>
*/
    if (rep->error() != 0) {
        qDebug() << rep->errorString();
        return;
    }

    QWebPage* page = new QWebPage();
    page->mainFrame()->setContent(rep->readAll()); //rep->readAll());
    if (rep->url().toString().endsWith("1")) { // first page tells us the total number of pages, and allows launching load of remaining ones
        QWebElement element = page->mainFrame()->findAllElements("A[class=last_page]").first();
        qapages = element.attribute("href").right(1).toUInt(); // yeah, should be lastIndexOf, not hardcoded
        qDebug () << "estimated pages: " << qapages << element.toPlainText();
        progress->setRange(1,qapages);
        progress->setWindowTitle(tr("Downloading repository data"));
        for (int i=2; i<=qapages; i++)
            nam->get(QNetworkRequest(QUrl(QString(QAPAGEURL).arg(i))));
    }
    progress->setValue(++loadedpages);

    // Teh Parser. Here be dragons and nasty code. Will prolly be deprecated for libattica

    foreach (QWebElement element, page->mainFrame()->findAllElements("DIV[class=repository_list_item]")) {
        if (element.findFirst("DIV[class=karma]").isNull()) continue;
        ExtrasPackage* package = new ExtrasPackage();
        QWebElement tmpelement;
        QStringList qsl;

        if (!(tmpelement = element.findFirst("DIV[class=karma]")).isNull()) {
            qsl = tmpelement.toPlainText().split(": ");
            if (!qsl.isEmpty()) package->setKarma(qsl[1].toInt());
            if (!tmpelement.findFirst("SPAN").isNull()) package->setStatus(true);
        }

        package->setWaiting(QDateTime::fromString(element.findFirst("DIV[class=waiting_since]").toPlainText().replace(" UTC",""), "yyyy-MM-dd HH:mm"));

        if (!element.findFirst("DIV[class=fav_btn]").isNull())  { package->setVote(1); }
        if (!element.findFirst("DIV[class=bury_btn]").isNull())  { package->setVote(-1); }

        if (!(tmpelement = element.findFirst("A[href]")).isNull()) {
            qsl = tmpelement.attribute("href").split("/");
            if (!qsl.empty()) { package->setPName(qsl[5]); package->setVersion(qsl[6]); package->setLink(tmpelement.toPlainText()); }
            package->setName(tmpelement.toPlainText());
        }
//        qDebug() << package->toString() << packages.count();
        packages << package;

    }
    delete page;
    qDebug() << packages.count() << "packages loading...";
    if (loadedpages == qapages) {
        QDeclarativeContext* ctx = viewer->rootContext();
    //    ctx->setContextProperty("packageListModel", &packages);
        ctx->setContextProperty("packageListModel", QVariant::fromValue(packages));
        qDebug() << ctx->contextProperty("packageListModel").type();
        qDebug() << ctx->contextProperty("packageListModel").typeName();

        // check for installed packages

        QScopedPointer<QProcess> dpkgquery(new QProcess(this));
        QStringList args("-W");
        foreach (QObject* pkg, packages){
            args << pkg->property("pname").toString();
        }
        dpkgquery->start("/usr/bin/dpkg-query", args );
        dpkgquery->waitForFinished();                   // yeah, blocking, shame on me
        QString dpkgout = dpkgquery->readAllStandardOutput();
        qDebug () << dpkgout;
        foreach (QString line, dpkgout.split("\n")){    // read lines
            QStringList pkgdata = line.split("\t");
            if (pkgdata.length() >= 2 && !pkgdata.at(1).isEmpty()) { // ugly way of saying it's an installed package
                qDebug() << pkgdata;
                foreach (QObject* pkg, packages) {      // set installed flag on it
                    if (pkg->property("pname").toString() == pkgdata.at(0)) {
                        pkg->setProperty("installed", true);
                        qDebug() << pkg->property("pname").toString() << " is installed";
                        continue;
                    }
                }
            }
        }
    }
}
