# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appitem.ui'
#
# Created: Sat Aug 14 02:32:35 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 345)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pname = QtGui.QLabel(Form)
        self.pname.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pname.setObjectName("pname")
        self.horizontalLayout_2.addWidget(self.pname)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pButton_bug = QtGui.QPushButton(Form)
        self.pButton_bug.setObjectName("pButton_bug")
        self.horizontalLayout_2.addWidget(self.pButton_bug)
        self.pButton_pdetails = QtGui.QPushButton(Form)
        self.pButton_pdetails.setObjectName("pButton_pdetails")
        self.horizontalLayout_2.addWidget(self.pButton_pdetails)
        self.pButton_install = QtGui.QPushButton(Form)
        self.pButton_install.setObjectName("pButton_install")
        self.horizontalLayout_2.addWidget(self.pButton_install)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.votedUpLabel = QtGui.QLabel(Form)
        self.votedUpLabel.setText("")
        self.votedUpLabel.setPixmap(QtGui.QPixmap(":/icons/favourite.png"))
        self.votedUpLabel.setObjectName("votedUpLabel")
        self.horizontalLayout.addWidget(self.votedUpLabel)
        self.votedDownLabel = QtGui.QLabel(Form)
        self.votedDownLabel.setText("")
        self.votedDownLabel.setPixmap(QtGui.QPixmap(":/icons/buried.png"))
        self.votedDownLabel.setObjectName("votedDownLabel")
        self.horizontalLayout.addWidget(self.votedDownLabel)
        self.pButton_vote = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pButton_vote.sizePolicy().hasHeightForWidth())
        self.pButton_vote.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/padlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pButton_vote.setIcon(icon)
        self.pButton_vote.setObjectName("pButton_vote")
        self.horizontalLayout.addWidget(self.pButton_vote)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

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
