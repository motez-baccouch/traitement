import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from PIL import ImageTk
from utils.functions import images
from utils.transformations import read,segment,write
import subprocess
import os
import sys
from utils.functions.openFolder import openFolder

class Segmentation(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.title= customtkinter.CTkLabel(self,  text="Segmentation",font=customtkinter.CTkFont( family = "Montserrat", size = 40))
        self.title.grid(row=0, column=0)

        self.upload_button = customtkinter.CTkButton(self, text="Upload", command=lambda:upload_file())
        self.upload_button.grid(row=3, column=0, pady=10)

        self.input_image = customtkinter.CTkLabel(self, width=250, height= 250,text="")
        self.input_image.grid(row=4, column=0)

        #transformation options
        self.transformation_options = customtkinter.CTkFrame(self)
        self.transformation_options.grid_columnconfigure(3, weight=1)
        self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        #transformation method
        self.method_selector = customtkinter.CTkOptionMenu(self.transformation_options, values=["default","ET","OU"], command=lambda value:onMethodChange(value))
        self.method_selector.set("default")
        self.method_selector.grid(row= 1, column=1, padx=20, pady=10)

        # transformation sliders
        self.sliders_container = customtkinter.CTkFrame(self.transformation_options)
        self.sliders_container.grid(row= 1, column=2, padx=20, pady=10)
        self.slider = customtkinter.CTkSlider(self.sliders_container, from_=0, to=255)
        self.slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider.grid(row=0, column=0, pady=5)
        self.slider1 = customtkinter.CTkSlider(self.sliders_container, from_=0, to=255)
        self.slider1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider1.grid(row=1, column=0, pady=5)
        self.slider2 = customtkinter.CTkSlider(self.sliders_container, from_=0, to=255)
        self.slider2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.slider2.grid(row=2, column=0, pady=5)


        # transformation_button
        self.transform_button = customtkinter.CTkButton(self.transformation_options, text="Transform",command=lambda:transform_file())
        self.transform_button.grid(row= 1, column=3, padx=20, pady=10)

        # open image folde
        self.open_button= customtkinter.CTkButton(self,text="Open Image Folder", command=lambda:openImage() )
        # self.open_button.grid(row=7, column=0, pady=10)

        def upload_file():
            global img
            global filename
            f_types = [('Colored files','*.ppm')]
            filename= filedialog.askopenfilename(filetypes=f_types)
   
            image= Image.open(filename)

            resize_image = images.set_max_height(image , maxHeight=250)
            img = ImageTk.PhotoImage(resize_image)
            
            # display image
            self.input_image.configure(image=img)

            self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        def transform_file():
            global resultImg

            imgInfo=read.ppmread(filename)

            method = self.method_selector.get()

            if method=="default": 
                seuil=[
                    self.slider.get(),
                    self.slider1.get(),
                    self.slider2.get()
                ]
                result=segment.segementParDefaut(imgInfo,seuil=seuil)
            else:
                result=segment.segement(imgInfo,seuil=self.slider.get(),method=method)
            write.ppmwrite(result, "out/segment")

            image= Image.open("out/segment.ppm")
            resize_image = images.set_max_height(image , maxHeight=250)
            resultImg = ImageTk.PhotoImage(resize_image)

            # display image
            self.result_image = tk.Label(self,image=resultImg, width=250, height= 250)
            self.result_image.grid(row=7, column=0)

            self.open_button.grid(row=8, column=0, pady=10)

        def onMethodChange(value):
            method = value
            if method=="default": 
                self.slider1.grid(row=1, column=0, pady=5)
                self.slider2.grid(row=2, column=0, pady=5)
            else: 
                self.slider1.grid_forget()
                self.slider2.grid_forget()

        def openImage():
            openFolder(os.path.join(os.getcwd(),"out"))


