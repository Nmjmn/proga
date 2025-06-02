from tkinter import *
import time
i = 1

valik = ""
while valik not in ["pall", "ruubiku-kuubik", "vihmavari", "vape"]:
    valik = input("Vali objekt (pall, ruubiku-kuubik, vihmavari, vape): ").strip().lower()

failinimi = "C:/Users/opilane/Desktop/" + valik + ".png"

raam = Tk()  
pilt = PhotoImage(file=failinimi)  
raam.title("Liikuv objekt")
raam.geometry("800x900")

tahvel = Canvas(raam, width=800, height=900)
tahvel.pack()

objekt = tahvel.create_image(50, 50, anchor=NW, image=pilt)

while i>0:
    for _ in range(100):
        tahvel.move(objekt, 5, 0) 
        raam.update()  
        time.sleep(0.01)
    for _ in range(100):
        tahvel.move(objekt, 0, 5)
        raam.update()  
        time.sleep(0.01)
    for _ in range(100):
        tahvel.move(objekt, -5, 0)
        raam.update()  
        time.sleep(0.01) 
    for _ in range(100):
        tahvel.move(objekt, 0, -5)
        raam.update()  
        time.sleep(0.01)
raam.mainloop()