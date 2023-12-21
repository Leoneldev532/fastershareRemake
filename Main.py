import customtkinter
import tkinter
from Modules.Accueil import Accueil
import threading

Fenetre = customtkinter.CTk(fg_color="#131f2a")
Fenetre.title('FasterShare')
            
Largeur = Fenetre.winfo_screenwidth()
Hauteur = Fenetre.winfo_screenheight()

# Largeur = 650
# Hauteur = 400


# Fenetre.geometry("%dx%d" % (Largeur, Hauteur))

# # Fenetre.iconbitmap("Image/logo.ico")

# Logo =  customtkinter.CTkFrame(Fenetre, width=Largeur, corner_radius=0, fg_color="#0E1C2A")
# Logo.pack(side="top", fill='y')


# Chargement =  customtkinter.CTkFrame(Fenetre, height=50, corner_radius=0, fg_color="#0E1C2A")
# Chargement.pack(side="bottom", fill="x", ipady=5)

# NomApp = customtkinter.CTkLabel(Chargement, text="FASTERSHARE", text_color="white", font=("bodoni mt",18,"bold"))
# NomApp.pack(side="right", padx=10)



# Accueil
Accueil(Fenetre)

Fenetre.mainloop()