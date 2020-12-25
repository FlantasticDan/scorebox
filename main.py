import sys
import functools

from PySide6.QtCore import Qt, QMargins
from PySide6.QtGui import QPixmap, QFontDatabase
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton

from PIL import Image

from camera_manager import list_camera_devices
from camera_manager import CameraManager
from scoreboard_manager import ScoreboardManager

import styles

class GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.source = -1

        self.setGeometry(0, 0, 1280, 960)
        self.setWindowTitle('ScoreBox')

        self.setStyleSheet(styles.main)

        self.header = Header()
        self.stream = Stream()
        self.interactive = Interactive(self)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.stream)
        self.layout.addWidget(self.interactive)
        self.layout.setContentsMargins(QMargins(0,0,0,0))

        self.show()

    def source_selected(self, source):
        self.source = source

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
    def __init__(self, gui_parent: GUI):
        QFrame.__init__(self)

        self.gui = gui_parent

        self.source_selection = SourceSelection(self)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.source_selection)

    def source_selected(self, source):
        self.gui.source_selected(source)
        self.source_selection.close()

class SourceSelection(QFrame):
    def __init__(self, interactive: Interactive):
        QFrame.__init__(self)

        self.selected_source = -1
        self.interactive = interactive

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignVCenter)
        self.instruction = QLabel(text='Camera Source')
        self.instruction.setStyleSheet(styles.instructions)
        self.instruction.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.instruction)

        self.buttons = QFrame()
        self.buttons.setStyleSheet(styles.buttons)
        self.buttons_layout = QHBoxLayout(self.buttons)

        self.inputs = list_camera_devices()
        self.push_buttons = list()
        for i, source in enumerate(self.inputs):
            self.push_buttons.append(QPushButton(text=source))
            self.push_buttons[i].clicked.connect(functools.partial(self.set_source, i))
            self.buttons_layout.addWidget(self.push_buttons[i])

        self.layout.addWidget(self.buttons)

    def set_source(self, source):
        self.selected_source = source
        self.interactive.source_selected(source)

if __name__ == '__main__':
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

    app = QApplication()

    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-CondensedItalic.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-CondensedRegular.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-Italic.otf')
    QFontDatabase.addApplicationFont(r'assets\LeagueGothic-Regular.otf')
    QFontDatabase.addApplicationFont(r'assets\Staatliches-Regular.ttf')
    QFontDatabase.addApplicationFont(r'assets\Roboto-Regular.ttf')

    gui = GUI()

    sys.exit(app.exec_())
