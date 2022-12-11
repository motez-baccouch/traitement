import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from utils.transformations import egalisation,read,calculators
import matplotlib.pyplot as plt
import numpy as np
from utils.functions import images


class Histogramme(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        
        self.title= customtkinter.CTkLabel(self,  text="Histogramme",font=customtkinter.CTkFont( family = "Montserrat", size = 40))
        self.title.grid(row=0, column=0)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="Upload",command=lambda:upload_file())
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        

        ## first image and graph container
        self.input_container = customtkinter.CTkFrame(self)
        self.input_container.grid(row=2, column=0, padx = 1, pady = 1)
        self.input_container.grid_columnconfigure(1, weight=2)

        # selected image
        self.display_image=customtkinter.CTkLabel(self.input_container, width=250, height=250, text="")
        self.display_image.grid(row=0,column=0, padx = 1, pady = 1)
      
        #histogramme of input image
        self.display_image_histo=customtkinter.CTkLabel(self.input_container,text="",width=250, height=250)
        self.display_image_histo.grid(row=0,column=1, padx = 1, pady = 1)

        self.resultText=tk.Label(self,text="resultat apres egalisation")
        self.resultText.grid(row=3,column=0, padx = 1, pady = 1)

        ## second image and graph container
        self.output_container = customtkinter.CTkFrame(self)
        self.output_container.grid(row=4, column=0, padx = 1, pady = 1)
        self.output_container.grid_columnconfigure(1, weight=2)

        # output image
        self.output_image=customtkinter.CTkLabel(self.output_container, width=250, height=250, text="")
        self.output_image.grid(row=0,column=0, padx = 1, pady = 1)

        # ouptut histogramme
        self.output_histo=customtkinter.CTkLabel(self.output_container,text="",width=250, height=250)
        self.output_histo.grid(row=0,column=1, padx = 1, pady = 1)

        def upload_file():
            global img,img2,img3,img4
            f_types = [('Pgm Files', '*.pgm')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            image= Image.open(filename)
            
            
            resize_image = images.set_max_height(image , maxHeight=250)
            img = ImageTk.PhotoImage(resize_image)
            self.display_image.configure(image=img)
            
            
            res=read.read_pgm(image.filename)
            hist=calculators.histo(res)
            print(hist)
            histCumule=calculators.cumule(res)
            egalisation.egalisation(res,"result")
            image2=Image.open("result.pgm")
            image2 = images.set_max_height(image2, maxHeight=250)
            plt.title('histograme')
            plt.xlabel('niveaux de gris')
            plt.ylabel('occurence')
            plt.plot(np.arange(0, 256, 1),np.int_(hist))
            plt.savefig("histo.png")
            plt.clf()
            plt.cla()
            plt.close()
            plt.title('histograme cumulé')
            plt.plot(np.arange(0, 256, 1),np.int_(histCumule))
            plt.savefig("histoCumule.png")
            img2 = ImageTk.PhotoImage(image2)

            self.output_image.configure(image= img2)

            

            imageHisto=Image.open("histo.png")
            imageHisto= images.set_max_height(imageHisto, maxHeight=250)
            imageHistoCumule=Image.open("histoCumule.png")
            imageHistoCumule= images.set_max_height(imageHistoCumule, maxHeight=250)
            img3=ImageTk.PhotoImage(imageHisto)
            img4=ImageTk.PhotoImage(imageHistoCumule)
            self.display_image_histo.configure(image= img3)
            self.output_histo.configure(image= img4)
