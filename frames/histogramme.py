import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk



class Histogramme(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="histogramme",command=lambda:upload_file())
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)

        def upload_file():
            print("test")
