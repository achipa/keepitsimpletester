# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appitem.ui'
#
# Created: Wed Aug 11 23:02:50 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(365, 57)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pname = QtGui.QLabel(Form)
        self.pname.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pname.setObjectName("pname")
        self.horizontalLayout.addWidget(self.pname)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pButton_bug = QtGui.QPushButton(Form)
        self.pButton_bug.setObjectName("pButton_bug")
        self.horizontalLayout.addWidget(self.pButton_bug)
        self.pButton_pdetails = QtGui.QPushButton(Form)
        self.pButton_pdetails.setObjectName("pButton_pdetails")
        self.horizontalLayout.addWidget(self.pButton_pdetails)
        self.pButton_install = QtGui.QPushButton(Form)
        self.pButton_install.setObjectName("pButton_install")
        self.horizontalLayout.addWidget(self.pButton_install)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pButton_vote = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/padlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pButton_vote.setIcon(icon)
        self.pButton_vote.setObjectName("pButton_vote")
        self.verticalLayout.addWidget(self.pButton_vote)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pname.setText(QtGui.QApplication.translate("Form", "Packagename", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_bug.setText(QtGui.QApplication.translate("Form", "Report bug", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_pdetails.setText(QtGui.QApplication.translate("Form", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_install.setText(QtGui.QApplication.translate("Form", "Install", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_vote.setText(QtGui.QApplication.translate("Form", "Version & Vote", None, QtGui.QApplication.UnicodeUTF8))

import kisstester_rc
