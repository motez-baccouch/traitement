import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
from utils.transformations import egalisation,read,calculators
import matplotlib.pyplot as plt
import numpy as np



class Histogramme(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="histogramme",command=lambda:upload_file())
        self.home_frame_button_1.grid(row=0, column=0, padx=20, pady=10)
        

        ## first image and graph container
        

        # selected image
        self.display_image=customtkinter.CTkLabel(self, width=250, height=250, text="")
        self.display_image.grid(row=1,column=0, padx = 1, pady = 1)
      

   

        def upload_file():
            global img,img2,img3,img4
            f_types = [('Pgm Files', '*.pgm')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            image= Image.open(filename)
                
            #resize_image = images.set_max_height(image , maxHeight=250)
            img = ImageTk.PhotoImage(image)
            self.display_image.configure(image=img)

            self.originalText=tk.Label(self,text="Original PGM file")
            self.originalText.grid(row=2,column=0, padx = 1, pady = 1)
            
            
            res=read.read_pgm(image.filename)
            hist=calculators.histo(res)
            print(hist)
            histCumule=calculators.cumule(res)
            egalisation.egalisation(res,"result")
            image2=Image.open("result.pgm")
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
            self.display_image1=tk.Label(self,image=img2)
            self.display_image1.grid(row=4,column=0, padx = 1, pady = 1)
            self.resultText=tk.Label(self,text="resultat apres egalisation")
            self.resultText.grid(row=5,column=0, padx = 1, pady = 1)

            imageHisto=Image.open("histo.png")
            imageHistoCumule=Image.open("histoCumule.png")
            img3=ImageTk.PhotoImage(imageHisto)
            img4=ImageTk.PhotoImage(imageHistoCumule)
            self.display_imagehist=tk.Label(self,image=img3)
            self.display_imagehist.grid(row=3,column=0, padx = 1, pady = 1)
            self.display_imagecumule=tk.Label(self,image=img4)
            self.display_imagecumule.grid(row=6,column=0, padx = 1, pady = 1)

            ecart=calculators.ecartypeGris(res)
            moyenne=calculators.moyenneGris(res)
            print(ecart+ " hahaha " + moyenne)
