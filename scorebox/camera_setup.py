import sys
import cv2
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt, QThread, Signal, Slot
from PySide2.QtGui import QImage, QPixmap
from GUI.camera_setup_ui import Ui_MainWindow

class CameraThread(QThread):
    frame_update = Signal(QImage)

    def run(self):
        cap = cv2.VideoCapture(1)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                # print(rgbImage.shape)
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio)
                self.frame_update.emit(p)

class CameraSetup(QMainWindow):
    def __init__(self):
        super(CameraSetup, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        camera_thread = CameraThread(self)
        camera_thread.frame_update.connect(self.update_frame)
        camera_thread.start()

    @Slot(QImage)
    def update_frame(self, frame):
        pixmap = QPixmap.fromImage(frame)
        geo = self.ui.camera_feed_viewer.geometry()
        pixmap = pixmap.scaled(geo.width(), geo.height(), Qt.KeepAspectRatio)
        self.ui.camera_feed_viewer.setPixmap(pixmap)

if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = CameraSetup()
    WINDOW.show()
    sys.exit(APP.exec_())