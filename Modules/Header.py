


        

import customtkinter
import tkinter

from Modules.Composants.WindowBtnChose import WindowBtnChose
from Modules.Composants.BarreInfosConnect import BarreInfoConnect
class Header():

    def __init__(self, Parent):
        
        Menu =  customtkinter.CTkFrame(Parent, width=300,height=45, fg_color="#0E1C2A",corner_radius=10)
        Menu.grid_propagate(0)
        Menu.pack(side="top", fill='x', padx=10, pady=(5,5))    
        
        # titleApp = customtkinter.CTkLabel(Menu,text="FASTERSHARE",font=("bodoni mt",30,"bold"))
        # titleApp.pack(side="left", padx=10, pady=(7,5))

        self.Menu(Menu)

    

    def Menu(self,FrameMenu):
       BarreInfoConnect(FrameMenu,"dqtq")
       WindowBtnChose(FrameMenu,"lkdsjfk")

        