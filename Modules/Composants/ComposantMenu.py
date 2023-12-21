from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


class ComposantMenu(customtkinter.CTkButton):

    Nom = ""

    def __init__(self, Parent, NomMenu):
        super().__init__(Parent)
            
        self.configure(Parent, height=50, width=250, text=NomMenu, fg_color="#383E49",font=("bodoni mt",18,"bold") ,corner_radius=24 )
        self.pack(side="top", pady=(20, 5), padx=10)
        