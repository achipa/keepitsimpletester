# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vote.ui'
#
# Created: Sun Sep 12 02:27:49 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 741)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 3, -1, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 972, 708))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.cBox_lic = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_lic.setObjectName("cBox_lic")
        self.verticalLayout_2.addWidget(self.cBox_lic)
        self.cBox_dub = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_dub.setObjectName("cBox_dub")
        self.verticalLayout_2.addWidget(self.cBox_dub)
        self.cBox_brk = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_brk.setObjectName("cBox_brk")
        self.verticalLayout_2.addWidget(self.cBox_brk)
        self.cBox_opt = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_opt.setObjectName("cBox_opt")
        self.verticalLayout_2.addWidget(self.cBox_opt)
        self.cBox_cpu = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_cpu.setObjectName("cBox_cpu")
        self.verticalLayout_2.addWidget(self.cBox_cpu)
        self.cBox_pwr = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cBox_pwr.setObjectName("cBox_pwr")
        self.verticalLayout_2.addWidget(self.cBox_pwr)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pButton_page = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pButton_page.setObjectName("pButton_page")
        self.horizontalLayout.addWidget(self.pButton_page)
        self.pButton_detail = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pButton_detail.setObjectName("pButton_detail")
        self.horizontalLayout.addWidget(self.pButton_detail)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.showCommentsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.showCommentsButton.setObjectName("showCommentsButton")
        self.verticalLayout_2.addWidget(self.showCommentsButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favourite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.passButton.setIcon(icon)
        self.passButton.setObjectName("passButton")
        self.horizontalLayout_2.addWidget(self.passButton)
        self.commentButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.commentButton.setObjectName("commentButton")
        self.horizontalLayout_2.addWidget(self.commentButton)
        self.failButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/buried.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.failButton.setIcon(icon1)
        self.failButton.setObjectName("failButton")
        self.horizontalLayout_2.addWidget(self.failButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Fulfilled criteria (required for passing an application):", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_lic.setText(QtGui.QApplication.translate("MainWindow", "Contains only properly licensed content", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_dub.setText(QtGui.QApplication.translate("MainWindow", "No dubious content (adult, violence, racism, etc)", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_brk.setText(QtGui.QApplication.translate("MainWindow", "No broken basic functionality", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_opt.setText(QtGui.QApplication.translate("MainWindow", "Optified", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_cpu.setText(QtGui.QApplication.translate("MainWindow", "No unreasonable CPU or resource usage", None, QtGui.QApplication.UnicodeUTF8))
        self.cBox_pwr.setText(QtGui.QApplication.translate("MainWindow", "No power management issues", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_page.setText(QtGui.QApplication.translate("MainWindow", "Use classic (web) interface", None, QtGui.QApplication.UnicodeUTF8))
        self.pButton_detail.setText(QtGui.QApplication.translate("MainWindow", "QA docs", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Detailed description of issues found (required for failing an application):", None, QtGui.QApplication.UnicodeUTF8))
        self.showCommentsButton.setText(QtGui.QApplication.translate("MainWindow", "Show previous comments", None, QtGui.QApplication.UnicodeUTF8))
        self.passButton.setText(QtGui.QApplication.translate("MainWindow", "PASS", None, QtGui.QApplication.UnicodeUTF8))
        self.commentButton.setText(QtGui.QApplication.translate("MainWindow", "Comment only", None, QtGui.QApplication.UnicodeUTF8))
        self.failButton.setText(QtGui.QApplication.translate("MainWindow", "FAIL", None, QtGui.QApplication.UnicodeUTF8))

import kisstester_rc
