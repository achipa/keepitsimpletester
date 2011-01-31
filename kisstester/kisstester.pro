# Add more folders to ship with the application, here
folder_01.source = qml/kisstester
folder_01.target = qml
folder_02.source = qml/images
folder_02.target = qml
DEPLOYMENTFOLDERS = folder_01 folder_02

# Additional import path used to resolve QML modules in Creator's code model
QML_IMPORT_PATH =

# Avoid auto screen rotation
DEFINES += ORIENTATIONLOCK

QT += network webkit

maemo5 {
    QT += maemo5
}
# Needs to be defined for Symbian
#DEFINES += NETWORKACCESS

symbian:TARGET.UID3 = 0xE58FF592

# Define QMLJSDEBUGGER to allow debugging of QML in debug builds
# (This might significantly increase build time)
#DEFINES += QMLJSDEBUGGER

# If your application uses the Qt Mobility libraries, uncomment
# the following lines and add the respective components to the 
# MOBILITY variable. 
# CONFIG += mobility
# MOBILITY +=
# The .cpp file which was generated for your project. Feel free to hack it.
SOURCES += main.cpp \
    mainwindow.cpp \
    extraspackage.cpp

# Please do not modify the following two lines. Required for deployment.
include(qmlapplicationviewer/qmlapplicationviewer.pri)
qtcAddDeployment()

RESOURCES += \
    kisstester.qrc

FORMS += \
    mainwindow.ui

HEADERS += \
    mainwindow.h \
    extraspackage.h
