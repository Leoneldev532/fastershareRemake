from typing import Optional, Tuple, Union
import customtkinter

class NameApp(customtkinter.CTkFrame):


    def __init__(self, Parent,data):
        super().__init__(Parent)
            
        self.configure(Parent, height=40, width=370,fg_color="transparent" )
        self.pack(side="right")

        titleApp = customtkinter.CTkLabel(self,text=data,font=("colonna mt",30,"bold"))
        titleApp.pack(side="left", padx=10, pady=(7,5))

        