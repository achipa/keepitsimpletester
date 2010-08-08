# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vote.ui'
#
# Created: Sun Aug  8 00:59:04 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(855, 575)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cBox_bug = QtGui.QCheckBox(Dialog)
        self.cBox_bug.setObjectName("cBox_bug")
        self.verticalLayout.addWidget(self.cBox_bug)
        self.cBox_lic = QtGui.QCheckBox(Dialog)
        self.cBox_lic.setObjectName("cBox_lic")
        self.verticalLayout.addWidget(self.cBox_lic)
        self.cBox_dub = QtGui.QCheckBox(Dialog)
        self.cBox_dub.setObjectName("cBox_dub")
        self.verticalLayout.addWidget(self.cBox_dub)
        self.cBox_brk = QtGui.QCheckBox(Dialog)
        self.cBox_brk.setObjectName("cBox_brk")
        self.verticalLayout.addWidget(self.cBox_brk)
        self.cBox_opt = QtGui.QCheckBox(Dialog)
        self.cBox_opt.setObjectName("cBox_opt")
        self.verticalLayout.addWidget(self.cBox_opt)
        self.cBox_cpu = QtGui.QCheckBox(Dialog)
        self.cBox_cpu.setObjectName("cBox_cpu")
        self.verticalLayout.addWidget(self.cBox_cpu)
        self.cBox_pwr = QtGui.QCheckBox(Dialog)
        self.cBox_pwr.setObjectName("cBox_pwr")
        self.verticalLayout.addWidget(self.cBox_pwr)
        self.pButton_detail = QtGui.QPushButton(Dialog)
        self.pButton_detail.setObjectName("pButton_detail")
        self.verticalLayout.addWidget(self.pButton_detail)
        self.pButton_page = QtGui.QPushButton(Dialog)
        self.pButton_page.setObjectName("pButton_page")
        self.verticalLayout.addWidget(self.pButton_page)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passButton = QtGui.QPushButton(Dialog)
        self.passButton.setObjectName("passButton")
        self.horizontalLayout.addWidget(self.passButton)
        self.failButton = QtGui.QPushButton(Dialog)
        self.failButton.setObjectName("failButton")
        self.horizontalLayout.addWidget(self.failButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Fulfilled criteria (required for passing an application):", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_bug.setText(QtGui.QApplication.translate("Dialog", "Has proper bugtracking", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_lic.setText(QtGui.QApplication.translate("Dialog", "Contains only properly licensed content", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_dub.setText(QtGui.QApplication.translate("Dialog", "No dubious content (adult, violence, racism, etc)", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_brk.setText(QtGui.QApplication.translate("Dialog", "No broken basic functionality", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_opt.setText(QtGui.QApplication.translate("Dialog", "Optified", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_cpu.setText(QtGui.QApplication.translate("Dialog", "No unreasonable CPU or resource usage", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_pwr.setText(QtGui.QApplication.translate("Dialog", "No power management issues", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_detail.setText(QtGui.QApplication.translate("Dialog", "Detailed description of the above criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_page.setText(QtGui.QApplication.translate("Dialog", "Go to maemo.org testing page", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Detailed description of issues found (required for failing an application):", None, QtGui.QApplication.UnicodeUTF8))
        self.passButton.setText(QtGui.QApplication.translate("Dialog", "PASS", None, QtGui.QApplication.UnicodeUTF8))
        self.failButton.setText(QtGui.QApplication.translate("Dialog", "FAIL", None, QtGui.QApplication.UnicodeUTF8))

