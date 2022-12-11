import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from PIL import ImageTk
from utils.functions import images
from utils.transformations import read,write,erosion
import subprocess
import os
import sys
from utils.functions.openFolder import openFolder
import cv2

class Erosion(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.title= customtkinter.CTkLabel(self,  text="Filtres",font=customtkinter.CTkFont( family = "Montserrat", size = 40))
        self.title.grid(row=0, column=0)

        self.upload_button = customtkinter.CTkButton(self, text="Upload", command=lambda:upload_file())
        self.upload_button.grid(row=3, column=0)

        self.input_image = customtkinter.CTkLabel(self, width=250, height= 250,text="")
        self.input_image.grid(row=4, column=0)

        #transformation options
        self.transformation_options = customtkinter.CTkFrame(self)
        self.transformation_options.grid_columnconfigure(3, weight=1)
        self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        #transformation method
        self.method_selector = customtkinter.CTkOptionMenu(self.transformation_options, values=["EROSION","DILATATION","OUVERTURE","FERMETURE"], command=lambda value:onMethodChange(value))
        self.method_selector.set("EROSION")
        self.method_selector.grid(row= 1, column=1, padx=20, pady=10)

     
        


        # transformation_button
        self.transform_button = customtkinter.CTkButton(self.transformation_options, text="Transform",command=lambda:transform_file())
        self.transform_button.grid(row= 1, column=3, padx=20, pady=10)

        # open image folde
        self.open_button= customtkinter.CTkButton(self,text="Open Image Folder", command=lambda:openImage() )
        # self.open_button.grid(row=7, column=0, pady=10)

        def upload_file():
            global img
            global filename
            f_types = [('colored images','*.ppm')]
            filename= filedialog.askopenfilename(filetypes=f_types)
   
            image= Image.open(filename)

            resize_image = images.set_max_height(image , maxHeight=250)
            img = ImageTk.PhotoImage(resize_image)
            
            # display image
            self.input_image.configure(image=img)

            self.transformation_options.grid(row=5, column=0, padx=20, pady=10)


        def transform_file():
            global resultImg
            method = self.method_selector.get()
            print(method)
            image= cv2.imread(filename)
            resultImg=erosion.morph(image,method)
            cv2.imwrite("result.ppm", resultImg)
                
            image= Image.open("result.ppm")
            resize_image = images.set_max_height(image , maxHeight=250)
            resultImg = ImageTk.PhotoImage(resize_image)
            
            # display image
            self.result_image = tk.Label(self,image=resultImg, width=250, height= 250)
            self.result_image.grid(row=7, column=0)

            self.open_button.grid(row=8, column=0, pady=10)

        def onMethodChange(value):
            method = value
          

        def openImage():
            openFolder(os.path.join(os.getcwd(),"out"))


