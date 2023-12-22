
import customtkinter
import tkinter

from Modules.Composants.WindowBtnChose import WindowBtnChose
from Modules.Composants.BarreInfosConnect import BarreInfoConnect
from Modules.Composants.NameApp import NameApp
class Header():

    def __init__(self, Parent):
        
        Menu =  customtkinter.CTkFrame(Parent, width=300,height=65, fg_color="#0E1C2A",corner_radius=10)
        Menu.grid_propagate(0)
        Menu.pack(side="top", fill='x', padx=10, pady=(5,5))    
        
        # titleApp = customtkinter.CTkLabel(Menu,text="FASTERSHARE",font=("bodoni mt",30,"bold"))
        # titleApp.pack(side="left", padx=10, pady=(7,5))

        self.Menu(Menu)
        
    def Menu(self,FrameMenu):
       # Create three subframes
       Frame1 = customtkinter.CTkFrame(FrameMenu,  height=45)
       Frame1.pack(side="left", fill='x', expand=True)

       Frame2 = customtkinter.CTkFrame(FrameMenu,  height=45)
       Frame2.pack(side="left", fill='x', expand=True)

       Frame3 = customtkinter.CTkFrame(FrameMenu, height=45,width=300)
       Frame3.pack(side="left", fill='x', expand=True)


       NameApp(Frame1,"fsoo").pack(fill='both', expand=True)
       BarreInfoConnect(Frame2,"dqtq").pack(fill='both', expand=True)
       WindowBtnChose(Frame3,"lkdsjfk").pack(fill='both', expand=True)

        