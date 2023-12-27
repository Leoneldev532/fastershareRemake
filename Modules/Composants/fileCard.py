import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class fileCard(customtkinter.CTkFrame):
 def __init__(self, Parent, nomicone, nomdirectory):
     super().__init__(Parent)
     self.configure(border_width=2,width=144,border_color="red", corner_radius=14)
     nomi = customtkinter.CTkLabel(self, text=nomicone, width=44, fg_color="transparent",bg_color='transparent', font=("bodoni mt",24,"bold"))
     nomdi = customtkinter.CTkLabel(self, text=nomdirectory, width=44,fg_color="transparent", bg_color='transparent', font=("bodoni mt",20,"bold"))
     nomi.pack(side="top",pady=44)              
     nomdi.pack(side="top") 
    #  self.pack(side="left", fill="y", padx=2, pady=14)
