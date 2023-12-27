import customtkinter
from customtkinter.windows.widgets import CTkFrame, CTkLabel

class WindowBtnChose(customtkinter.CTkFrame):

    Nom = ""

    def __init__(self, Parent,vql):
        super().__init__(Parent)
            
        self.configure(Parent, height=40, width=200,fg_color="transparent",corner_radius=24 )
        self.pack(side="right",padx=10)
        self.grid_propagate(0)

        closeBtn = customtkinter.CTkButton(self,text="X",width=50,corner_radius=54,height=20,font=("colonna mt",30,"bold"),fg_color="#383E49")
        closeBtn.pack(side="right",ipadx=4,padx=4)

        AugmenterWindowBtn = customtkinter.CTkButton(self,text="□",corner_radius=54,height=20,width=50,font=("bodoni mt",30,"bold"),fg_color="#383E49")
        AugmenterWindowBtn.pack(side="left",ipadx=4,padx=4)

        diminuerbtn = customtkinter.CTkButton(self,text="-",width=50,corner_radius=54,height=20,font=("bodoni mt",30,"bold"),fg_color="#383E49")
        diminuerbtn.pack(side="left",ipadx=4,padx=4)