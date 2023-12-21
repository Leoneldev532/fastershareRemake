import customtkinter
import tkinter
from Modules.Composants.ComposantMenu import ComposantMenu
from Modules.Composants.ListDIrectory import ListDIrectory
from Modules.Composants.Infouser import Infouser
class Accueil():

    def __init__(self, Parent):
        
        HL = (25 * Parent._current_width) / 100
        Menu =  customtkinter.CTkFrame(Parent, width=HL, fg_color="#0E1C2A", border_width=2,border_color="#384149",corner_radius=10)
        Menu.grid_propagate(0)
        Menu.pack(side="left", fill='y', padx=10, pady=10)
        
        Modules =  customtkinter.CTkFrame(Parent, height=Parent._current_height,width=Parent._current_width,border_width=2,border_color="#252c32",fg_color="#252c32")
        Modules.pack(side="top", fill="x", padx=10, pady=10)
        Modules.grid_propagate(0)


        self.Menu(Menu)
        self.Contain(Modules,Modules._current_height)

    

    def Menu(self, FrameMenu):
        Menu1 = ComposantMenu(FrameMenu, "MENU TEST")
        Menu2 = ComposantMenu(FrameMenu, "HELLO")
        Infouserk = Infouser(FrameMenu,"192.258.25.25","dorval")

    def Contain(self,Contentplace,widthcontainer):
        ListDirectory = ListDIrectory(Contentplace,widthcontainer)