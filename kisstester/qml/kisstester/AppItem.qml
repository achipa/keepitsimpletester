import Qt 4.7

    Image {
        property string appname: "AppName"
        property string appscore: "K: 11"
        property string appage: "D: 11"
        property bool appunlocked: true
        property bool appquarantine: false
        property bool appupdated: false
        property bool appkarma: false
        property bool appinstalled: false
        property int appmyvote: 0
        id: image5

        source: appmyvote == 0 ? "../images/unpressed_button_wide.png" :  "../images/pressed_button_wide.png"
        Image {
            id: thumb
            anchors.leftMargin: 15
            anchors.verticalCenter: parent.verticalCenter
            source: appmyvote > 0 ? "../images/thumbsup.png" : (appmyvote < 0 ? "../images/thumbsdown.png" : "" )
            anchors.left: parent.left
        }
        Text {
            id: appnametext
            color: "#ffffff"
            text: appname
            font.family: "Nokia Sans Cn"
            anchors.leftMargin: appmyvote == 0 ? 0 : 7
            anchors.left: thumb.right
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
            text: appinstalled ? "Uninstall" : "Install"
            font.family: "Nokia Sans SemiBold"
            anchors.verticalCenterOffset: 0
            anchors.rightMargin: 15
            anchors.right: image5.right
            anchors.verticalCenter: parent.verticalCenter
        }

        Image {
            id: image1
            x: 491
            anchors.verticalCenterOffset: 0
            source: appunlocked ? "../images/icon1_active.png" : "../images/icon1_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
        }

        Image {
            id: image2
            anchors.left: image1.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appquarantine ? "../images/icon2_active.png" : "../images/icon2_inactive.png"
            anchors.verticalCenter: image1.verticalCenter
        }

        Image {
            id: image3
            anchors.left: image2.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appkarma ? "../images/icon3_active.png" : "../images/icon3_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
        }

        Image {
            id: image4
            anchors.left: image3.right
            anchors.leftMargin: 10
            anchors.verticalCenterOffset: 0
            source: appupdated ? "../images/icon4_active.png" : "../images/icon4_inactive.png"
            anchors.verticalCenter: parent.verticalCenter
        }

    }
