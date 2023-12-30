
import customtkinter
import tkinter

from Modules.Composants.WindowBtnChose import WindowBtnChose
from Modules.Composants.BarreInfosConnect import BarreInfoConnect
from Modules.Composants.NameApp import NameApp
class Header():

    def __init__(self, Parent):
        
        Menu =  customtkinter.CTkFrame(Parent, width=300,height=65, fg_color="transparent",corner_radius=10)
        Menu.grid_propagate(0)
        Menu.pack(side="top", fill='x', padx=10, pady=(14,5))    
        
        

        self.Menu(Menu)
        
    def Menu(self,FrameMenu):
       # Create three subframes
       Frame1 = customtkinter.CTkFrame(FrameMenu,fg_color='transparent' ,height=45)
       Frame1.pack(side="left", fill='x', expand=True)

       Frame2 = customtkinter.CTkFrame(FrameMenu,fg_color='transparent', height=45)
       Frame2.pack(side="left", fill='x', expand=True,)

       Frame3 = customtkinter.CTkFrame(FrameMenu,fg_color='transparent',height=45,width=300)
       Frame3.pack(side="left", fill='x', expand=True)


       NameApp(Frame1,"*FASTERSHARE").pack(fill='both', expand=True)
       BarreInfoConnect(Frame2,"1/2","● connecté","signal").pack(fill='both', expand=True)
       WindowBtnChose(Frame3,"lkdsjfk").pack(fill='both',side="right")

        