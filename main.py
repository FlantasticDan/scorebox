import sys
import functools
from threading import Thread

from PySide6.QtCore import Qt, QMargins, Signal, Slot, QObject
from PySide6.QtGui import QPixmap, QFontDatabase, QImage
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton, QSizePolicy

import cv2

from camera_manager import list_camera_devices
from camera_manager import CameraManager
from scoreboard_manager import ScoreboardManager

import styles

class GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.source = -1

        self.camera_manager = None

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
        self.camera_manager = CameraManager(self.source)
        self.stream.attach_camera_manager(self.camera_manager)


class Header(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setMaximumHeight(75)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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

        self.camera_manager: CameraManager = None
        self.scoreboard_manager: ScoreboardManager = None

        self.frame_source = None
        self.frame_update_thread: Thread = None
        self.frame_signal = FrameSignal().frame_signal

        self.stream_viewer = QLabel()
        self.stream_viewer.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.stream_viewer)

    def resizeEvent(self, e):
        if self.frame_update_thread is None:
            geo = self.geometry()
            no_signal = QPixmap(r'assets\no_signal.png')
            no_signal = no_signal.scaled(geo.width() - 20, geo.height() - 20, Qt.KeepAspectRatio)
            self.stream_viewer.setPixmap(no_signal)

    def attach_camera_manager(self, camera_manager: CameraManager):
        self.camera_manager = camera_manager
        self.frame_source = self.camera_manager
        self.frame_signal.connect(self.draw_updated_frame)
        self.frame_update_thread = Thread(target=self.update_frame)
        self.frame_update_thread.start()

    def update_frame(self):
        while True:
            if self.frame_source.frame is not None:
                rgb_image = cv2.cvtColor(self.frame_source.frame, cv2.COLOR_BGR2RGB)
                height, width, channels = rgb_image.shape
                bytes_per_line = width * channels
                image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                image = image.scaled(self.width() - 20, self.height() - 20, Qt.KeepAspectRatio)
                self.frame_signal.emit(image.copy())
        print('EXITING')

    @Slot(QImage)
    def draw_updated_frame(self, new_frame: QImage):
        self.stream_viewer.setPixmap(QPixmap.fromImage(new_frame))

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
    '''UI for choosing camera source.'''
    def __init__(self, interactive: Interactive):
        QFrame.__init__(self)

        self.selected_source = -1
        self.interactive = interactive

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
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
        '''Set the user selected source and send the choice upstream'''
        self.selected_source = source
        self.interactive.source_selected(source)

class FrameSignal(QObject):
    '''Qt Required Signal Wrapper in QObject for Frame Draw Update Signal'''
    frame_signal = Signal(QImage)

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

    app.exec_()
