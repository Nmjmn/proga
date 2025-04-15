from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = "Good morning" + nimi.get()
    messagebox.showinfo(message=tervitus)
    
#tkinteri aken
raam = TK()
raam.title("CostCoGreeting program")
raam.geometry("300x100")

# tekstikasti silt
silt = ttk.label(raam, text="Nimi")
silt.place(x=5, y=5)

#tekstikast ise'
nimi = ttk.Entry(raam)
nimi.place(x70, y=5, width=150)

# greeting nupp
nupp = ttk.Button(raam, text="Customer greeting", command = tervita)
nupp.place(x=70,y=40,width=150)