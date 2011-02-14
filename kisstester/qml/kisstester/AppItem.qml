import Qt 4.7
import Qt.labs.particles 1.0

    Image {
        property string appname: "AppName"
        property string appscore: "K: 11"
        property string appage: "D: 11"
        property string appbugpage: "http://bugs.maemo.org"
        property bool appunlocked: true
        property bool appquarantine: false
        property bool appupdated: false
        property bool appkarma: false
        property bool appinstalled: false
        property int appmyvote: 0
        id: image5

        source: appmyvote == 0 ? "../images/unpressed_button_wide.png" :  "../images/pressed_button_wide.png"
        Rectangle {
            id: thumbanchor
            anchors.leftMargin: 15
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            width: thumb.width
            Image {
                id: thumb
                source: appmyvote > 0 ? "../images/thumbsup.png" : (appmyvote < 0 ? "../images/thumbsdown.png" : "" )
                SequentialAnimation {
                    running: appmyvote != 0
                    loops: Animation.Infinite
                    PropertyAnimation { target: thumb; property: "y"; from: -thumb.height/2; to: -10; duration: 2000;}
                    PropertyAnimation { target: thumb; property: "y"; from: -10; to: -thumb.height/2; duration: 2000;}
                }
            }
        }
        Text {
            id: appnametext
            color: "#ffffff"
            text: appname
            font.family: "Nokia Sans Cn"
            anchors.leftMargin: appmyvote == 0 ? 0 : 7
            anchors.left: thumbanchor.right
            anchors.verticalCenter: parent.verticalCenter
        }

        Text {
            id: scoretext
            color: "#ffffff"
            text: appscore
            font.family: "Nokia Sans Cn"
            anchors.verticalCenterOffset: 0
            anchors.leftMargin: 445
            anchors.left: image5.left
            anchors.verticalCenter: parent.verticalCenter
        }

        Text {
            id: agetext
            color: "#ffffff"
            text: appage
            font.family: "Nokia Sans Cn"
            anchors.verticalCenterOffset: 0
            anchors.leftMargin: 400
            anchors.left: image5.left
            anchors.verticalCenter: parent.verticalCenter
        }

        Text {
            id: action
            color: "#ffffff"
            text: appinstalled ? "Report bug" : "Install"
            font.family: "Nokia Sans SemiBold"
            anchors.verticalCenterOffset: 0
            anchors.rightMargin: 15
            anchors.right: image5.right
            anchors.verticalCenter: parent.verticalCenter
            Particles {
                id: bugburst
                anchors.centerIn: parent
                source:  "../images/star.png"
                lifeSpan: 1000
                count: 0
                angleDeviation: 360
                velocity: 100
                velocityDeviation: 30
            }
            MouseArea {
                id: reportbug
                anchors.fill: parent
                onClicked: { bugburst.burst(20); Qt.openUrlExternally(appbugpage); }
            }
       }

        MouseArea {
            enabled: appmyvote == 0 ? true: false
            id: pkgbutton
            anchors.right: image1.left
            anchors.left: image5.left
            anchors.top:  image5.top
            anchors.bottom: image5.bottom
            onClicked: { console.log("vote"); mw.vote(index); }
        }
        Image {
            id: image1
            x: 491
            anchors.verticalCenterOffset: 0
            source: appupdated ? "../images/icon1_active.png" : "../images/icon1_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
            MouseArea {
                id: updatedhelp
                anchors.fill: parent
            }
            NumberAnimation on rotation { from: 360; to: 0.0; duration: 60000; loops: Animation.Infinite; running: appupdated }
        }

        Image {
            id: image2
            anchors.left: image1.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appkarma ? "../images/icon2_active.png" : "../images/icon2_inactive.png"
            anchors.verticalCenter: image1.verticalCenter
            MouseArea {
                id: karmahelp
                anchors.fill: parent
            }
        }

        Image {
            id: image3
            anchors.left: image2.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appquarantine ? "../images/icon3_active.png" : "../images/icon3_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
            smooth: true
            MouseArea {
                id: quarantinehelp
                anchors.fill: parent
            }
            SequentialAnimation {
                running: !appquarantine
                loops: Animation.Infinite
                NumberAnimation { target: image3; property: "rotation"; easing.type: Easing.InOutExpo; from: 360; to: 180; duration: 10000;}
                NumberAnimation { target: image3; property: "rotation"; easing.type: Easing.InOutExpo; from: 180; to: 0; duration: 10000;}
            }
        }

        Image {
            id: image4
            anchors.left: image3.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appunlocked ? "../images/icon4_active.png" : "../images/icon4_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
            MouseArea {
                id: unlockhelp
                anchors.fill: parent
            }
            SequentialAnimation {
                running: appunlocked
                loops: Animation.Infinite
                NumberAnimation { target: image4; property: "scale"; easing.type: Easing.OutBounce; from: 0.6; to: 1.0; duration: 300;}
                NumberAnimation { target: image4; property: "scale"; from: 1.0; to: 0.6; duration: 30000;}
            }
        }

    }
