# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Aug 18 01:02:21 2010
#      by: PyQt4 UI code generator 4.7.2
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
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recentScroll = QtGui.QScrollArea(self.centralwidget)
        self.recentScroll.setWidgetResizable(True)
        self.recentScroll.setObjectName("recentScroll")
        self.recentContents = QtGui.QWidget(self.recentScroll)
        self.recentContents.setGeometry(QtCore.QRect(0, 0, 866, 332))
        self.recentContents.setObjectName("recentContents")
        self.recentLayout = QtGui.QVBoxLayout(self.recentContents)
        self.recentLayout.setMargin(0)
        self.recentLayout.setObjectName("recentLayout")
        spacerItem = QtGui.QSpacerItem(20, 279, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.recentLayout.addItem(spacerItem)
        self.recentScroll.setWidget(self.recentContents)
        self.verticalLayout.addWidget(self.recentScroll)
        self.queueScroll = QtGui.QScrollArea(self.centralwidget)
        self.queueScroll.setWidgetResizable(True)
        self.queueScroll.setObjectName("queueScroll")
        self.queueContents = QtGui.QWidget(self.queueScroll)
        self.queueContents.setGeometry(QtCore.QRect(0, 0, 866, 331))
        self.queueContents.setObjectName("queueContents")
        self.queueLayout = QtGui.QVBoxLayout(self.queueContents)
        self.queueLayout.setMargin(0)
        self.queueLayout.setObjectName("queueLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 278, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.queueLayout.addItem(spacerItem1)
        self.queueScroll.setWidget(self.queueContents)
        self.verticalLayout.addWidget(self.queueScroll)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName("menubar")
        self.menuFremantle = QtGui.QMenu(self.menubar)
        self.menuFremantle.setObjectName("menuFremantle")
        MainWindow.setMenuBar(self.menubar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionReload_repository_data = QtGui.QAction(MainWindow)
        self.actionReload_repository_data.setObjectName("actionReload_repository_data")
        self.actionCommentList = QtGui.QAction(MainWindow)
        self.actionCommentList.setObjectName("actionCommentList")
        self.actionTesterList = QtGui.QAction(MainWindow)
        self.actionTesterList.setObjectName("actionTesterList")
        self.actionFilter_packages = QtGui.QAction(MainWindow)
        self.actionFilter_packages.setObjectName("actionFilter_packages")
        self.actionShow_only_unchecked = QtGui.QAction(MainWindow)
        self.actionShow_only_unchecked.setCheckable(True)
        self.actionShow_only_unchecked.setObjectName("actionShow_only_unchecked")
        self.menuFremantle.addAction(self.actionAbout)
        self.menuFremantle.addAction(self.actionAbout_Qt)
        self.menuFremantle.addAction(self.actionCommentList)
        self.menuFremantle.addAction(self.actionTesterList)
        self.menuFremantle.addAction(self.actionSettings)
        self.menuFremantle.addAction(self.actionReload_repository_data)
        self.menuFremantle.addAction(self.actionFilter_packages)
        self.menuFremantle.addAction(self.actionShow_only_unchecked)
        self.menubar.addAction(self.menuFremantle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "KISStester", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFremantle.setTitle(QtGui.QApplication.translate("MainWindow", "Fremantle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Login settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload_repository_data.setText(QtGui.QApplication.translate("MainWindow", "Reload repository data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommentList.setText(QtGui.QApplication.translate("MainWindow", "Package comment archive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTesterList.setText(QtGui.QApplication.translate("MainWindow", "Join the testing squad", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilter_packages.setText(QtGui.QApplication.translate("MainWindow", "Package filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_only_unchecked.setText(QtGui.QApplication.translate("MainWindow", "Show only unchecked", None, QtGui.QApplication.UnicodeUTF8))

