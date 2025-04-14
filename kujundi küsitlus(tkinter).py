from tkinter import *

raam = Tk()
tahvel = Canvas(raam, width = 600, height = 600)

vana = 0
vanus = 18
värv = ""
kujund = ""
while True:
    vana = int(input("Kui vana te olete?"))

    if(vana > vanus):
        värv = input("Mis on teie lemmik värv (inglise keels)")
        kujund = input("Mis on teie lemmik kujund (ristkülik; ovaal; kolmnurk; ring)")
    
        if(kujund == "ristkülik"):
            tahvel.create_rectangle(50, 50, 300,150, fill = värv)
            tahvel.create_text(175,100, text = vana)
            break
        if(kujund == "ring"):
            tahvel.create_oval(50,50,300,300,fill = värv)  
            tahvel.create_text(175,175, text = vana)
            break
        if(kujund == "ovaal"):
            tahvel.create_oval(50,150,300,250,fill = värv)
            tahvel.create_text(175,200, text = vana)
            break
        if(kujund == "kolmnurk"):
            tahvel.create_line(200, 100, 200,200, 300, 200,200,100,fill = värv)
            tahvel.create_text(225,180, text = vana)
            break
        
    if(vana < 15):
        print("Kahjuks olete liiga noor ja kujundi ei saa")
    
    
    
    
tahvel.pack()
raam.mainloop()    
