import customtkinter
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter as tk
import os
from utils.functions import images


class Home(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        image_path = os.path.join(os.getcwd(), "test_images")

        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))

        self.grid_columnconfigure(0, weight=1)

        self.large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image)
        self.large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self, text="", image=self.image_icon_image,command=lambda:upload_file())
        self.home_frame_button_1.grid(row=10, column=0, padx=20, pady=10)

        #upload image 
        def upload_file():
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            image= Image.open(filename)

            info_dict = {
                "Filename": image.filename,
                "Image Size": image.size,
                "Image Height": image.height,
                "Image Width": image.width,
                "Image Format": image.format,
                "Image Mode": image.mode,
                "Image is Animated": getattr(image, "is_animated", False),
                "Frames in Image": getattr(image, "n_frames", 1)
                        }

            for label,value in info_dict.items():
                 print(f"{label:25}: {value}")
            
            resize_image = images.set_max_height(image , maxHeight=250)
            
            img = ImageTk.PhotoImage(resize_image)
            self.display_image=tk.Label(self,image=img, width=250, height= 250)
            self.display_image.grid(row=1,column=0)
            #image details
            self.display_filename=tk.Label(self,text="Filename: "+image.filename)
            self.display_filename.grid(row=2,column=0)
            self.display_filesize=tk.Label(self,text="Image Size: "+ str(image.size))
            self.display_filesize.grid(row=3,column=0)
            self.display_fileheight=tk.Label(self,text="Image Height:"+ str(image.height))
            self.display_fileheight.grid(row=4,column=0)
            self.display_filewidth=tk.Label(self,text="Image Width: "+ str(image.width,))
            self.display_filewidth.grid(row=5,column=0)
            self.display_fileformat=tk.Label(self,text="Image Format: "+ str(image.format,))
            self.display_fileformat.grid(row=6,column=0)
            self.display_filemode=tk.Label(self,text="Image Mode: "+ str(image.mode,))
            self.display_filemode.grid(row=7,column=0)
            self.display_fileanimated=tk.Label(self,text="Image is Animated: "+ str(getattr(image, "is_animated", False)))
            self.display_fileanimated.grid(row=8,column=0)
            self.display_filefps=tk.Label(self,text="Frames in Image: "+ str(getattr(image, "n_frames", 1)))
            self.display_filefps.grid(row=9,column=0)
            
