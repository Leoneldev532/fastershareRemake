from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


class Infouser(customtkinter.CTkFrame):

    ipadress = ""
    nom = ""

    def __init__(self, Parent,nom,ipadress):
        super().__init__(Parent)
         

    
        
        nom = customtkinter.CTkLabel(self,text=nom,font=("bodoni mt",30,"bold"))
        ipadress = customtkinter.CTkLabel(self,text=ipadress,font=("bodoni mt",30,"bold"))

        nom.grid(row=1,column=1)
        ipadress.grid(row=2,column=1)

        self.grid_propagate(0)
        self.configure(Parent, height=100, width=250 ,border_width=0,corner_radius=24 )
        self.pack(side="bottom", pady=(14, 5), padx=2)
        