from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


class ListDIrectory(customtkinter.CTkFrame):
   Nom = ""

   def __init__(self, Parent, widthcontainer):
    super().__init__(Parent, widthcontainer)

    ligneOne = customtkinter.CTkFrame(self, height=40, corner_radius=10, bg_color="white", fg_color="black")
    ligneOne.pack(side="top", pady=(0,14), fill="x", padx=10)
    
    ligneThree = customtkinter.CTkFrame(self, height=70, corner_radius=10)
    ligneThree.pack(side="top", pady=(0,14), fill="x", padx=10)  

    ligneTwo = customtkinter.CTkFrame(self, height=220, corner_radius=10, bg_color="white", fg_color="black")
    ligneTwo.pack(side="bottom", pady=(0,14), fill="x", padx=10)

    ligneFour= customtkinter.CTkFrame(self, height=190, corner_radius=10)
    ligneFour.pack(side="top", pady=(0,14), fill="x", padx=10)  

    ethernet = customtkinter.CTkButton(ligneThree,height=50,text="Ethernet",corner_radius=30)
    ethernet.pack(side="left", padx=10, pady=10)
    
    pointacces = customtkinter.CTkButton(ligneThree,height=50,text="point d'acces",corner_radius=30)
    pointacces.pack(side="left",pady=10)

    scrollbarContainer = customtkinter.CTkScrollableFrame(ligneTwo,orientation="horizontal")
    scrollbarContainer.pack(side="bottom", fill="x", padx=10, pady=10)

    label_gauche = customtkinter.CTkLabel(ligneOne, text="Label gauche")
    label_gauche.pack(side="left", padx=10, pady=10)

    label_droit = customtkinter.CTkLabel(ligneOne, text="Label droit")
    label_droit.pack(side="right", padx=10, pady=10)

    self.configure(Parent, height=300, width=1200, fg_color="#252c31", corner_radius=14 )
    self.pack(side="top", pady=(10, 5), padx=4, fill="x")
    self.grid_propagate(0)