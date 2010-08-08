#!/usr/bin/python

import sys
import os
import subprocess
import time
import cookielib, urllib2, urllib
import parser
import logging

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    app = QApplication(sys.argv)
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.getmtime("main.ui") > os.path.getmtime("main_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except Exception, e:
    subprocess.call(["pyuic4", "main.ui", "-o", "main_ui.py"])
from main_ui import Ui_MainWindow
    
import settings
import vote 

class MainWindow(QMainWindow):
    loginAvailable = pyqtSignal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.settings = settings.Settings()
        self.loggedin = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

        self.packages = {}
        self.loadProgress = QProgressDialog()
        self.loadProgress.setVisible(False)
        self.loadProgress.setWindowModality(Qt.WindowModal)
        self.ui.queueScroll.setVisible(False)
        self.ui.recentScroll.setVisible(False)
        
        self.connect(self.ui.actionSettings, SIGNAL("triggered()"), self.settings, 
                     SLOT("show()"))
        
        self.connect(self.ui.actionAbout, SIGNAL("triggered()"), 
                     lambda: QMessageBox.about(self, "KISStester", "An application to simplify the QA feedback for applications in the extras-testing repository of maemo.org"))
        
        self.connect(self.ui.actionAbout_Qt, SIGNAL("triggered()"), 
                     lambda: QApplication.instance().aboutQt())
        
        self.connect(self.ui.actionReload_repository_data, SIGNAL("triggered()"),
                     self.loadPackages)
        
        self.connect(self.ui.recentButton, SIGNAL("toggled(bool)"),
                     self.showRecent)
        
        self.connect(self.ui.queueButton, SIGNAL("toggled(bool)"),
                     self.showQueue)
        
        self.loginAvailable.connect(self.loadPackages)
                         
    #            http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&ordermode=new&search=hermes
    #    mainw.connect(umw.actionAutorotate, SIGNAL("triggered(bool)"), lambda x: settings.setValue("autorotate", 0))
    
    def login(self):
        logging.warning("Logging in")
#        garagedata = { "return_to" : "", "form_loginname" : "achipa" , "form_pw" : "123456", "login" : "Login+with+SSL" }
#        r = opener.open("https://garage.maemo.org/account/login.php", urllib.urlencode(garagedata))

        self.loadProgress.setWindowTitle("Logging in to maemo.org")
        self.loadProgress.setRange(0,0)
        self.loadProgress.setValue(0)
        self.loadProgress.show()
        QApplication.processEvents()
        maemodata = { "username" : str(self.settings.data.value("username").toString()), "password" : str(self.settings.data.value("password").toString()), "midcom_services_auth_frontend_form_submit" : "Login" }
        print maemodata
        try:
            r = self.opener.open("https://maemo.org", urllib.urlencode(maemodata))
            if r.read().find("http://static.maemo.org/style_maemo2009/img/logged.png") > 0:
                self.loggedin = True
                self.loadProgress.reset()
                self.loginAvailable.emit()
        except Exception, e:
            print e
         
#        "https://maemo.org/username=achipa&password=123456&midcom_services_auth_frontend_form_submit=Login"

        while not self.loggedin:
            if not self.settings.show():
                self.loadProgress.hide()
                return
            self.login()
    
    @pyqtSlot()
    @pyqtSlot(int)
    def loadPackages(self,page=1):
        if page == 1:
            self.loadProgress.setWindowTitle("Loading extras-testing data")
            self.loadProgress.setRange(0,0)
            self.loadProgress.show()
            QApplication.processEvents()
            while self.ui.queueLayout.count() > 1:
                self.ui.queueLayout.takeAt(0).widget().deleteLater()
            while self.ui.recentLayout.count() > 1:
                self.ui.recentLayout.takeAt(0).widget().deleteLater()
 #      try:
        r = self.opener.open("http://maemo.org/packages/repository/qa/fremantle_extras-testing/?org_openpsa_qbpager_packages_in_repo_page=%s" % page)
        content = r.read()
        p = parser.MyHTMLParser()
        p.feed(content)
        p.close()
        if page == 1:
            self.loadProgress.setRange(0, p.pages)
        self.loadProgress.setValue(page)
        QApplication.processEvents()
        print p.pages
        print len(p.packages)
        
        def configureButton(b, d):
                    b.setText("%s, Karma %s%s, %s" % (d["version"], d["karma"], d["status"], d["waiting"]))
                    if d["voted"]:
                        b.setEnabled(False)
                        if d["myvote"]:
                            b.setStyleSheet("QPushButton{ background-color: green }")
                        else:
                            b.setStyleSheet("QPushButton{ background-color: red }")
                    elif d["status"]:
                        b.setStyleSheet("QPushButton{ color: green }")
                    elif d["karma"] < 0:
                        b.setStyleSheet("QPushButton{ color: red }")
                        
                    b.setProperty("karma", d["karma"])
                    b.setProperty("name", d["name"])
                    b.setProperty("status", d["status"])
                    b.setProperty("version", d["version"])
                    b.setProperty("waiting", d["waiting"])
                    self.connect(b, SIGNAL("clicked()"), self.vote)
            
            
        if len(p.packages) > 0:
            pkglist = ""
            for (name, d) in p.packages.iteritems():
                b = QPushButton()
                label = QLabel(d["name"])
                configureButton(b,d)
                self.ui.queueLayout.insertWidget(0,b)
                self.ui.queueLayout.insertWidget(0,label)
                pkglist += " " + name
                
            package = ""
            rawrecent = subprocess.Popen(["/usr/bin/dpkg -s %s" % str(pkglist)], shell=True, bufsize=8192, stdout=subprocess.PIPE).stdout.read()
            for line in rawrecent.splitlines():
                if line.startswith("Package:"):
                    package = line.split(": ")[1]
                if line.startswith("Status:") and line.endswith(" installed"):
                    b = QPushButton()
                    d = p.packages[package]
                    label = QLabel(d["name"])
                    configureButton(b,d)
                    self.ui.recentLayout.insertWidget(0,b)
                    self.ui.recentLayout.insertWidget(0,label)
                    
#                    for filename in os.listdir("/var/lib/dpkg/info"):
#                        if not filename.endswith(".list"):
#                            continue
                
            self.loadPackages(page + 1)
        else:
            self.loadProgress.reset()
            self.sortArea("waiting")
            
#       except:
                    
    def sortArea(self, prop):
        tmplist = []
        while self.ui.queueLayout.count() > 1:
            self.ui.queueLayout.takeAt(0).widget().deleteLater()
            tmplist.append(self.ui.queueLayout.takeAt(0).widget())
        s = sorted(tmplist, key=lambda x: x.property(prop).toByteArray(), reverse=True)
        for elem in s:
            label = QLabel(elem.property("name").toString())
            self.ui.queueLayout.insertWidget(0, elem)
            self.ui.queueLayout.insertWidget(0, label)
        
    def vote(self):
        votedialog = vote.Vote(self)
        votedialog.setWindowTitle(self.sender().property("name").toString() + " " + self.sender().property("version").toString())
        votedialog.show()
    
    @pyqtSlot(bool)
    def showRecent(self, b):
        print b
        self.ui.recentScroll.setVisible(b)
        self.ui.queueScroll.setVisible(not b)
        if not self.loggedin:
            self.login()
        
    @pyqtSlot(bool)
    def showQueue(self, b):
        self.showRecent(not b)
        
def start():
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())
