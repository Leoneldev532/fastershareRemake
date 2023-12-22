import customtkinter
import tkinter
from Modules.Accueil import Accueil
from Modules.Header import Header
import threading

Fenetre = customtkinter.CTk(fg_color="#131f2a")
Fenetre.title('FasterShare')
# Fenetre.overrideredirect(True)
Largeur = Fenetre.winfo_screenwidth()
Hauteur = Fenetre.winfo_screenheight()
Fenetre.minsize(1000, 200)

x = 0
y = 0

def clickwin(event):
    global x, y
    x = event.x
    y = event.y
 
def dragwin(event):
    global x, y
    new_x = Fenetre.winfo_x() - x + event.x
    new_y = Fenetre.winfo_y() - y + event.y
    Fenetre.geometry("+%s+%s" % (new_x, new_y))

Fenetre.bind("<Button-1>", clickwin)
Fenetre.bind("<B1-Motion>", dragwin)

Header(Fenetre)
Accueil(Fenetre)

Fenetre.mainloop()