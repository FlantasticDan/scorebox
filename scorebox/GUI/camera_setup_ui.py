# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_setup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import scorebox_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setBaseSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color: #1a1a1a;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #32a849;\n"
"border: 3px solid  #32a849;\n"
"outline: 5px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#63cf77;\n"
"border: 3px solid  #63cf77;\n"
"}\n"
"\n"
"QPushButton[pushButtonType=\"radio\"]{\n"
"background-color: #3366ff;\n"
"border: 3px solid  #3366ff;\n"
"outline: 5px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton[pushButtonType=\"radio\"]:hover{\n"
"background-color:#5983ff;\n"
"border: 3px solid  #5983ff;\n"
"}\n"
"\n"
"QPushButton[pushButtonType=\"radio\"]:!checked{\n"
"background-color: rgba(0,0,0,0);\n"
"border: 3px solid  #3366ff;\n"
"}\n"
"\n"
"QPushButton[pushButtonType=\"radio\"]:!checked:hover{\n"
"background-color: rgba(0,0,0,0);\n"
"border: 3px solid  #5983ff;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgba(0,0,0,0);\n"
"	border: 3px solid #6e6e6e;\n"
"	padding-left: 10px;\n"
"	text-align: center center;\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemVie"
                        "w {\n"
"	background-color: #6e6e6e;\n"
"	border: 3px solid #6e6e6e;\n"
"	text-align: center center;\n"
"	color: white;\n"
"\n"
"	outline: none;\n"
"	selection-background-color: #3b3b3b;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(:/icons/down-arrow.png);\n"
"	width: 16px;\n"
"	image-position: center center;\n"
"	right: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.camera_setup = QWidget(self.centralwidget)
        self.camera_setup.setObjectName(u"camera_setup")
        self.camera_container = QWidget(self.camera_setup)
        self.camera_container.setObjectName(u"camera_container")
        self.camera_container.setGeometry(QRect(0, 0, 571, 431))
        self.camera_feed_label = QLabel(self.camera_container)
        self.camera_feed_label.setObjectName(u"camera_feed_label")
        self.camera_feed_label.setGeometry(QRect(9, 9, 100, 32))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.camera_feed_label.sizePolicy().hasHeightForWidth())
        self.camera_feed_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"League Gothic Italic")
        font.setPointSize(20)
        self.camera_feed_label.setFont(font)
        self.camera_feed_label.setStyleSheet(u"color: white;")
        self.camera_feed_label.setScaledContents(False)
        self.stackedWidget = QStackedWidget(self.camera_container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 47, 551, 381))
        self.stackedWidget.setStyleSheet(u".QWidget{\n"
"	background: #333333;\n"
"}\n"
"QLabel{\n"
"	background: rgba(0,0,0,0);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setMinimumSize(QSize(352, 200))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 160, 131, 40))
        font1 = QFont()
        font1.setFamily(u"Staatliches")
        font1.setPointSize(18)
        self.pushButton_3.setFont(font1)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 50, 170, 35))
        font2 = QFont()
        font2.setFamily(u"League Gothic")
        font2.setPointSize(18)
        self.pushButton.setFont(font2)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(False)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 351, 21))
        font3 = QFont()
        font3.setFamily(u"Staatliches")
        font3.setPointSize(16)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 110, 351, 35))
        self.comboBox.setFont(font2)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 50, 171, 35))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        self.pushButton_2.setFlat(False)

        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.camera_feed_viewer = QLabel(self.page_2)
        self.camera_feed_viewer.setObjectName(u"camera_feed_viewer")
        self.camera_feed_viewer.setStyleSheet(u"background-color: #333333;")
        self.camera_feed_viewer.setScaledContents(False)

        self.verticalLayout.addWidget(self.camera_feed_viewer)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.camera_setup, 1, 1, 1, 1)

        self.side_header = QWidget(self.centralwidget)
        self.side_header.setObjectName(u"side_header")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.side_header.sizePolicy().hasHeightForWidth())
        self.side_header.setSizePolicy(sizePolicy4)
        self.side_header.setMinimumSize(QSize(150, 0))
        self.side_header.setMaximumSize(QSize(150, 16777215))
        self.side_header.setStyleSheet(u"image: url(:/side_headers/side_header_camera_setup.png);")

        self.gridLayout.addWidget(self.side_header, 1, 0, 1, 1)

        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy5)
        self.header.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QWidget(self.header)
        self.logo.setObjectName(u"logo")
        sizePolicy4.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy4)
        self.logo.setMinimumSize(QSize(200, 0))
        self.logo.setStyleSheet(u"image: url(:/logos/scorebox_logo_crop_white.png);")

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScoreBox", None))
        self.camera_feed_label.setText(QCoreApplication.translate("MainWindow", u"CAMERA FEED", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"720p", None))
        self.pushButton.setProperty("pushButtonType", QCoreApplication.translate("MainWindow", u"radio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAMERA  INPUT  SETTINGS", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"webcam", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"dslr", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1080p", None))
        self.pushButton_2.setProperty("pushButtonType", QCoreApplication.translate("MainWindow", u"radio", None))
        self.camera_feed_viewer.setText("")
    # retranslateUi

