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
    
# end ugly, you can open your eyes now

import settings
import vote 
import appitem2
from asyncloader import aLoader

class MainWindow(QMainWindow, Ui_MainWindow):
    loginAvailable = pyqtSignal()
    loginRequested = pyqtSignal()
    loadNextPage = pyqtSignal(int)
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except: pass
 
        self.settings = settings.Settings()
        self.votedialog = vote.Vote(self)
        self.loggedin = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

        self.packages = {}
        self.loadProgress = QProgressDialog(self)
        self.loadProgress.setVisible(False)
        self.loadProgress.setWindowModality(Qt.NonModal)

        self.queueScroll.setVisible(False)
        
        self.connect(self.actionSettings, SIGNAL("triggered()"), self.settings, 
                    SLOT("show()"))
        
        self.connect(self.actionAbout, SIGNAL("triggered()"), 
                    lambda: QMessageBox.about(self, "KISStester", "An application to simplify the QA feedback for applications in the extras-testing repository of maemo.org. <BR><BR>Border colour indicates your vote, text color indicates unlock status.<BR><BR>Developed with PyQt and WingIDE. Happy testing !"))
        
        self.connect(self.actionAbout_Qt, SIGNAL("triggered()"), 
                    lambda: QApplication.instance().aboutQt())
        
        self.connect(self.actionReload_repository_data, SIGNAL("triggered()"),
                    self.loadPackages)
        
        self.connect(self.actionCommentList, SIGNAL("triggered()"),
                    lambda: webbrowser.open("https://garage.maemo.org/mailman/listinfo/testingsquad-comments"))

        self.connect(self.actionTesterList, SIGNAL("triggered()"),
                    lambda: webbrowser.open("https://garage.maemo.org/mailman/listinfo/testingsquad-list"))
                                             
        self.connect(self.actionFilter_packages, SIGNAL("triggered()"),
                    self.pickFilter)
        
        self.connect(self.actionShow_only_unchecked, SIGNAL("triggered(bool)"),
                    self.hideTested)
        
        self.loginAvailable.connect(self.loadPackages)
        self.loginRequested.connect(self.login)
        self.loadNextPage.connect(self.loadPackages)
                         
        self.showRecent(True)

    #            http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&ordermode=new&search=hermes
    #    mainw.connect(umw.actionAutorotate, SIGNAL("triggered(bool)"), lambda x: settings.setValue("autorotate", 0))

    @pyqtSlot()
    def login(self):
        logging.warning("Logging in")

        self.loadProgress.setWindowTitle("Logging in to maemo.org")
        self.loadProgress.setRange(0,0)
        self.loadProgress.setValue(0)
        self.loadProgress.show()
        QApplication.processEvents()
        maemodata = { "username" : str(self.settings.data.value("username").toString()).lower(), "password" : str(self.settings.data.value("password").toString()), "midcom_services_auth_frontend_form_submit" : "Login" }
        print maemodata
        if len(maemodata['username']) == 0:
            self.settings.show()
            self.loginRequested.emit()
            return

        def finishLogin(a):
            if a.content.find("http://static.maemo.org/style_maemo2009/img/logged.png") > 0:
                self.loggedin = True
                self.loadProgress.reset()
                self.loginAvailable.emit()
            else:
                if self.settings.show():
                    self.loginRequested.emit()

            a.deleteLater()
            self.loadProgress.hide()

        try:
            self.a = aLoader(self.opener, "https://maemo.org/", urllib.urlencode(maemodata))
            self.connect(self.a, SIGNAL("finished()"), lambda: finishLogin(self.a))
            self.a.start()
        except Exception, e:
            print e
         
    @pyqtSlot()
    @pyqtSlot(int)
    def loadPackages(self, page=1):
        if page == 1:
            self.loadProgress.setWindowTitle("Loading extras-testing data")
            self.loadProgress.setRange(0,0)
            self.loadProgress.show()
            QApplication.processEvents()
            while self.queueLayout.count() > 1:
                self.queueLayout.takeAt(0).widget().deleteLater()
            while self.recentLayout.count() > 1:
                self.recentLayout.takeAt(0).widget().deleteLater()
      
        self.a = aLoader(self.opener, "http://maemo.org/packages/repository/qa/fremantle_extras-testing/?org_openpsa_qbpager_packages_in_repo_page=%s" % page)
        self.a.start()
        self.connect(self.a, SIGNAL("finished()"), self.processPageData )
        self.page = page

    @pyqtSlot()
    def processPageData(self):
 #      try:
        p = parser.MyHTMLParser()
        p.feed(self.sender().content) # gotta quit using this self.sender() thing...
        self.sender().deleteLater()
        p.close()
        if self.page == 1: # we will know the range we need to load after getting the first page
            self.loadProgress.setRange(0, 2*p.pages) # we count 1 step for loading and one step for processing the data
          
        print p.pages
        print len(p.packages)
        
        if len(p.packages) > 0:
            self.loadProgress.setValue(2*self.page-1) # 1 means we loaded it, it will be 2 when we finish processing
            QApplication.processEvents()

            pkglist = ""
            for (name, d) in p.packages.iteritems():
                item = appitem2.AppItem(self, d)
                self.connect(item.pButton_vote, SIGNAL("clicked()"), self.vote)
                self.connect(item.pButton_details, SIGNAL("clicked()"), item.debDetails)
                self.queueLayout.insertWidget(0,item)
                pkglist += " " + name
                
            rawrecent = subprocess.Popen(["/usr/bin/dpkg-query -W %s" % str(pkglist)], shell=True, bufsize=8192, stdout=subprocess.PIPE).stdout.read()
            for line in rawrecent.splitlines():
                pkgdata = line.split("\t")
                print pkgdata
                if len(pkgdata) < 2:
                    continue
                for (pname, d) in p.packages.iteritems():         
                    if d["pname"] == pkgdata[0] and d["version"] == pkgdata[1]:
                        item = appitem2.AppItem(self, d)
                        self.connect(item.pButton_vote, SIGNAL("clicked()"), self.vote)
                        self.connect(item.pButton_details, SIGNAL("clicked()"), item.bugReport)
                        item.pButton_details.setText("Report bug")
                        self.recentLayout.insertWidget(0,item)                                  
                    
#                    for filename in os.listdir("/var/lib/dpkg/info"):
#                        if not filename.endswith(".list"):
#                            continue
                
            self.loadProgress.setValue(2*self.page)
            self.loadNextPage.emit(self.page + 1)
        else:
            self.loadProgress.reset()
            self.sortArea()
            if self.recentContents.isVisible and self.recentLayout.count() < 2:
                QMessageBox.warning(self, "No packages", "Currently you do not have packages installed from extras-testing that need feedback. Switching to full QA queue view.")
                self.showRecent(False)
            
#       except:
                    
    def sortArea(self):
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
            QApplication.processEvents()
        except: pass
        tmplist = []
        while self.queueLayout.count() > 1: # move appitems from the layout to a list so we could sort them
            tmplist.append(self.queueLayout.takeAt(0).widget())
        s = sorted(tmplist, key=lambda x: x.waiting, reverse=True) # reverse as QA is a LIFO (should be, anyway)
        for elem in s:
            self.queueLayout.insertWidget(0, elem)
            
        tmplist = []
        while self.recentLayout.count() > 1:
            tmplist.append(self.recentLayout.takeAt(0).widget())
        s = sorted(tmplist, key=lambda x: x.waiting) # not reverse as the already installed section is LIFO
        for elem in s:
            self.recentLayout.insertWidget(0, elem)
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
        except: pass
        
    def vote(self):
        if self.votedialog.isVisible():
            return
        
        p = self.sender().parent().parent() # yes, cludgy
        self.votedialog.setWindowTitle(p.name + " " + p.version)
        self.votedialog.pname = p.pname
        self.votedialog.version = p.version
        try: 
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, True)
            QApplication.processEvents()
        except: pass
        self.votedialog.id = p.getId()
        try:
            self.setAttribute(Qt.WA_Maemo5ShowProgressIndicator, False)
            QApplication.processEvents()
        except: pass
        self.votedialog.show()
        
#        self.votedialog.deleteLater()
#        self.votedialog = None
    
    @pyqtSlot(bool)
    def hideTested(self, b):
        for item in self.queueContents.children():
            try:
                if b and item.voted:
                    item.setVisible(False)
                else:
                    item.setVisible(True)
            except Exception, e:
                print e
        for item in self.recentContents.children():
            try:
                if b and item.voted:
                    item.setVisible(False)
                else:
                    item.setVisible(True)
            except Exception, e:
                print e
        
    @pyqtSlot(bool)
    def showRecent(self, b):
        self.recentScroll.setVisible(b)
        self.queueScroll.setVisible(not b)
        if not self.loggedin:
            self.loginRequested.emit()
        elif b and self.recentLayout.count() < 2:
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
