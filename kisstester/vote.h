#ifndef VOTE_H
#define VOTE_H

#include <QtGui/QMainWindow>
#include <QtGui/QDesktopServices>
#include <QtCore/QUrl>
#include <QtCore/QPointer>
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>

namespace Ui {
    class VoteDialog;
}

class VoteDialog : public QMainWindow
{
    Q_OBJECT

public:
    explicit VoteDialog(QWidget *parent = 0);
    ~VoteDialog();
    void setName(QString name) { pname = name; setWindowTitle(pname);}
    void setVersion(QString version) { pversion = version; }
    void setNAM(QNetworkAccessManager* mwnam) { nam = mwnam; }
    void id();

private slots:
    void idDone(QNetworkReply *rep);

public slots:
    void on_cBox_cpu_clicked() { unlockCheck(); }
    void on_cBox_brk_clicked() { unlockCheck(); }
    void on_cBox_dub_clicked() { unlockCheck(); }
    void on_cBox_lic_clicked() { unlockCheck(); }
    void on_cBox_opt_clicked() { unlockCheck(); }
    void on_cBox_pwr_clicked() { unlockCheck(); }
    void on_pButton_detail_clicked() { QDesktopServices::openUrl(QUrl("http://wiki.maemo.org/Extras-testing/QA_Checklist")); }
    void on_pButton_page_clicked() { QDesktopServices::openUrl(QString("http://maemo.org/packages/package_instance/view/fremantle_extras-testing_free_armel/%0/%1/").arg(pname).arg(pversion)); }
    void on_passButton_clicked() { passVote(); }
    void on_failButton_clicked() { failVote(); }
    void on_commentButton_clicked() { comment(); }
    void on_showCommentsButton_clicked() { loadComments(); }

    void thumbDone(QNetworkReply *rep);
    void commentDone(QNetworkReply *rep);
    void loadCommentsDone(QNetworkReply *rep);
private:
    void passVote();
    void failVote();
    void loadComments();
    void thumb(bool vote);
    void comment();

    bool unlockCheck();
    QString pname;
    QString pversion;
    QString pid;
    QPointer<QNetworkAccessManager> nam;
    Ui::VoteDialog *ui;
    bool silentcomment;
};

#endif // VOTE_H
