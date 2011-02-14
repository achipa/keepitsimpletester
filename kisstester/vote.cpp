#include "vote.h"
#include "ui_vote.h"
#include <QtGui/QMessageBox>
#include <QtWebKit/QWebPage>
#include <QtWebKit/QWebElement>
#include <QtWebKit/QWebFrame>
#include <QDebug>
#include <QByteArray>

VoteDialog::VoteDialog(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::VoteDialog),
    silentcomment(false)
{
    ui->setupUi(this);
    ui->commentView->setVisible(false);
#ifdef Q_WS_MAEMO5
    setAttribute(Qt::WA_Maemo5StackedWindow);
#endif
}

VoteDialog::~VoteDialog()
{
    delete ui;
}

bool VoteDialog::unlockCheck()
{
    bool state = ui->cBox_brk->isChecked() & ui->cBox_cpu->isChecked() & ui->cBox_dub->isChecked() &ui->cBox_lic->isChecked() &ui->cBox_opt->isChecked() &ui->cBox_pwr->isChecked();
    ui->passButton->setEnabled(state);
    return state;
}

void VoteDialog::passVote()
{
    if (unlockCheck()) {
        comment();
        thumb(true);
    } else {
        QMessageBox::information(this, "Pass criteria missing","You need to check (or have a good indication) of all the criteria above (i.e. all the checkboxes need to be checked)");
    }
}

void VoteDialog::failVote()
{
    if (!unlockCheck()) {
//        if (QMessageBox::Ok == QMessageBox.question(self, "Are you sure ?", "Remember, the reasons for failing an app should be based on severe issues. It's more of a 'does itwork' rather than a 'how well does it work'. If in doubt, please consult the QA a documentation."):
        comment();
        thumb(false);
    } else {
        QMessageBox::information(this, "Fail criteria missing","You need to supply a reason for failing this package. Remember, it's not about whether you like the application, how pretty or cool it is - it is about whether it negatively impacts your usage of your device and if it is well-behaved (isn't illegal, is possible to report errors, etc). The slickness/coolness of the app will be judged by awarding it with 1-5 stars in Extras, not here.");
    }
}
void VoteDialog::id()
{
    nam->disconnect();
    QByteArray getData = QString("http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&search=%0").arg(pname).toUtf8();
    qDebug() << getData;
    connect(nam, SIGNAL(finished(QNetworkReply*)), SLOT(idDone(QNetworkReply*)));
    nam->get(QNetworkRequest(QUrl(getData)));
#ifdef Q_WS_MAEMO5
    setAttribute(Qt::WA_Maemo5ShowProgressIndicator, true);
#endif
}

void VoteDialog::idDone(QNetworkReply* rep)
{
    nam->disconnect(this);
    QScopedPointer<QWebPage> page(new QWebPage());
    page->mainFrame()->setContent(rep->readAll()); //rep->readAll());
    foreach (QWebElement element, page->mainFrame()->findAllElements("CONTENT")) {
        QWebElement nameElement = element.findAll("name").first();
        QWebElement idElement = element.findAll("id").first();
        qDebug() << "id" << idElement.toPlainText();
        qDebug() << "name" << nameElement.toPlainText();
        if (!nameElement.isNull() && nameElement.toPlainText() == pname) {
            pid = idElement.toPlainText();
            qDebug() << "id match" << idElement.toPlainText();
            ui->commentButton->setEnabled(true);
            ui->passButton->setEnabled(true);
            ui->failButton->setEnabled(true);
        }

    }
#ifdef Q_WS_MAEMO5
    setAttribute(Qt::WA_Maemo5ShowProgressIndicator, false);
#endif
//    for (QWebElement el, element.
//        qapages = element.attribute("href").right(1).toUInt(); // yeah, should be lastIndexOf, not hardcoded
//        qDebug () << "estimated pages: " << qapages << element.toPlainText();
//        progress->setRange(1,qapages);
//        progress->setWindowTitle(tr("Downloading repository data"));
//        for (int i=2; i<=qapages; i++)
//            nam->get(QNetworkRequest(QUrl(QString(QAPAGEURL).arg(i))));
//    }
//    progress->setValue(++loadedpages);

//    // Teh Parser. Here be dragons and nasty code. Will prolly be deprecated for libattica

//    foreach (QWebElement element, page->mainFrame()->findAllElements("DIV[class=repository_list_item]")) {
//        if (element.findFirst("DIV[class=karma]").isNull()) continue;
//}
//    nam->post(QNetworkRequest(QUrl('https://maemo.org/packages/api/v1/comments/add/')), postData);
//    connect    xmlstr = urllib2.urlopen("http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&search=%s" % self.pname).read()
//        domm = parseString(xmlstr)
//        for es in domm.getElementsByTagName("content"):
//            tmpid = ""
//            tmpname = ""
//            for child in es.childNodes:
//                try:
//                    if child.tagName == "id":
//                        tmpid = child.childNodes[0].data
//                    if child.tagName == "name":
//                        tmpname = child.childNodes[0].data
//                except: pass

//            if tmpid and tmpname == self.pname:
//                self.id = tmpid

//        return self.id
}
void VoteDialog::comment()
{
    if (ui->textEdit->toPlainText().length() == 0)
            return;
#ifdef Q_WS_MAEMO5
    setAttribute(Qt::WA_Maemo5ShowProgressIndicator, true);
#endif
    QByteArray postData = QString("content=%0&message=%1&type=1").arg(pid).arg(ui->textEdit->toPlainText() + "\n\n--\n\nKT").toUtf8();
    qDebug() << postData;
    connect(nam, SIGNAL(finished(QNetworkReply*)), SLOT(commentDone(QNetworkReply*)));
    nam->post(QNetworkRequest(QUrl("https://maemo.org/packages/api/v1/comments/add/")), postData);
}

void VoteDialog::commentDone(QNetworkReply* rep)
{
    nam->disconnect(this);
    if (rep->error() == QNetworkReply::NoError && !silentcomment) {
        QMessageBox::information(this, "Commented","Comment on package left. It might take a few minutes until it appears on the maemo.org site.");
#ifdef Q_WS_MAEMO5
        setAttribute(Qt::WA_Maemo5ShowProgressIndicator, false);
#endif
        ui->textEdit->setText("");
    } else {
        QMessageBox::critical(this, "Network error","Uh-oh, network error encountered.");
    }
    silentcomment = false;
}

void VoteDialog::thumb(bool vote)
{
    if (!vote && ui->textEdit->toPlainText().length() < 3) {
        QMessageBox::warning(this, "No fail reason given","Please provide the reason for failing this packet in the comment field. Remember, this a test for TECHNICAL blockers (see the list of checkboxes above), not how pretty or cool the application is.");
        return;
    }
    QByteArray postData = QString("content=%0&message=%1&type=1").arg(pid).arg(vote ? "1" : "0").toUtf8();
    qDebug() << postData;
    connect(nam, SIGNAL(finished(QNetworkReply*)), SLOT(commentDone(QNetworkReply*)));
    nam->post(QNetworkRequest(QUrl("https://maemo.org/packages/api/v1/favs/add/")), postData);
    if (vote) {
        QMessageBox::information(this, "Package Passed :)","Package thumbed up. It might take a few minutes until your vote appears in the listing.");
    } else {
        QMessageBox::information(this, "Package Failed :(","Package thumbed down. It might take a few minutes until your vote appears in the listing.");
    }
}

void VoteDialog::thumbDone(QNetworkReply* rep)
{
    nam->disconnect(this);
    if (rep->error() == QNetworkReply::NoError) {
        silentcomment = true;
        comment();
    } else {
        QMessageBox::critical(this, "Network error","Uh-oh, network error encountered.");
    }
}

void VoteDialog::loadComments()
{
    ui->commentView->setVisible(true);
    ui->commentView->setHtml("Please wait, loading comments.");
    QByteArray getData = QString("http://maemo.org/packages/package_instance/view/fremantle_extras-testing_free_armel/%0/%1/").arg(pname).arg(pversion).toUtf8();
    qDebug() << getData;
    connect(nam, SIGNAL(finished(QNetworkReply*)), SLOT(loadCommentsDone(QNetworkReply*)));
    nam->get(QNetworkRequest(QUrl(getData)));
}

void VoteDialog::loadCommentsDone(QNetworkReply* rep)
{
    nam->disconnect(this);
    if (rep->error() == QNetworkReply::NoError) {
        QString content = "";
        QScopedPointer<QWebPage> page(new QWebPage());
        page->mainFrame()->setContent(rep->readAll()); //rep->readAll());
        foreach (QWebElement element, page->mainFrame()->findAllElements("DIV[class=net_nehmer_comments_comment]")) {
            content += element.toOuterXml();
        }
        qDebug() << content;
        ui->commentView->setHtml(content);
    } else {
        QMessageBox::critical(this, "Network error","Uh-oh, network error encountered.");
        ui->commentView->setVisible(false);
    }
}
/*@pyqtSlot()
def comment(self):
    if len(self.textEdit.toPlainText()) == 0 :
        return
    try:
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
        QApplication.processEvents()
    except: pass
    commentdata = { "content" : self.id, "message" : self.textEdit.toPlainText() + "\n\n--\n\nKT", "type" : 1 }
    print commentdata
    self.textEdit.setText("")
    passw_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passw_mgr.add_password( None,
                      'https://maemo.org/packages/api/v1/comments/add/',
                      str(self.settings.data.value("username").toString()).lower(),
                      str(self.settings.data.value("password").toString()))
    auth_handler = urllib2.HTTPBasicAuthHandler(passw_mgr)
    self.opener = urllib2.build_opener(auth_handler)

    r = self.opener.open("https://maemo.org/packages/api/v1/comments/add/", urllib.urlencode(commentdata))
    ret = r.read()
    try:
        self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
        QApplication.processEvents()
    except: pass

def thumb(self, b):
    if b:
        message = 1
    else:
        message = 0
    votedata = { "content" : self.id, "message" : message, "type" : 1 }
    print votedata
    passw_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passw_mgr.add_password( None,
                      'https://maemo.org/packages/api/v1/favs/add/',
                      str(self.settings.data.value("username").toString()).lower(),
                      str(self.settings.data.value("password").toString()))
    auth_handler = urllib2.HTTPBasicAuthHandler(passw_mgr)
    self.opener = urllib2.build_opener(auth_handler)

    try:
        if os.path.exists("/home/user/.kisstester_rw"):
            try:
                self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
                QApplication.processEvents()
            except: pass
            r = self.opener.open("https://maemo.org/packages/api/v1/favs/add/", urllib.urlencode(votedata))
            ret = r.read()
            # voting is slow, maybe we need a progress bar here, too...
            if b:
                QMessageBox.information(self, "Package Passed :)","Package thumbed up. It might take a few minutes until your vote appears in the listing.")
            else:
                QMessageBox.information(self, "Package Failed :(","Package thumbed down. It might take a few minutes until your vote appears in the listing.")
            try:
                self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
          QApplication.processEvents()
      except: pass
      self.close()
  else:
      QMessageBox.warning(self, "WARNING", "KISStester operating in read-only mode. Please check the testing-squad mailing-list before you do something you don't want to
:)")
except Exception, e:
  QMessageBox.warning(self, "Vote failed", str(e))
*/
