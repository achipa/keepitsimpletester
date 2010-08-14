# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sat Aug 14 22:44:19 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 108)
        self.formLayout_2 = QtGui.QFormLayout(Dialog)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.user = QtGui.QLineEdit(Dialog)
        self.user.setObjectName("user")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.user)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passw = QtGui.QLineEdit(Dialog)
        self.passw.setEchoMode(QtGui.QLineEdit.Password)
        self.passw.setObjectName("passw")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passw)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.registerLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName("registerLabel")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.registerLabel)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Login parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "maemo.org username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.registerLabel.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://garage.maemo.org/account/register.php\"><span style=\" text-decoration: underline; color:#0057ae;\">Register for maemo.org account</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

