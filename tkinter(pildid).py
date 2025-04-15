from tkinter import *

raam= Tk()
raam.title("Pildid")
tahvel = Canvas(raam, width=400, height=400, background="white")
tahvel.grid

kuusk = PhotoImage(file="Nimetu.png")
img= tahvel.create_image(250, 80, image=kuusk)

lill = PhotoImage(file="Nimetdau.png")
img = tahvel.create_image(50,200, image=lill, activeimage = kuusk, anchor=NW)

raam.mainloop()