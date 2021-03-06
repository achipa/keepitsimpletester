import os
import webbrowser
import urllib2, urllib

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.exists("vote.ui") and os.path.getmtime("vote.ui") > os.path.getmtime("vote_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "vote.ui", "-o", "vote_ui.py"])
from vote_ui import Ui_MainWindow

import settings

class Vote(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=0):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except: pass
        
        self.pname = ""
        self.version = ""
        self.id = "" # "46957f1e934411dfbd57954ef8a05a175a17" # pyqt's guinea pig id until the rest parser is in place
        self.settings = settings.Settings()
        self.failUnlocked = False
        self.passUnlocked = False
        
        self.connect(self.cBox_cpu, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.cBox_brk, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.cBox_dub, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.cBox_lic, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.cBox_opt, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.cBox_pwr, SIGNAL("clicked(bool)"), self.unlockCheck)
        
        self.connect(self.textEdit, SIGNAL("textChanged()"), self.unlockCheck)
       
        self.connect(self.pButton_detail, SIGNAL("clicked(bool)"), lambda: webbrowser.open("http://wiki.maemo.org/Extras-testing/QA_Checklist"))
        self.connect(self.pButton_page, SIGNAL("clicked(bool)"), lambda: webbrowser.open("http://maemo.org/packages/package_instance/view/fremantle_extras-testing_free_armel/%s/%s/" % (self.pname, self.version)))
                     
        self.connect(self.failButton, SIGNAL("clicked(bool)"), self.failVote)
        self.connect(self.passButton, SIGNAL("clicked(bool)"), self.passVote)
        self.connect(self.commentButton, SIGNAL("clicked(bool)"), self.comment)
        
    def show(self):
        self.cBox_cpu.setChecked(False)
        self.cBox_brk.setChecked(False)
        self.cBox_dub.setChecked(False)
        self.cBox_lic.setChecked(False)
        self.cBox_opt.setChecked(False)
        self.cBox_pwr.setChecked(False)
        self.textEdit.setText("")
        QMainWindow.show(self)
        
    @pyqtSlot()
    def unlockCheck(self):
        if self.cBox_cpu.isChecked() and self.cBox_brk.isChecked() and self.cBox_dub.isChecked() and self.cBox_lic.isChecked() and self.cBox_opt.isChecked() and self.cBox_pwr.isChecked() :
            self.passUnlocked = True
        else:
            self.passUnlocked = False
            
        if len(self.textEdit.toPlainText()) > 5:
            self.failUnlocked = True
        else:
            self.failUnlocked = False
            

    @pyqtSlot()
    def passVote(self):
        if self.passUnlocked:
            self.comment()
            self.thumb(True)
        else:
            QMessageBox.information(self, "Pass criteria missing","You need to check (or have a good indication) of all the criteria above (i.e. all the checkboxes need to be checked)")
      
    @pyqtSlot()
    def failVote(self):
        if self.failUnlocked:
#            if QMessageBox.Ok == QMessageBox.question(self, "Are you sure ?", "Remember, the reasons for failing an app should be based on severe issues. It's more of a 'does it work' rather than a 'how well does it work'. If in doubt, please consult the QA a documentation."):
            self.comment()
            self.thumb(False)
        else:
            QMessageBox.information(self, "Fail criteria missing","You need to supply a reason for failing this package. Remember, it's not about whether you like the application, how pretty or cool it is - it is about whether it negatively impacts your usage of your device and if it is well-behaved (isn't illegal, is possible to report errors, etc). The slickness/coolness of the app will be judged by awarding it with 1-5 stars in Extras, not here.")
      
    @pyqtSlot()
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
                QMessageBox.warning(self, "WARNING", "KISStester operating in read-only mode. Please check the testing-squad mailing-list before you do something you don't want to :)")
        except Exception, e:
            QMessageBox.warning(self, "Vote failed", str(e))
    
    
        
