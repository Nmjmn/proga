import tkinter as tk
import time
import os

valik = ""
while valik not in ["pall", "ruubiku-kuubik", "vihmavari", "vape"]:
    valik = input("Vali objekt (pall, ruubiku-kuubik, vihmavari, vape): ").strip().lower()

failinimi = "C:/Users/opilane/Desktop/" + valik + ".png"

if not os.path.exists(failinimi):
    print(f"Fail {failinimi} ei ole leitud!")
    exit(1)

raam = tk.Tk()
raam.title("Liikuv objekt")
raam.geometry("800x900")

tahvel = tk.Canvas(raam, width=800, height=900)
tahvel.pack()
pilt = tk.PhotoImage(file=failinimi)
objekt = tahvel.create_image(50, 50, anchor=tk.NW, image=pilt)
raam.update()
while valik == "pall" or valik == "ruubiku-kuubik" or valik == "vihmavari" or valik == "vape":
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