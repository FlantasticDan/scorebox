from tkinter import *
from tkinter import ttk
from threading import Thread
import time

from PIL import Image
from PIL import ImageTk

from camera_manager import list_camera_devices
from camera_manager import CameraManager
from scoreboard_manager import ScoreboardManager

class GUI:
    def __init__(self):
        self.root = None
        self.input_index = None

        self.scoreboard: ScoreboardManager = None

        self.user_select_input_source()

        self.process_thread = None
        self.processing = True
        self.camera_manager = CameraManager(self.input_index)
        self.stream_img = None

        self.process_target = self.camera_manager

        self.show_stream()
        # self.process_thread.join()
        # self.root.destroy()
        self.show_scoreboard()

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

        selection_frame = Frame(self.root)
        selection_frame.pack()

        self.corner_pin = list()
        instructions = Label(selection_frame, text="Click the scoreboard's corners in a clockwise order starting with the top left.")
        instructions.pack()

        self.stream_frame = Frame(self.root)
        self.stream_frame.pack()

        self.prepare_process_thread(self.stream_frame)

        self.stream_img.bind('<Button 1>', self.update_corner_pin)

        self.root.mainloop()

    def process_frame(self):
        while self.processing:
            if self.process_target.frame is not None:
                image = Image.fromarray(self.process_target.frame)
                image = ImageTk.PhotoImage(image)
                self.stream_img.configure(image=image)
                self.stream_img.image = image
        print("Process Thread Exited")

    def start_process_thread(self):
        self.process_thread = Thread(target=self.process_frame, daemon=False)
        self.process_thread.start()
        print('Process Thread Started')

    def prepare_process_thread(self, parent):
        while self.process_target.frame is None:
            time.sleep(0.1)
        image = Image.fromarray(self.process_target.frame)
        image = ImageTk.PhotoImage(image)
        self.stream_img = Label(parent, image=image)
        self.stream_img.image = image
        self.stream_img.pack()
        self.start_process_thread()

    def update_corner_pin(self, event):
        self.corner_pin.append((event.x, event.y))
        if len(self.corner_pin) == 4:
            print(f'Scoreboard Corners: {self.corner_pin}')
            self.scoreboard = ScoreboardManager(self.camera_manager, self.corner_pin)
            self.process_target = self.scoreboard

    def show_scoreboard(self):
        print("Showing Scoreboard")
        self.root = Tk()

        scoreboard_frame = Frame(self.root)
        scoreboard_frame.pack()

        self.corner_pin = list()
        instructions = Label(scoreboard_frame, text="Scoreboard View")
        instructions.pack()

        self.stream_frame = Frame(self.root)
        self.stream_frame.pack()

        # self.process_thread.join()
        self.process_target = self.scoreboard
        # self.processing = True
        # self.prepare_process_thread(self.stream_frame)

        self.root.mainloop()


GUI()
