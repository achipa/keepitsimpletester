#!/usr/bin/python

import sys
import os
import subprocess
import time
import cookielib, urllib2, urllib
import parser
import logging
import webbrowser


# This is ugly and not how you should be using PyQt in general , but don't let that scare you. I do it like this for a reason

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    app = QApplication(sys.argv)
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.exists("main.ui") and os.path.getmtime("main.ui") > os.path.getmtime("main_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
    if os.path.exists("kisstester.qrc") and os.path.getmtime("kisstester.qrc") > os.path.getmtime("kisstester_rc.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except Exception, e:
    subprocess.call(["pyuic4", "main.ui", "-o", "main_ui.py"])
    subprocess.call(["pyrcc4", "kisstester.qrc", "-o", "kisstester_rc.py"])
from main_ui import Ui_MainWindow
    
# end ugly

import settings
import vote 
import appitem

class MainWindow(QMainWindow):
    loginAvailable = pyqtSignal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except: pass
 
        self.settings = settings.Settings()
        self.loggedin = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

        self.packages = {}
        self.loadProgress = QProgressDialog()
        self.loadProgress.setVisible(False)
        self.loadProgress.setWindowModality(Qt.WindowModal)
        self.ui.queueScroll.setVisible(False)
        
        self.connect(self.ui.actionSettings, SIGNAL("triggered()"), self.settings, 
                    SLOT("show()"))
        
        self.connect(self.ui.actionAbout, SIGNAL("triggered()"), 
                    lambda: QMessageBox.about(self, "KISStester", "An application to simplify the QA feedback for applications in the extras-testing repository of maemo.org. <BR><BR>Border colour indicates your vote, text color indicates unlock status.<BR><BR>Developed with PyQt and WingIDE. Happy testing !"))
        
        self.connect(self.ui.actionAbout_Qt, SIGNAL("triggered()"), 
                    lambda: QApplication.instance().aboutQt())
        
        self.connect(self.ui.actionReload_repository_data, SIGNAL("triggered()"),
                    self.loadPackages)
        
        self.connect(self.ui.actionCommentList, SIGNAL("triggered()"),
                    lambda: webbrowser.open("https://garage.maemo.org/mailman/listinfo/testingsquad-comments"))

        self.connect(self.ui.actionTesterList, SIGNAL("triggered()"),
                    lambda: webbrowser.open("https://garage.maemo.org/mailman/listinfo/testingsquad-list"))
                                             
        self.connect(self.ui.actionFilter_packages, SIGNAL("triggered()"),
                    self.pickFilter)
        
        self.loginAvailable.connect(self.loadPackages)
                         
        self.showRecent(True)
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
        maemodata = { "username" : str(self.settings.data.value("username").toString()).lower(), "password" : str(self.settings.data.value("password").toString()), "midcom_services_auth_frontend_form_submit" : "Login" }
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
        
        if len(p.packages) > 0:
            pkglist = ""
            for (name, d) in p.packages.iteritems():
                item = appitem.AppItem(self, d)
                self.connect(item.ui.pButton_vote, SIGNAL("clicked()"), self.vote)
                self.ui.queueLayout.insertWidget(0,item)
                pkglist += " " + name
                
            rawrecent = subprocess.Popen(["/usr/bin/dpkg-query -W %s" % str(pkglist)], shell=True, bufsize=8192, stdout=subprocess.PIPE).stdout.read()
            for line in rawrecent.splitlines():
                pkgdata = line.split("\t")
                print pkgdata
                if len(pkgdata) < 2:
                    continue
                for (pname, d) in p.packages.iteritems():         
                    print d["pname"]
                    print d["version"]
                    if d["pname"] == pkgdata[0] and d["version"] == pkgdata[1]:
                        item = appitem.AppItem(self, d)
                        item.ui.pButton_install.setVisible(False) # no install button if already installed
                        self.connect(item.ui.pButton_vote, SIGNAL("clicked()"), self.vote)
                        self.ui.recentLayout.insertWidget(0,item)                                  
                    
#                    for filename in os.listdir("/var/lib/dpkg/info"):
#                        if not filename.endswith(".list"):
#                            continue
                
            self.loadProgress.setValue(page)
            QApplication.processEvents()
            self.loadPackages(page + 1)
        else:
            self.loadProgress.reset()
            self.sortArea()
            if self.ui.recentContents.isVisible and self.ui.recentLayout.count() < 2:
                QMessageBox.warning(self, "No packages", "Currently you do not have packages installed from extras-testing that need feedback. Switching to full QA queue view.")
                self.showRecent(False)
            
#       except:
                    
    def sortArea(self):
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
            QApplication.processEvents()
        except: pass
        tmplist = []
        while self.ui.queueLayout.count() > 1:
            tmplist.append(self.ui.queueLayout.takeAt(0).widget())
        s = sorted(tmplist, key=lambda x: x.waiting, reverse=True) # reverse as QA is a LIFO (should be, anyway)
        for elem in s:
            self.ui.queueLayout.insertWidget(0, elem)
            
        tmplist = []
        while self.ui.recentLayout.count() > 1:
            tmplist.append(self.ui.recentLayout.takeAt(0).widget())
        s = sorted(tmplist, key=lambda x: x.waiting) # not reverse as the already installed section is LIFO
        for elem in s:
            self.ui.recentLayout.insertWidget(0, elem)
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
        except: pass
        
    def vote(self):
        votedialog = vote.Vote(self)
        p = self.sender().parent()
        votedialog.setWindowTitle(p.name + " " + p.version)
        votedialog.pname = p.pname
        votedialog.version = p.version
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
            QApplication.processEvents()
        except: pass
        votedialog.id = p.getId()
        try:
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
        except: pass
        votedialog.show()
    
    @pyqtSlot(bool)
    def showRecent(self, b):
        self.ui.recentScroll.setVisible(b)
        self.ui.queueScroll.setVisible(not b)
        if not self.loggedin:
            self.login()
        elif b and self.ui.recentLayout.count() < 2:
            QMessageBox.warning(self, "No packages", "Currently you do not have packages installed from extras-testing that need feedback. If you want to install such software, please change the package filter in the menu to show the complete QA queue")
        
    @pyqtSlot()
    def pickFilter(self):
        item = QStringList()
        item.append("Already installed")
        item.append("QA queue")
        ret = QInputDialog.getItem(self, "Shown packages", "", item, 0, False)
        if item.indexOf(ret[0]) != 0:
            self.showRecent(False)
        else:
            self.showRecent(True)
        
def start():
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())
