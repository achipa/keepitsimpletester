# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appitem2.ui'
#
# Created: Wed Aug 18 02:01:38 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 70)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 70))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thumbLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbLabel.sizePolicy().hasHeightForWidth())
        self.thumbLabel.setSizePolicy(sizePolicy)
        self.thumbLabel.setMinimumSize(QtCore.QSize(26, 0))
        self.thumbLabel.setPixmap(QtGui.QPixmap(":/appitem/images/thumbsup.png"))
        self.thumbLabel.setObjectName("thumbLabel")
        self.horizontalLayout.addWidget(self.thumbLabel)
        self.pButton_vote = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pButton_vote.sizePolicy().hasHeightForWidth())
        self.pButton_vote.setSizePolicy(sizePolicy)
        self.pButton_vote.setMinimumSize(QtCore.QSize(280, 0))
        self.pButton_vote.setMaximumSize(QtCore.QSize(280, 16777215))
        self.pButton_vote.setFlat(True)
        self.pButton_vote.setObjectName("pButton_vote")
        self.horizontalLayout.addWidget(self.pButton_vote)
        self.scoreAgeLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreAgeLabel.sizePolicy().hasHeightForWidth())
        self.scoreAgeLabel.setSizePolicy(sizePolicy)
        self.scoreAgeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.scoreAgeLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.scoreAgeLabel.setObjectName("scoreAgeLabel")
        self.horizontalLayout.addWidget(self.scoreAgeLabel)
        self.upgradeLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upgradeLabel.sizePolicy().hasHeightForWidth())
        self.upgradeLabel.setSizePolicy(sizePolicy)
        self.upgradeLabel.setPixmap(QtGui.QPixmap(":/appitem/images/icon1_inactive.png"))
        self.upgradeLabel.setObjectName("upgradeLabel")
        self.horizontalLayout.addWidget(self.upgradeLabel)
        self.voteLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voteLabel.sizePolicy().hasHeightForWidth())
        self.voteLabel.setSizePolicy(sizePolicy)
        self.voteLabel.setPixmap(QtGui.QPixmap(":/appitem/images/icon2_inactive.png"))
        self.voteLabel.setObjectName("voteLabel")
        self.horizontalLayout.addWidget(self.voteLabel)
        self.quarantineLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quarantineLabel.sizePolicy().hasHeightForWidth())
        self.quarantineLabel.setSizePolicy(sizePolicy)
        self.quarantineLabel.setText("")
        self.quarantineLabel.setPixmap(QtGui.QPixmap(":/appitem/images/icon3_inactive.png"))
        self.quarantineLabel.setObjectName("quarantineLabel")
        self.horizontalLayout.addWidget(self.quarantineLabel)
        self.unlockedLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unlockedLabel.sizePolicy().hasHeightForWidth())
        self.unlockedLabel.setSizePolicy(sizePolicy)
        self.unlockedLabel.setPixmap(QtGui.QPixmap(":/appitem/images/icon4_inactive.png"))
        self.unlockedLabel.setObjectName("unlockedLabel")
        self.horizontalLayout.addWidget(self.unlockedLabel)
        self.pButton_details = QtGui.QPushButton(self.widget)
        self.pButton_details.setMinimumSize(QtCore.QSize(120, 0))
        self.pButton_details.setFlat(True)
        self.pButton_details.setObjectName("pButton_details")
        self.horizontalLayout.addWidget(self.pButton_details)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("Form", "QWidget#widget {\n"
"   border: none;\n"
"   background-image: url(:/appitem/images/unpressed_button.png);\n"
"   background-repeat: None;\n"
"   top 2px;\n"
"}", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_vote.setStyleSheet(QtGui.QApplication.translate("Form", "QPushButton#pButton_vote {\n"
"text-align: left;\n"
"font-family: \"Nokia Sans Cn\";\n"
"}", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_vote.setText(QtGui.QApplication.translate("Form", "Appname", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreAgeLabel.setText(QtGui.QApplication.translate("Form", "k:8 d:8", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_details.setStyleSheet(QtGui.QApplication.translate("Form", "QPushButton {\n"
"font: \"Nokia Sans Cn\"\n"
"}", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_details.setText(QtGui.QApplication.translate("Form", "Install", None, QtGui.QApplication.UnicodeUTF8))

import kisstester_rc
