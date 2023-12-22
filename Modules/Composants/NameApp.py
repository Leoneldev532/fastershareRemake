from typing import Optional, Tuple, Union
import customtkinter

class NameApp(customtkinter.CTkFrame):


    def __init__(self, Parent,data):
        super().__init__(Parent)
            
        self.configure(Parent, height=40, width=370,fg_color="blue",corner_radius=24 )
        self.pack(side="right")
        