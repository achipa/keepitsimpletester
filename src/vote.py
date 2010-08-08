import os

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.getmtime("vote.ui") > os.path.getmtime("vote_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "vote.ui", "-o", "vote_ui.py"])
from vote_ui import Ui_Dialog

class Vote(QMainWindow):
    def __init__(self, parent=0):
        QMainWindow.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        try:
            self.setAttribute(Qt.WA_Maemo5StackedWindow)
        except: pass
        self.ui.passButton.setEnabled(False)
        self.ui.failButton.setEnabled(False)
        self.connect(self.ui.cBox_cpu, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_brk, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_bug, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_dub, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_lic, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_opt, SIGNAL("clicked(bool)"), self.unlockCheck)
        self.connect(self.ui.cBox_pwr, SIGNAL("clicked(bool)"), self.unlockCheck)
        
        self.connect(self.ui.textEdit, SIGNAL("textChanged()"), self.unlockCheck)
       
        self.connect(self.ui.failButton, SIGNAL("clicked(bool)"), self.failVote)
        self.connect(self.ui.passButton, SIGNAL("clicked(bool)"), self.passVote)
        
    @pyqtSlot()
    def unlockCheck(self):
        if self.ui.cBox_cpu.isChecked() and self.ui.cBox_brk.isChecked() and self.ui.cBox_bug.isChecked() and self.ui.cBox_dub.isChecked() and self.ui.cBox_lic.isChecked() and self.ui.cBox_opt.isChecked() and self.ui.cBox_pwr.isChecked() :
            self.ui.passButton.setEnabled(True)
        else:
            self.ui.passButton.setEnabled(False)
            
        if len(self.ui.textEdit.toPlainText()) > 5:
            self.ui.failButton.setEnabled(True)
        else:
            self.ui.failButton.setEnabled(False)
            

    @pyqtSlot(bool)
    def passVote(self):
        self.thumb(True)
      
    @pyqtSlot(bool)
    def failVote(self):
        self.thumb(False)
      
    def thumb(self, b):
        if b:
            QMessageBox.information(self, "Pass :)","Package thumbed up. Or at least it would be if this method was implemented :)")
        else:
            QMessageBox.information(self, "Fail :(","Package thumbed down. Or at least it would be if this method was implemented :)")
    
    
        