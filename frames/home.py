import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
import os

class Home(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")

        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))


        self.grid_columnconfigure(0, weight=1)

        self.large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image)
        self.large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="", image=self.image_icon_image,command=lambda:upload_file())
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)

        #upload image 
        def upload_file():
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            img.height=500
            img.width=500
            self.home_frame_image=tk.Label(self.home_frame,image=img)
            self.home_frame_image.grid(row=1,column=0)