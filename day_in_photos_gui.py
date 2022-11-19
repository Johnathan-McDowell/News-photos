from tkinter import *
from datetime import date
from datetime import timedelta
import pandas as pd
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        WIDTH = 780
        HEIGHT = 520
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Your Week in The News")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)
        
        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)
        self.label_1 = customtkinter.CTkLabel(master=self.frame_1,
                                              text="Your Week in Images!",
                                              text_font=("Roboto Medium", -16),)  
        self.label_1.grid(row=1, column=0, pady=20,sticky="ew")
        dates = []
        day_of_week= []
        buttons = []
        date1 = date.today()
        d = pd.Timestamp(date1)
        for i in range(7):
            dates.append(date.today() - timedelta(days = i))
            day_of_week.append(pd.Timestamp(dates[i]))
            
        self.buttons1 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[0].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons1.grid(row=2, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
        self.buttons2 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[1].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons2.grid(row=3, column=0, columnspan=2, padx=20, pady= 10, sticky="ew")
        self.buttons3 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[2].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons3.grid(row=4, column=0, columnspan=2, padx=20, pady=( 10), sticky="ew")        
        self.buttons4 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[3].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons4.grid(row=5, column=0, columnspan=2, padx=20, pady= 10, sticky="ew")       
        self.buttons5 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[4].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons5.grid(row=6, column=0, columnspan=2, padx=20, pady= 10, sticky="ew")
        self.buttons6 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[5].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons6.grid(row=7, column=0, columnspan=2, padx=20, pady=( 10), sticky="ew")       
        self.buttons7 = customtkinter.CTkButton(master=self.frame_1, text= day_of_week[6].day_name(), height=32,compound="right",hover_color="#C77C78", command=self.button_function)
        self.buttons7.grid(row=8, column=0, columnspan=2, padx=20, pady= 10, sticky="ew")
    def on_closing(self, event=0):
        self.destroy()
    def button_function(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
        