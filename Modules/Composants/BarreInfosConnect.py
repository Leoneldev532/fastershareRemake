import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class BarreInfoConnect(customtkinter.CTkFrame):

 

   def __init__(self, Parent,nbreconnecttxt,status,signal):
       super().__init__(Parent)
       def setcolor(texte):
        if(texte=="● connecté"):
           return "#1d862b"
        else:
           return "red"
       self.configure(height=40, width=570,fg_color="#383E49",corner_radius=24 )
       self.pack(side="right")

       nbreconnect = customtkinter.CTkLabel(self,text=nbreconnecttxt,height=Parent._current_height,font=("bodoni mt",20))
       nbreconnect.pack(side="left",fill="x",padx=(18,0),expand=True)

       status = customtkinter.CTkLabel(self,text=status,text_color=setcolor(status),font=("bodoni mt",24),height=Parent._current_height)
       status.pack(side="left",fill="x",expand=True)

       nbreconnectsa = customtkinter.CTkLabel(self,text=signal,height=Parent._current_height,font=("bodoni mt",20),text_color="red")
       nbreconnectsa.pack(side="left",fill="x",padx=(0,18),expand=True)
       
  