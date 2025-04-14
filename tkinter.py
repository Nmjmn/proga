from tkinter import *

raam = Tk()
raam.title("Window")

tahvel = Canvas(raam, width = 600, height = 600)
tahvel.create_rectangle(50, 50, 300,300, fill = "cyan",)

tahvel.create_line(50, 50, 300,300)
tahvel.create_line(100, 50, 100,100, 150, 100, width = 2, fill = "blue", arrow=LAST)

tahvel.create_rectangle(50, 50, 300,300, outline="red", width = 5)

tahvel.create_polygon(400, 400, 425,350,575, 350, 550, 400, outline = "black", fill="white", width = 5)

tahvel.pack()
raam.mainloop()