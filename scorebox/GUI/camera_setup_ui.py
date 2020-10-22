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
        MainWindow.setStyleSheet(u"background-color: #1a1a1a;")
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
        self.side_header = QWidget(self.centralwidget)
        self.side_header.setObjectName(u"side_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.side_header.sizePolicy().hasHeightForWidth())
        self.side_header.setSizePolicy(sizePolicy2)
        self.side_header.setMinimumSize(QSize(150, 0))
        self.side_header.setMaximumSize(QSize(150, 16777215))
        self.side_header.setStyleSheet(u"image: url(:/side_headers/side_header_camera_setup.png);")

        self.gridLayout.addWidget(self.side_header, 1, 0, 1, 1)

        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy3)
        self.header.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_2 = QGridLayout(self.header)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QWidget(self.header)
        self.logo.setObjectName(u"logo")
        sizePolicy2.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setMinimumSize(QSize(200, 0))
        self.logo.setStyleSheet(u"image: url(:/logos/scorebox_logo_crop_white.png);")

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.header)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)

        self.camera_setup = QWidget(self.centralwidget)
        self.camera_setup.setObjectName(u"camera_setup")
        self.camera_container = QWidget(self.camera_setup)
        self.camera_container.setObjectName(u"camera_container")
        self.camera_container.setGeometry(QRect(230, 30, 531, 411))
        self.camera_feed_label = QLabel(self.camera_container)
        self.camera_feed_label.setObjectName(u"camera_feed_label")
        self.camera_feed_label.setGeometry(QRect(0, 0, 121, 41))
        font = QFont()
        font.setFamily(u"League Gothic Italic")
        font.setPointSize(18)
        self.camera_feed_label.setFont(font)
        self.camera_feed_label.setStyleSheet(u"color: white;")
        self.camera_feed_label.setScaledContents(False)
        self.camera_feed_viewer = QLabel(self.camera_container)
        self.camera_feed_viewer.setObjectName(u"camera_feed_viewer")
        self.camera_feed_viewer.setGeometry(QRect(0, 80, 431, 191))
        self.camera_feed_viewer.setStyleSheet(u"background-color: #333333;")
        self.camera_feed_viewer.setScaledContents(False)

        self.gridLayout.addWidget(self.camera_setup, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScoreBox", None))
        self.camera_feed_label.setText(QCoreApplication.translate("MainWindow", u"CAMERA FEED", None))
        self.camera_feed_viewer.setText("")
    # retranslateUi

