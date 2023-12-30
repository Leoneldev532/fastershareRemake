from typing import Optional, Tuple, Union
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
from Modules.Composants.fileCard import fileCard

class ListDIrectory(customtkinter.CTkFrame):
   Nom = ""

   def __init__(self, Parent, widthcontainer,data:{}):
    super().__init__(Parent, widthcontainer)

    ligneOne = customtkinter.CTkFrame(self, height=40, corner_radius=10, bg_color="white", fg_color="transparent")
    ligneOne.pack(side="top", pady=(0,14), fill="x", padx=10)
     

    ligneTwo = customtkinter.CTkFrame(self, height=220, corner_radius=10, bg_color="white", fg_color="#252c32")
    ligneTwo.pack(side="top", pady=(0,14), fill="x")
    
    ligneThree = customtkinter.CTkFrame(self, height=70, corner_radius=10,fg_color="transparent")
    ligneThree.pack(side="top", pady=(0,14), fill="x", padx=10) 

    ligneFour= customtkinter.CTkFrame(self, height=190, corner_radius=10)
    ligneFour.pack(side="top", pady=(0,14), fill="x", padx=10)  

    ethernet = customtkinter.CTkButton(ligneThree,height=50,text="Ethernet",font=("bodoni mt",20),hover_color="#4da456",border_width=2,border_color="#1d862b",fg_color="#2e3235",corner_radius=30)
    ethernet.pack(side="left", padx=10, pady=10)
    
    pointacces = customtkinter.CTkButton(ligneThree,height=50,text="point d'acces",font=("bodoni mt",20),hover_color="#4da456",border_width=2,border_color="#1d862b",fg_color="#2e3235",corner_radius=30)
    pointacces.pack(side="left",pady=10)

    scrollbarContainer = customtkinter.CTkScrollableFrame(ligneTwo, orientation="horizontal", fg_color="#252c32")
    scrollbarContainer.grid(row=0, column=0,sticky="nsew")

    scrollbarContainer2 = customtkinter.CTkScrollableFrame(ligneFour, orientation="horizontal", fg_color="#252c32")
    scrollbarContainer2.grid(row=0, column=0,sticky="nsew")

    ligneTwo.grid_columnconfigure(0, weight=1)
    ligneFour.grid_columnconfigure(0, weight=1)

    for i, card in enumerate(data): 
      print(data)
      scrollbarContainer.grid_columnconfigure(i, minsize=244)
      fileCard(scrollbarContainer, *card).grid(row=0, column=i,padx=6,pady=10, sticky="nsew")

      
    scrollbarContainer.grid_columnconfigure(i, weight=1)
    scrollbarContainer.grid_rowconfigure(0, weight=1)


    for i, card in enumerate(data): 
      print(data)
      scrollbarContainer2.grid_columnconfigure(i, minsize=244)
      fileCard(scrollbarContainer2, *card).grid(row=0, column=i,padx=6,pady=10, sticky="nsew")
    scrollbarContainer2.grid_columnconfigure(i, weight=1)
    scrollbarContainer2.grid_rowconfigure(0, weight=1)

      

    label_gauche = customtkinter.CTkLabel(ligneOne,text_color="white",text="Dossier courant",font=("bodoni mt",24))
    label_gauche.pack(side="left",padx=10, pady=10)

    label_droit = customtkinter.CTkLabel(ligneOne, text="44" ,text_color="#18de27",font=("bodoni mt",24))
    label_droit.pack(side="right", padx=10, pady=10)

    self.configure(Parent, height=300, width=1200, fg_color="#252c31", corner_radius=14 )
    self.pack(side="top", pady=(10, 5), padx=4, fill="both")
    self.grid_propagate(0)