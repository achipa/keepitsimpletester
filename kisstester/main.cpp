#include <QtGui/QApplication>
#include <QtNetwork/QNetworkProxy>
#include <QtCore/QProcessEnvironment>
#include "mainwindow.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    // for people living in proxy hell
    QNetworkProxy proxy;
    // This should happening automatically but it doesn't. It's easier to code than to debug. Feel free to fix.
    QString proxystring = QProcessEnvironment::systemEnvironment ().value("http_proxy");
    if (!proxystring.isEmpty()){
        proxy.setType(QNetworkProxy::HttpProxy);
        proxystring.replace("http://","");
        proxy.setHostName(proxystring.split(":")[0]);
        proxy.setPort(proxystring.split(":").at(1).split("/")[0].toInt());
        QNetworkProxy::setApplicationProxy(proxy);
    }
    MainWindow mw;
    mw.show();

    return app.exec();
}
