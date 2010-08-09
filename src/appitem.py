
import os
import urllib2
from xml.dom.minidom import parseString

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
    def __init__(self, parent=0, data={ 'name' : "", "karma" : 0, "pname" : "", "version" : "", "status" : "", "waiting" : "", "voted" : False, "myvote" : False }):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.name = data["name"]
        self.karma = data["karma"]
        self.pname = data["pname"]
        self.version = data["version"]
        self.status = data["status"]
        self.waiting = data["waiting"]
        self.voted = data["voted"]
        self.myvote = data["myvote"]
        self.id = ""
        
        self.configure()
        
        self.connect(self.ui.pButton_install, SIGNAL("clicked()"), self.debInstall)
        self.connect(self.ui.pButton_pdetails, SIGNAL("clicked()"), self.debDetails)
        

    @pyqtSlot()
    def configure(self):
        self.ui.pButton_vote.setText("%s, Karma %s%s, %s" % (self.version, self.karma, self.status, self.waiting))
        self.ui.pname.setText(self.name)
        myvote = ""
        publicvote = ""
        if self.voted:
            # pButton_vote.setEnabled(False) # can't disable as then you couldn't change your vote
            if self.myvote:
                myvote = " border-style: outset; border-color: green; border-width: 2px;"
            else:
                myvote = " border-style: outset; border-color: red; border-width: 2px;"
        if self.status:
            publicvote = "color : green;"
        elif self.karma < 0:
            publicvote = "color : red;"
            
        self.ui.pButton_vote.setStyleSheet("QPushButton{ %s %s}" % (myvote, publicvote))

    @pyqtSlot()
    def debInstall(self):
        QMessageBox.information(self, "%s %s" % (self.name, self.version), "Insert install functionality here. I take patches.")
        
    @pyqtSlot()
    def debDetails(self):
        QMessageBox.information(self, "%s %s" % (self.name, self.version), "Insert details functionality here (REST, or, probably better, from apt-cache show). I take patches.")
        
    @pyqtSlot()
    def getId(self): # ugliest REST hack on the planet
        if self.id:
            return id
        
        xmlstr = urllib2.urlopen("http://maemo.org/packages/api/v1/content/data/?parent=fremantle_extras-testing_free_armel&search=%s" % self.pname).read()
        domm = xml.dom.minidom.parseString(xmlstr)
        for es in domm.getElementsByTagName("content"):
            tmpid = ""
            for child in es.childNodes:
                if child.tagName == "id":
                    tmpid = child.childNodes[0].data
                if child.tagName == "name":
                    tmpname = child.childNodes[0].data

            if tmpid and tmpname == self.name:
                self.id = tmpid
                
        return self.id
    

