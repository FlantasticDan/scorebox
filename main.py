from tkinter import *
from tkinter import ttk
from threading import Thread
import time

from PIL import Image
from PIL import ImageTk

from camera_manager import list_camera_devices
from camera_manager import CameraManagaer

class GUI:
    def __init__(self):
        self.root = None
        self.input_index = None

        self.user_select_input_source()

        self.process_thread = None
        self.camera_manager = CameraManagaer(self.input_index)
        self.stream_img = None

        self.show_stream()

    def user_select_input_source(self):
        self.root = Tk()
        input_select_frame = Frame(self.root)
        input_select_frame.pack()

        input_combo = ttk.Combobox(input_select_frame, values=list_camera_devices(),
                                   state='readonly', width=30, justify='center')
        input_combo.set("Select Input")
        input_combo.pack(padx=5, pady=5)

        input_button = Button(input_select_frame, text="Confirm Input", relief=GROOVE, bd=3,
                              command=lambda:self.user_selected_input_source(input_combo.current()))
        input_button.pack(padx=5, pady=5)

        self.root.mainloop()

    def user_selected_input_source(self, index):
        if index >= 0:
            self.input_index = index
            self.root.destroy()

    def show_stream(self):
        self.root = Tk()

        stream_frame = Frame(self.root)
        stream_frame.pack()
        time.sleep(4)
        image = Image.fromarray(self.camera_manager.frame)
        image = ImageTk.PhotoImage(image)
        self.stream_img = Label(stream_frame, image=image)
        self.stream_img.image = image
        self.stream_img.pack()

        self.start_process_thread()

        self.root.mainloop()

    def process_frame(self):
        while True:
            if self.camera_manager.frame is not None:
                image = Image.fromarray(self.camera_manager.frame)
                image = ImageTk.PhotoImage(image)
                self.stream_img.configure(image=image)
                self.stream_img.image = image

    def start_process_thread(self):
        self.process_thread = Thread(target=self.process_frame)
        self.process_thread.start()


GUI()
