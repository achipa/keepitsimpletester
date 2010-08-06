#!/usr/bin/python

import sys
import os
import subprocess
import time
import cookielib, urllib2, urllib
import parser

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    app = QApplication(sys.argv)
#    if os.path.exists("splash.png"):
#        image = QImage("splash.png")
#    else:
#        image = QImage("/usr/share/kisstester/splash.png")
#    splash = QSplashScreen(QPixmap.fromImage(image))
#    splash.show()
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.getmtime("main.ui") > os.path.getmtime("main_ui.py"):
        raise Exception()
except:
    subprocess.call(["pyuic4", "main.ui", "-o", "main_ui.py"])
from main_ui import Ui_MainWindow
    
import settings

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.settings = settings.Settings()
        self.loggedin = False
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

        self.packages = {}
        
        self.ui.queueScroll.setVisible(False)
        self.ui.recentScroll.setVisible(False)
        
        # populate recently installed scroller
        
        for filename in os.listdir("/var/lib/dpkg/info"):
            if not filename.endswith(".list"):
                continue
            
            # installed package
             
        self.connect(self.ui.actionSettings, SIGNAL("triggered()"), self.settings, 
                     SLOT("show()"))
        self.connect(self.ui.actionAbout, SIGNAL("triggered()"), 
                     lambda: QMessageBox.about(self, "KISStester", "An application to simplify the QA feedback for applications in the extras-testing repository of maemo.org"))
        self.connect(self.ui.actionAbout_Qt, SIGNAL("triggered()"), 
                     lambda: QApplication.instance().aboutQt())
        
        self.connect(self.ui.recentButton, SIGNAL("triggered(bool)"), 
                     lambda b: self.showRecent(b))
                     
#            http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&ordermode=new&search=hermes
#    mainw.connect(umw.actionAutorotate, SIGNAL("triggered(bool)"), lambda x: settings.setValue("autorotate", 0))

    def login(self):
        
#        garagedata = { "return_to" : "", "form_loginname" : "achipa" , "form_pw" : "123456", "login" : "Login+with+SSL" }
#        r = opener.open("https://garage.maemo.org/account/login.php", urllib.urlencode(garagedata))

        maemodata = { "username" : self.settings.data.value("username").toAscii(), "password" : self.settings.data.value("password").toAscii(), "midcom_services_auth_frontend_form_submit" : "Login" }
        try:
            r = self.opener.open("https://maemo.org", urllib.urlencode(maemodata))
            if r.read().find("http://static.maemo.org/style_maemo2009/img/logged.png") > 0:
                self.loggedin = True
                return True
        except Exception, e:
            print e
        finally:
            return False
            
         
#        "https://maemo.org/username=achipa&password=123456&midcom_services_auth_frontend_form_submit=Login"

        while not self.login():
            self.settings.show()
    
    def loadPackages(self):
        done = False
        page = 1
        while not done:
 #           try:
                r.self.opener.open("http://maemo.org/packages/repository/qa/fremantle_extras-testing/?org_openpsa_qbpager_packages_in_repo_page=" % page)
                content = r.read()
                p = parser.MyHTMLParser()
                p.feed(content)
                p.close()
                print p.packages
                if len(p.packages) == 0:
                    done = True
#            except:
#                done = True
                
    def showRecent(self, b):

        print "x"
        self.ui.recentScroll.setVisible(b)
        self.ui.queueScroll.setVisible(not b)
        if not self.loggedin:
            self.login()
        self.loadPackages()
        
def start():
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())
