from threading import Thread
from typing import List

import cv2
from pygrabber.dshow_graph import FilterGraph

def list_camera_devices() -> List:
    return FilterGraph().get_input_devices()

class CameraManagaer:
    def __init__(self, source_id):
        self.source_id = source_id

        self.capture_width = 1280
        self.capture_height = 720

        self.frame = None
        self.thread = None

        self.capture = cv2.VideoCapture(self.source_id)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.capture_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capture_height)

        self.start_capture()

    def change_resolution(self, width, height):
        self.capture_width = width
        self.capture_height = height

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.capture_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capture_height)

    def grab_frame_from_buffer(self):
        while True:
            ret, frame = self.capture.read()
            if ret:
                self.frame = frame

    def start_capture(self):
        self.thread = Thread(target=self.grab_frame_from_buffer, daemon=True)
        self.thread.start()
