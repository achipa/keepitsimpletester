import os

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.exists("settings.ui") and os.path.getmtime("settings.ui") > os.path.getmtime("settings_ui.py") and not os.path.exists("/dev/mmcblk0"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "settings.ui", "-o", "settings_ui.py"])
from settings_ui import Ui_Dialog

class Settings(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.data = QSettings("kisstester","main")
        self.sd = Ui_Dialog()
        self.sd.setupUi(self)
        
    def show(self):
        self.sd.user.setText(self.data.value("username","").toString())
        self.sd.passw.setText(self.data.value("password","").toString())
        if self.exec_() and self.accepted():
            self.data.setValue("username", self.sd.user.text())
            self.data.setValue("password", self.sd.passw.text())
            self.data.sync()
            return True
        
        return False
        
        
    
