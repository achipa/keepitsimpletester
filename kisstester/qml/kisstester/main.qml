import Qt 4.7
/*
Rectangle {
    anchors.fill: parent
    color: "tomato"
    opacity: 0.33
}
*/
Rectangle {
    width: 800
    height: 435
    id: main
    color: "#000000"
    property bool cludge: true // I know there is a better way to do this, I just can't remember it
/*    property ListModel packageListModel
: ListModel {       // test data for qmlviewer/bauhaus
        ListElement { name: "Apple" }
        ListElement { name: "Banana" }
        ListElement { name: "Orange" }
        ListElement { name: "Pear" }
        ListElement { name: "Plum" }
    }*/
    VisualDataModel {
        id: visualModel
        model: packageListModel
        delegate: Rectangle {
            width: 800
            height: 75
            color: "#000000"
            AppItem {
                id: item
                Timer { interval: index*200; running: index < 7 ? true : false; onTriggered: { if (index == 6) main.cludge = false; item.state = "" } }
                states: State {
                    name: "unloaded"
                    PropertyChanges {
                        target: item.parent
                        x: 800
                    }

                }
                state: cludge ? "unloaded" : ""

                transitions: Transition { NumberAnimation { target: item.parent; property: "x"; duration: 300; easing.type: Easing.OutQuad }  }

                anchors.horizontalCenter: parent.horizontalCenter
                appname: name.length > 36 ? name.substring(0, 36) + "..." : name
                appscore: "K: " + karma
                appage : age + "days"
                appunlocked: status
                appinstalled: installed
                appquarantine : age > 10
                // appupdated :
                appmyvote: vote
                appkarma: karma > 10

            }


        }
    }

    ListView {
        anchors.fill: parent
        model: visualModel
    }
    State {
        name: "blank"
        PropertyChanges {
            target: name

        }
    }
/*    MouseArea {
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }
    */
}
