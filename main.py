import sys

from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QPixmap, QFontDatabase
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel

from PIL import Image

from camera_manager import list_camera_devices
from camera_manager import CameraManager
from scoreboard_manager import ScoreboardManager

import styles

class GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(0, 0, 1280, 960)
        self.setWindowTitle('ScoreBox')

        self.setStyleSheet(styles.main)

        self.header = Header()
        self.stream = Stream()
        self.interactive = Interactive()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.stream)
        self.layout.addWidget(self.interactive)
        self.layout.setContentsMargins(QMargins(0,0,0,0))

        self.show()

class Header(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setMaximumHeight(75)
        self.setStyleSheet(styles.header)

        self.logo = QPixmap(r'assets\scorebox_logo_crop_white.png')
        self.logo = self.logo.scaledToHeight(self.height(), Qt.TransformationMode.SmoothTransformation)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(self.logo)

        self.header_title = QLabel("Camera Setup")
        self.header_title.setStyleSheet(styles.header_label)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.logo_label)
        self.layout.addWidget(self.header_title)

class Stream(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setStyleSheet('background-color: green;')

class Interactive(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setStyleSheet('background-color: blue;')

if __name__ == '__main__':
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

    app = QApplication()

    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-CondensedItalic.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-CondensedRegular.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-Italic.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-Regular.otf')
    QFontDatabase.addApplicationFont(r'assets\Staatliches-Regular.ttf')

    gui = GUI()

    sys.exit(app.exec_())