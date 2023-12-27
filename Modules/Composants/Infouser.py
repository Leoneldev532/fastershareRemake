import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class Infouser(customtkinter.CTkFrame):
   ipadress = ""
   nom = ""

   def __init__(self, Parent,nom,ipadress):
       super().__init__(Parent)
       self.grid_propagate(0)
       nom = customtkinter.CTkLabel(self,text=nom,fg_color='transparent',font=("bodoni mt",30,"bold"))
       ipadress = customtkinter.CTkLabel(self,text=ipadress,fg_color='transparent',font=("bodoni mt",30,"bold"))
    #    nom.pack(side="right") 

       self.configure(height=100, width=250,corner_radius=14)
       self.pack(side="bottom", padx=2,pady=14)