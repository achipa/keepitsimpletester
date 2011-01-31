#ifndef EXTRASPACKAGE_H
#define EXTRASPACKAGE_H

#include <QString>
#include <QDateTime>

class ExtrasPackage: public QObject
{
    Q_OBJECT
//  yeah, this property stuff is *way* too verbose in Qt
    Q_PROPERTY(QString name READ name WRITE setName NOTIFY nameChanged)
    Q_PROPERTY(QString pname READ pname WRITE setPName NOTIFY pnameChanged)
    Q_PROPERTY(QString version READ version WRITE setVersion NOTIFY versionChanged)
    Q_PROPERTY(QString link READ link WRITE setLink NOTIFY linkChanged)
    Q_PROPERTY(QString imageurl READ imageurl WRITE setImageURL NOTIFY imageurlChanged)
    Q_PROPERTY(QString bugtracker READ bugtracker WRITE setBugTracker NOTIFY bugtrackerChanged)
    Q_PROPERTY(int karma READ karma WRITE setKarma NOTIFY karmaChanged)
    Q_PROPERTY(int vote READ vote WRITE setVote NOTIFY voteChanged)
    Q_PROPERTY(bool status READ status WRITE setStatus NOTIFY statusChanged)
    Q_PROPERTY(bool installed READ installed WRITE setInstalled NOTIFY installedChanged)
    Q_PROPERTY(QDateTime waiting READ waiting WRITE setWaiting NOTIFY waitingChanged)
    Q_PROPERTY(int age READ age WRITE setAge NOTIFY ageChanged)
signals:
    void nameChanged(QString name);
    void pnameChanged(QString pname);
    void versionChanged(QString version);
    void linkChanged(QString link);
    void imageurlChanged(QString imageurl);
    void bugtrackerChanged(QString bugtracker);
    void karmaChanged(int karma);
    void voteChanged(int vote);
    void statusChanged(bool status);
    void installedChanged(bool installed);
    void waitingChanged(QDateTime waiting);
    void ageChanged(int vote);
public:
    ExtrasPackage(QObject* parent = 0);
    QString name() const { return m_name; }
    void setName(QString name) { m_name = name; }

    QString pname() const { return m_pname; }
    void setPName(QString pname) { m_pname = pname; }

    QString version() const { return m_version; }
    void setVersion(QString version) { m_version = version; }

    QString link() const { return m_link; }
    void setLink(QString link) { m_link = link; }

    QString imageurl() const { return m_imageurl; }
    void setImageURL(QString imageurl) { m_imageurl = imageurl; }

    QString bugtracker() const { return m_bugtracker; }
    void setBugTracker(QString bugtracker) { m_bugtracker = bugtracker; }

    int karma() const { return m_karma; }
    void setKarma(int karma) { m_karma = karma; }

    int vote() const { return m_vote; }
    void setVote(int vote) { m_vote = vote; }

    bool status() const { return m_status; }
    void setStatus(bool status) { m_status = status; }

    bool installed() const { return m_installed; }
    void setInstalled(bool installed) { m_installed = installed; }

    QDateTime waiting() const { return m_waiting; }
    void setWaiting(QDateTime waiting) { m_waiting = waiting; }

    int age() const { return m_waiting.daysTo(QDateTime::currentDateTimeUtc()); }
    void setAge(int age) { m_waiting = QDateTime::currentDateTimeUtc().addDays(-age); }

    QString toString();
private:
    QString m_name;
    QString m_pname;
    QString m_version;
    int m_karma;
    int m_vote;
    bool m_status;
    bool m_installed;
    QString m_link;
    QString m_imageurl;
    QDateTime m_waiting;
    QString m_bugtracker;
};

#endif // EXTRASPACKAGE_H
