from PyQt4.QtCore import *

class aLoader(QThread):
    def __init__(self, opener, url, data=None):
        QThread.__init__(self)
        self.opener = opener
	self.url = url
        self.data = data
        self.content = ""

    def run(self):
        r = self.opener.open(self.url, self.data)
        self.content = r.read()
