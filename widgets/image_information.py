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

        self.configure(bg="blue")