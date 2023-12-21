import customtkinter
from customtkinter.windows.widgets import CTkFrame, CTkLabel

class BarreInfoConnect(customtkinter.CTkFrame):
   def __init__(self, Parent):
       super().__init__(Parent)

       ligneOne = customtkinter.CTkFrame(self, height=40, corner_radius=10, bg_color="white", fg_color="black")
       ligneOne.pack(side="top", pady=(0,14), fill="x", padx=10)

       nbreconnect = customtkinter.CTkLabel(ligneOne, text="Nombre de connexion : 10", font=("Roboto", 12), fg_color="black", bg_color="white")
       nbreconnect.pack(side="left", padx=(10,0))
