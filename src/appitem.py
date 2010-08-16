
import os
import urllib2
from xml.dom.minidom import parseString
import webbrowser

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.exists("appitem.ui") and os.path.getmtime("appitem.ui") > os.path.getmtime("appitem_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "appitem.ui", "-o", "appitem_ui.py"])
from appitem_ui import Ui_Form

class AppItem(QWidget):
    def __init__(self, parent=0, data={ 'name' : "", "karma" : 0, "pname" : "", "version" : "", "status" : "", "waiting" : "", "voted" : False, "myvote" : False, "bugtracker" : "" }):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.name = data["name"]
        self.karma = data["karma"]
        self.pname = data["pname"]
        self.version = data["version"]
        self.status = data["status"]
        self.waiting = data["waiting"]
        self.age = QDateTime.fromString(self.waiting, "yyyy-MM-dd HH:mm UTC").daysTo(QDateTime.currentDateTime())
        self.voted = data["voted"]
        self.myvote = data["myvote"]
        self.bugtracker = data["bugtracker"]
        self.id = ""
        
        if not self.bugtracker:
            self.ui.pButton_bug.setVisible(False)
            
        self.configure()
        
        self.connect(self.ui.pButton_pdetails, SIGNAL("clicked()"), self.debDetails)
        self.connect(self.ui.pButton_bug, SIGNAL("clicked()"), self.bugReport)
        
    @pyqtSlot()
    def configure(self):
#        self.ui.pButton_vote.setText("%s, Karma %s, %s days old" % (self.version, self.karma, self.age))
        
        if self.name.length() > 40:
            self.ui.pButton_vote.setText(self.name[0:40]+ "...")
        else:
            self.ui.pButton_vote.setText(self.name)
            
        self.ui.updateLabel.setVisible(False)
        self.ui.unlockedLabel.setVisible(False)
        self.ui.hasvotesLabel.setVisible(False)
        self.ui.quarantineLabel.setVisible(False)
        if self.status: # unlocked
#            self.ui.pButton_vote.setIcon(QIcon())
            self.ui.unlockedLabel.setVisible(True)
            self.ui.scoreAgeLabel.setVisible(False)
            self.ui.pButton_vote.setFlat(True)
        else:
            if self.karma >= 10:
#            self.ui.pButton_vote.setIcon(QIcon(QPixmap(":/icons/clock.png")))
                self.ui.hasvotesLabel.setVisible(True)
            if self.age < 10:
                self.ui.quarantineLabel.setVisible(True)
                
        if self.voted:
            self.ui.pButton_vote.setFlat(True)
            if self.myvote:
                self.ui.pButton_vote.setIcon(QIcon(QPixmap(":/icons/favourite.png")))
            else:
                self.ui.pButton_vote.setIcon(QIcon(QPixmap(":/icons/buried.png")))
            
        self.ui.scoreAgeLabel.setText("%s/%s" % (self.karma, self.age))

    @pyqtSlot()
    def debDetails(self):
        QMessageBox.information(self, "%s %s" % (self.name, self.version), "Insert details functionality here (REST, or, probably better, from apt-cache show). I take patches.")
        
    @pyqtSlot()
    def bugReport(self):
#        if self.bugtracker.startswith("mailto"):
#            #send mail
#            pass
#        else:
        if self.bugtracker:
            webbrowser.open(self.bugtracker)
    
    @pyqtSlot()
    def getId(self): # ugliest REST hack on the planet
        if self.id:
            return id
        
        xmlstr = urllib2.urlopen("http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&search=%s" % self.pname).read()
        domm = parseString(xmlstr)
        for es in domm.getElementsByTagName("content"):
            tmpid = "" 
            tmpname = ""
            for child in es.childNodes:
                try:
                    if child.tagName == "id":
                        tmpid = child.childNodes[0].data
                    if child.tagName == "name":
                        tmpname = child.childNodes[0].data
                except: pass

            if tmpid and tmpname == self.pname:
                self.id = tmpid
                
        return self.id
    

