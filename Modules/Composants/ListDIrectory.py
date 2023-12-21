from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


class ListDIrectory(customtkinter.CTkFrame):

    Nom = ""

    def __init__(self, Parent,widthcontainer):
        super().__init__(Parent,widthcontainer)
         


        self.configure(Parent, height=300,width=widthcontainer, fg_color="red",corner_radius=24 )
        self.pack(side="top", pady=(20, 5), padx=10)
        