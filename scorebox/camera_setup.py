import cv2
from pygrabber.dshow_graph import FilterGraph
from PySide2.QtCore import Qt, QThread, Signal, Slot, QObject
from PySide2.QtGui import QImage, QPixmap

class CameraSetup():

    def __init__(self, gui):
        self.gui = gui
        self.ui = gui.ui

        self.full_hd = True
        self.camera_thread = None

        self.setup_ui()

    def setup_ui(self):
        cameras = FilterGraph().get_input_devices()
        self.ui.input_combo_box.addItems(cameras)

        self.connect_buttons()

    def toggle_full_hd(self):
        if self.full_hd:
            self.ui.hd_toggle.setChecked(True)
            self.ui.fhd_toggle.setChecked(False)
            self.full_hd = False
        else:
            self.ui.hd_toggle.setChecked(False)
            self.ui.fhd_toggle.setChecked(True)
            self.full_hd = True
        
        self.gui.update()
    
    def get_resolution(self):
        if self.full_hd:
            return (1920, 1080)
        else:
            return (1280, 720)

    def connect_to_camera(self):
        self.frame_buffer = FrameBuffer()
        self.frame_update = self.frame_buffer.frame_update
        self.camera_thread = CameraThread(self.frame_update, self.get_resolution(), self.ui.input_combo_box.currentIndex())
        self.frame_update.connect(self.update_frame)
        self.camera_thread.start()

        self.ui.camera_stack.setCurrentIndex(1)
    
    def connect_buttons(self):
        self.ui.hd_toggle.clicked.connect(self.toggle_full_hd)
        self.ui.fhd_toggle.clicked.connect(self.toggle_full_hd)
        self.ui.connect_button.clicked.connect(self.connect_to_camera)

    @Slot(QImage)
    def update_frame(self, frame):
        pixmap = QPixmap.fromImage(frame)
        geo = self.ui.camera_feed_viewer.geometry()
        pixmap = pixmap.scaled(geo.width(), geo.height(), Qt.KeepAspectRatio)
        self.ui.camera_feed_viewer.setPixmap(pixmap)

class FrameBuffer(QObject):
    frame_update = Signal(QImage)

class CameraThread(QThread):

    def __init__ (self, frame_update, resolution, source):
        super(CameraThread, self).__init__()

        self.frame_update = frame_update
        self.width = resolution[0]
        self.height = resolution[1]
        self.source = source

    def run(self):
        cap = cv2.VideoCapture(self.source)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        while True:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_qt_format.scaled(1280, 720, Qt.KeepAspectRatio)
                self.frame_update.emit(p)
