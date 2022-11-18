from tkinter import *
from datetime import date
from datetime import timedelta
import pandas as pd


root = Tk()
root.geometry("1000x1500")   
frame = Frame(root)
frame.pack()
 
var = StringVar()
var.set("The News in Photos")
 
label = Label(frame, textvariable = var, font =("Comic sans",25) )
label.pack(pady=20)
 
dates = []
day_of_week= []
buttons = []
date1 = date.today()
d = pd.Timestamp(date1)
for i in range(7):
    dates.append(date.today() - timedelta(days = i))
    day_of_week.append(pd.Timestamp(dates[i]))
    buttons.append(Button(text = day_of_week[i].day_name()))
    buttons[i].config(height = 10, width = 20)
    buttons[i].pack(side = 'left', padx = 60)
        
MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)
 
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
 
Menu1 = Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", variable = Var1)
Menu1.add_checkbutton(label = "Cheese Burger", variable = Var2)
Menu1.add_checkbutton(label = "Salad", variable = Var3)
 
MenuBttn["menu"] = Menu1
MenuBttn.pack()



root.mainloop()
        