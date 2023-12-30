from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


class ComposantMenu(customtkinter.CTkFrame):

    Nom = ""

    def __init__(self, Parent, NomMenu):
        super().__init__(Parent)

        icon = customtkinter.CTkButton(self,text="🎅",fg_color="transparent",hover_color="#252c31",text_color="green",width=14,corner_radius=24,height=34,font=("bodoni mt",24))
        icon.pack(side="left",padx=(24,0),ipady=0) 

        txt = customtkinter.CTkButton(self,text=NomMenu,fg_color="transparent",hover_color="#252c31",width=Parent._current_width / 3,corner_radius=24,height=34,font=("bodoni mt",14))
        txt.pack(side="left",fill="x",ipadx=14,padx=14,ipady=0)    
        self.configure(Parent, height=40, width=250,fg_color="#252c31",corner_radius=24,)
        self.pack(side="top", fill="x",pady=(20, 5), padx=10,ipady=14)
        