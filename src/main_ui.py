# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Aug  6 01:37:14 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 704)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recentButton = QtGui.QPushButton(self.centralwidget)
        self.recentButton.setCheckable(True)
        self.recentButton.setAutoExclusive(True)
        self.recentButton.setObjectName("recentButton")
        self.horizontalLayout.addWidget(self.recentButton)
        self.queueButton = QtGui.QPushButton(self.centralwidget)
        self.queueButton.setCheckable(True)
        self.queueButton.setAutoExclusive(True)
        self.queueButton.setObjectName("queueButton")
        self.horizontalLayout.addWidget(self.queueButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recentScroll = QtGui.QScrollArea(self.centralwidget)
        self.recentScroll.setWidgetResizable(True)
        self.recentScroll.setObjectName("recentScroll")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.recentScroll)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 866, 297))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 279, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.recentScroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.recentScroll)
        self.queueScroll = QtGui.QScrollArea(self.centralwidget)
        self.queueScroll.setWidgetResizable(True)
        self.queueScroll.setObjectName("queueScroll")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.queueScroll)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 866, 296))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(20, 278, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.queueScroll.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.queueScroll)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 23))
        self.menubar.setObjectName("menubar")
        self.menuFremantle = QtGui.QMenu(self.menubar)
        self.menuFremantle.setObjectName("menuFremantle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuFremantle.addAction(self.actionSettings)
        self.menuFremantle.addAction(self.actionAbout)
        self.menuFremantle.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuFremantle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.recentButton.setText(QtGui.QApplication.translate("MainWindow", "Recently installed", None, QtGui.QApplication.UnicodeUTF8))
        self.queueButton.setText(QtGui.QApplication.translate("MainWindow", "QA Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFremantle.setTitle(QtGui.QApplication.translate("MainWindow", "Fremantle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))

