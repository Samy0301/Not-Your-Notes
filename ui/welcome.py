import customtkinter as ctk
from config import purple_bg


class WelcomePanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=purple_bg)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(self,
            text="Select a note from the list \n or create a new one to start", 
            font=ctk.CTkFont(size=16), text_color="#a688c5").grid(row=0, column=0)