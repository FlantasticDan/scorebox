import sys
import GUI.resource_path
import cv2
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtGui import QImage, QPixmap
from GUI.scorebox_ui import Ui_MainWindow
from camera_setup import CameraSetup

class ScoreBox(QMainWindow):
    def __init__(self):
        super(ScoreBox, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dynamic_property_styling()

        self.camera_setup = CameraSetup(self)

    def dynamic_property_styling(self):
        self.ui.hd_toggle.setProperty("pushButtonType", "radio")
        self.ui.hd_toggle.setStyle(self.ui.hd_toggle.style())
        self.ui.fhd_toggle.setProperty("pushButtonType", "radio")
        self.ui.fhd_toggle.setStyle(self.ui.fhd_toggle.style())

if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = ScoreBox()
    WINDOW.show()
    sys.exit(APP.exec_())
