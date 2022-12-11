import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from PIL import ImageTk
from utils.functions import images
from utils.transformations import read,write,lutte,filtre_mediane,filtre_moyenne
import subprocess
import os
import sys
from utils.functions.openFolder import openFolder
import math

class Filtres(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="segmentation",command=lambda:upload_file())
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.upload_button = customtkinter.CTkButton(self, text="Upload", command=lambda:upload_file())
        self.upload_button.grid(row=3, column=0)

        #transformation options
        self.transformation_options = customtkinter.CTkFrame(self)
        self.transformation_options.grid_columnconfigure(3, weight=1)
        # self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        #transformation method
        self.method_selector = customtkinter.CTkOptionMenu(self.transformation_options, values=["LUT","filtre mediane","filtre moyenne"], command=lambda value:onMethodChange(value))
        self.method_selector.set("LUT")
        self.method_selector.grid(row= 1, column=1, padx=20, pady=10)

        # transformation sliders
        self.sliders_container = customtkinter.CTkFrame(self.transformation_options)
        self.sliders_container.grid(row= 1, column=2, padx=20, pady=10)
        self.slider = customtkinter.CTkSlider(self.sliders_container, from_=0, to=12,number_of_steps=12)
        self.slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider.grid(row=0, column=0, pady=5)
        self.slider1 = customtkinter.CTkSlider(self.sliders_container, from_=0, to=12,number_of_steps=12)
        self.slider1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider1.grid(row=1, column=0, pady=5)
        self.slider2 = customtkinter.CTkSlider(self.sliders_container, from_=0, to=12,number_of_steps=12)
        self.slider2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider2.grid(row=2, column=0, pady=5)
        self.slider3 = customtkinter.CTkSlider(self.sliders_container, from_=0, to=12,number_of_steps=12)
        self.slider3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider3.grid(row=3, column=0, pady=5)
        


        # transformation_button
        self.transform_button = customtkinter.CTkButton(self.transformation_options, text="Transform",command=lambda:transform_file())
        self.transform_button.grid(row= 1, column=3, padx=20, pady=10)

        # open image folde
        self.open_button= customtkinter.CTkButton(self,text="Open Image Folder", command=lambda:openImage() )
        # self.open_button.grid(row=7, column=0, pady=10)

        def upload_file():
            global img
            global filename
            f_types = [('black and white images','*.pgm')]
            filename= filedialog.askopenfilename(filetypes=f_types)
   
            image= Image.open(filename)

            resize_image = images.set_max_height(image , maxHeight=250)
            img = ImageTk.PhotoImage(resize_image)
            
            # display image
            self.input_image = tk.Label(self,image=img, width=250, height= 250)
            self.input_image.grid(row=4, column=0)

            self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        def transform_file():
            global resultImg

            imgInfo=read.read_pgm(filename)

            method = self.method_selector.get()

            if method=="LUT": 
                lutte.lutte({"x":math.floor(self.slider.get()),"y":math.floor(self.slider1.get())},{"x":math.floor(self.slider2.get()),"y":math.floor(self.slider3.get())},"out/result",imgInfo)
            elif method=="filtre mediane":
                filtre_mediane.pgm_filtre_mediane(imgInfo,"out/result",filterSize=self.slider.get())
            else:
                filtre_moyenne.pgm_filtre_moyenne(imgInfo,"out/result",filterSize=self.slider.get())
                
                
           

            image= Image.open("out/result.pgm")
            resize_image = images.set_max_height(image , maxHeight=250)
            resultImg = ImageTk.PhotoImage(resize_image)

            # display image
            self.result_image = tk.Label(self,image=resultImg, width=250, height= 250)
            self.result_image.grid(row=7, column=0)

            self.open_button.grid(row=8, column=0, pady=10)

        def onMethodChange(value):
            method = value
            if method=="LUT": 
                self.slider1.grid(row=1, column=0, pady=5)
                self.slider2.grid(row=2, column=0, pady=5)
                self.slider3.grid(row=3, column=0, pady=5)
            else: 
                self.slider1.grid_forget()
                self.slider2.grid_forget()
                self.slider3.grid_forget()

        def openImage():
            openFolder(os.path.join(os.getcwd(),"out"))


