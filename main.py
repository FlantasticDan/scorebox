from tkinter import *
from tkinter import ttk

from camera_manager import list_camera_devices
from camera_manager import CameraManagaer

class GUI:
    def __init__(self):
        self.root = None
        self.input_index = None

        self.user_select_input_source()
        print(self.input_index)

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

GUI()
