from tkinter import *
from datetime import date
from datetime import timedelta
import pandas as pd
import customtkinter
from PIL import Image, ImageTk
import api_test as api

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        WIDTH = 480
        HEIGHT = 520
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Your Week in The News")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=250)
        
        self.frame_1 = customtkinter.CTkFrame(master=self, width=300, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, columnspan=2 ,sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="Your Week in Images!",
                                              text_font=("Roboto Medium", -20))  
        
        self.label_1.grid(row=1, column=0, pady=20,columnspan=2 ,sticky="new")
        self.label_mode = customtkinter.CTkLabel(master=self.frame_1, text="News Category:")
        self.label_mode.grid(row=2, column=3, pady=0, padx=20, sticky="w")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_1,
                                                        values=["Politics", "Culture", "Culinary"])
        self.optionmenu_1.grid(row=3, column=3, padx=20, sticky="w")
        
        self.label_mode = customtkinter.CTkLabel(master=self.frame_1, text="News Organization:")
        self.label_mode.grid(row=4, column=3, pady=0, padx=20, sticky="w")
        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_1,
                                                        values=["BBC", "New York Times", "Washington Post"])
        self.optionmenu_2.grid(row=5, column=3, pady=10, padx=20, sticky="w")

        dates = []
        day_of_week= []
        buttons = []
        date1 = date.today()
        for i in range(7):
            dates.append(date.today() - timedelta(days = i))
            day_of_week.append(pd.Timestamp(dates[i]))
           
            buttons.append(customtkinter.CTkButton(master=self.frame_1, text= day_of_week[i].day_name(), height=32,compound="right",hover_color="#C77C78",command =lambda:api.printImages(dates[i])))
            buttons[i].grid(row=i+2, column=0, columnspan=2, padx=20, pady=(10), sticky="ew")

        
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
        