import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage

class BarreInfoConnect(customtkinter.CTkFrame):
   def __init__(self, Parent,nbreconnecttxt,status,signal):
       super().__init__(Parent)
           
       self.configure(height=40, width=370,fg_color="blue",corner_radius=24 )
       self.pack(side="right")

       nbreconnect = customtkinter.CTkLabel(self,text=nbreconnecttxt,height=Parent._current_height,bg_color="orange")
       nbreconnect.pack(side="left",fill="x",expand=True)

       status = customtkinter.CTkLabel(self,text=status,height=Parent._current_height,bg_color="orange")
       status.pack(side="left",fill="x",expand=True)

       nbreconnectsa = customtkinter.CTkLabel(self,text=signal,height=Parent._current_height,bg_color="orange")
       nbreconnectsa.pack(side="left",fill="x",expand=True)