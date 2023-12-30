import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class Infouser(customtkinter.CTkFrame):
 

   def __init__(self, Parent,nom,ipadress):
       super().__init__(Parent)
       nom = customtkinter.CTkLabel(self,text=nom,fg_color='transparent',font=("bodoni mt",26,"bold"))
       ipadress = customtkinter.CTkLabel(self,text=ipadress,fg_color='transparent',font=("bodoni mt",26,"bold"))

       nom.grid(row=0,column=1,pady=24,padx=(23,0)) 
       ipadress.grid(row=1,column=1,pady=4,padx=13) 

       self.configure(height=100, width=250,corner_radius=14,fg_color="#383E49")
       self.pack(side="bottom", padx=12,pady=14,ipady=24,ipadx=14)
       self.grid_propagate(0)