import customtkinter
from customtkinter.windows.widgets import CTkFrame, CTkLabel

class WindowBtnChose(customtkinter.CTkFrame):

    Nom = ""

    def __init__(self, Parent,vql):
        super().__init__(Parent)
            
        self.configure(Parent, height=50, width=70,fg_color="blue",corner_radius=24 )
        self.pack(side="right",padx=10)
        