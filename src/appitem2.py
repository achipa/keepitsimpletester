import os
import urllib2
from xml.dom.minidom import parseString
import webbrowser
import subprocess

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.exists("appitem2.ui") and os.path.getmtime("appitem2.ui") > os.path.getmtime("appitem2_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "appitem2.ui", "-o", "appitem2_ui.py"])
from appitem2_ui import Ui_Form

class AppItem(QWidget):
    def __init__(self, parent=0, data={ 'name' : "", "karma" : 0, "pname" : "", "version" : "", "status" : "", "waiting" : "", "voted" : False, "myvote" : False, "bugtracker" : "" }):
        QWidget.__init__(self)
        self.pkgcache = QSettings("kisstester", "pkginfo")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.installed = False
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
        
#        if not self.bugtracker:
#            self.ui.pButton_bug.setVisible(False)
            
        self.configure()
        
        #self.connect(self.ui.pButton_details, SIGNAL("clicked()"), self.debDetails)
#        self.connect(self.ui.pButton_bug, SIGNAL("clicked()"), self.bugReport)
        
    @pyqtSlot()
    def configure(self):
        """Setup button/widget states so they match object configuration"""
        
        flat = False
        
        if len(self.name) > 40:
            self.ui.pButton_vote.setText(self.name[0:40]+ "...")
        else:
            self.ui.pButton_vote.setText(self.name)

        if self.pkgcache.value(self.pname, "").toString() == "Y":
            self.ui.upgradeLabel.setPixmap(QPixmap(":/appitem/images/icon1_active.png"))
        elif self.pkgcache.value(self.pname, "").toString() != self.version:
            # not in cache
            print "caching %s extras status" % self.pname
            policy = subprocess.Popen(["/usr/bin/apt-cache showpkg %s" % str(self.pname)], shell=True, bufsize=8192, stdout=subprocess.PIPE).stdout.read()
            isinextras = False
            for line in policy.splitlines():
                if line.find("repository.maemo.org_extras_dists") > 0:
                    self.pkgcache.setValue(self.pname,"Y")
                    self.ui.upgradeLabel.setPixmap(QPixmap(":/appitem/images/icon1_active.png"))
                    isinextras = True
                    break
            else:
                self.pkgcache.setValue(self.pname,self.version)
                    
            self.pkgcache.sync()    
        
                
        if self.status: # unlocked
            flat = True
            self.ui.unlockedLabel.setPixmap(QPixmap(":/appitem/images/icon4_active.png"))
            self.ui.voteLabel.setPixmap(QPixmap(":/appitem/images/icon2_active.png"))
        elif self.karma >= 10:
            flat = True
            self.ui.voteLabel.setPixmap(QPixmap(":/appitem/images/icon2_active.png"))
            
        if self.age > 10:
            self.ui.quarantineLabel.setPixmap(QPixmap(":/appitem/images/icon3_active.png"))
                
        if not self.voted:
            self.ui.thumbLabel.setPixmap(QPixmap())
        elif not self.myvote:
            self.ui.thumbLabel.setPixmap(QPixmap(":/appitem/images/thumbsdown.png"))
            flat = True
        else:
            flat = True
            
        if flat:
            self.ui.widget.setStyleSheet(self.ui.widget.styleSheet().replace("unpress", "press"))
            self.ui.pButton_vote.setStyleSheet(self.ui.pButton_vote.styleSheet().replace("white", "gray"))
            
        self.ui.scoreAgeLabel.setText("k:%s d:%s" % (self.karma, self.age))

    @pyqtSlot()
    def debDetails(self):
        QMessageBox.information(self, "%s %s" % (self.name, self.version), "Insert details functionality here (REST, or, probably better, from apt-cache show). I take patches.")
        
    @pyqtSlot()
    def bugReport(self):
        """Send bugreport by invoking the application's bugtracker"""
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
    

