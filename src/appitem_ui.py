# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appitem.ui'
#
# Created: Sun Aug 15 21:00:31 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 82)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pButton_vote = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pButton_vote.sizePolicy().hasHeightForWidth())
        self.pButton_vote.setSizePolicy(sizePolicy)
        self.pButton_vote.setObjectName("pButton_vote")
        self.horizontalLayout.addWidget(self.pButton_vote)
        self.scoreAgeLabel = QtGui.QLabel(Form)
        self.scoreAgeLabel.setObjectName("scoreAgeLabel")
        self.horizontalLayout.addWidget(self.scoreAgeLabel)
        self.quarantineLabel = QtGui.QLabel(Form)
        self.quarantineLabel.setText("")
        self.quarantineLabel.setPixmap(QtGui.QPixmap(":/icons/wait.png"))
        self.quarantineLabel.setObjectName("quarantineLabel")
        self.horizontalLayout.addWidget(self.quarantineLabel)
        self.hasvotesLabel = QtGui.QLabel(Form)
        self.hasvotesLabel.setText("")
        self.hasvotesLabel.setPixmap(QtGui.QPixmap(":/icons/pass.png"))
        self.hasvotesLabel.setObjectName("hasvotesLabel")
        self.horizontalLayout.addWidget(self.hasvotesLabel)
        self.unlockedLabel = QtGui.QLabel(Form)
        self.unlockedLabel.setText("")
        self.unlockedLabel.setPixmap(QtGui.QPixmap(":/icons/padlock_open.png"))
        self.unlockedLabel.setObjectName("unlockedLabel")
        self.horizontalLayout.addWidget(self.unlockedLabel)
        self.pButton_bug = QtGui.QPushButton(Form)
        self.pButton_bug.setObjectName("pButton_bug")
        self.horizontalLayout.addWidget(self.pButton_bug)
        self.pButton_pdetails = QtGui.QPushButton(Form)
        self.pButton_pdetails.setObjectName("pButton_pdetails")
        self.horizontalLayout.addWidget(self.pButton_pdetails)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_vote.setText(QtGui.QApplication.translate("Form", "Version & Vote", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreAgeLabel.setText(QtGui.QApplication.translate("Form", "0/0", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_bug.setText(QtGui.QApplication.translate("Form", "Report bug", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_pdetails.setText(QtGui.QApplication.translate("Form", "Details", None, QtGui.QApplication.UnicodeUTF8))

import kisstester_rc
