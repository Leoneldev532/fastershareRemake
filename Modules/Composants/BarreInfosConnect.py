import customtkinter
from customtkinter.windows.widgets import CTkFrame, CTkLabel

class BarreInfoConnect(customtkinter.CTkFrame):

    Nom = ""

    def __init__(self, Parent,data):
        super().__init__(Parent)
            
        self.configure(Parent, height=40, width=450,fg_color="red",corner_radius=24 )
        self.pack(side="right", fill="x",padx=8)
        