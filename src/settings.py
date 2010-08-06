
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except Exception, e:
    import logging
    logging.critical("Uh, oh, you seem to be missing PyQT4 !\nHave you tried 'apt-get install python2.5-qt4-gui' ?")
    exit()

try:
    if os.path.getmtime("settings.ui") > os.path.getmtime("settings_ui.py"):
        raise Exception()
except:
    import subprocess
    subprocess.call(["pyuic4", "settings.ui", "-o", "settings_ui.py"])
from settings_ui import Ui_Dialog

class Settings(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.data = QSettings("kisstester","main")
        sd = Ui_Dialog()
        sd.setupUi(self)
        
    def show():
        if self.dialog.execute():
            self.data.setValue("username", self.dialog.user.text())
            self.data.setValue("password", self.dialog.passw.text())
            self.data.sync()
        
        
    