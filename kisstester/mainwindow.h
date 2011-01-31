#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QtGui/QMainWindow>
#include "qmlapplicationviewer.h"

#include <QMessageBox>
#include <QDesktopServices>
#include <QProgressDialog>
#include <QSettings>
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkRequest>

#include <extraspackage.h>

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void on_actionAboutQt_triggered(bool checked) { QMessageBox::aboutQt(this, tr("About Qt")); }
    void on_actionAbout_triggered(bool checked) { QMessageBox::about(this, tr("About"), tr("An application to simplify the QA feedback for applications in the extras-testing repository of maemo.org. <BR><BR>Border colour indicates your vote, text color indicates unlock status.<BR><BR>Happy testing !" )); }
    void on_actionCommentList_triggered(bool checked) { QDesktopServices::openUrl(QUrl("https://garage.maemo.org/mailman/listinfo/testingsquad-comments")); }
    void on_actionTesterList_triggered(bool checked) { QDesktopServices::openUrl(QUrl("https://garage.maemo.org/mailman/listinfo/testingsquad-list")); }
    void on_actionSettings_triggered(bool checked) { QMessageBox::aboutQt(this, tr("About Qt")); }
    void on_actionFilter_packages_triggered(bool checked) { QMessageBox::aboutQt(this, tr("About Qt")); }
    void on_actionShow_only_unchecked_triggered(bool checked) { QMessageBox::aboutQt(this, tr("About Qt")); }
    void on_progress_canceled() { }
    void finishLogin(QNetworkReply* rep);
    void pageLoaded(QNetworkReply *rep);

private:
    Ui::MainWindow *ui;
    QmlApplicationViewer* viewer;
    QProgressDialog* progress;
    void startLogin();
    QSettings* settings;
    QNetworkAccessManager* nam;
    int qapages;
    int loadedpages;
    QList<QObject*> packages;
};

#endif // MAINWINDOW_H
