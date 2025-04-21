from tkinter import*
raam = Tk()
raam.title("Pilt")
tahvel = Canvas(raam,width = 500, height = 500, background = "white")



nahavärv = ""
kasmüts = ""
mismüts = ""
hetkeilm = ""
kasutajatuju = ""

while (nahavärv == "" or kasmüts == "" or kasutajatuju == "" or hetkeilm == ""):
    if (nahavärv == ""):
        nahavärv = input("Mis on teie nahavärv: hele/latiino/punanahk/pronksjas/tume")
    if (kasmüts == ""):
        kasmüts = input("Kas teil on müts? jah/ei")
    if (kasmüts != "ei"):
        mismüts = input("Milline on müts teil on: nokamüts/torumüts/fedora")
    if (kasutajatuju == ""):
        kasutajatuju = input("Mis tuju teil on: 1-hea/2-tavaaline/3-halb/4-üllatunud/5-tülpinud")
    if (hetkeilm == ""):
        hetkeilm= input("Milline on ilm: pilvitu/pilvine/vihmane")

if nahavärv.lower() == "hele":
    nahavärv="#FFCCE0"
if nahavärv.lower() == "latiino":
    nahavärv="#DEAD4B"
if nahavärv.lower() == "punanahk":
    nahavärv="#DE7C4B"
if nahavärv.lower() == "pronksjas":
    nahavärv="#8C390F"
if nahavärv.lower() == "tume":
    nahavärv="#4F1E05"


def  joonistaNägu(nahavärv,kasmüts,mismüts,kasutajatuju,hetkeilm):
    tahvel.create_oval(50,50,450,450,fill = nahavärv,outline="black",width=5)
    tahvel.create_oval(140,140,160,160,fill="green",outline="black",width=2)
    tahvel.create_oval(340,140,360,160,fill="green",outline="black",width=2)
    if kasmüts.lower() == "jah":
        if mismüts.lower() == "nokamüts":
           tahvel.create_polygon(100,100,200,100,200,75,250,25,300,25,400,75,400,100, fill= "red", outline="black",width=10)
        if mismüts.lower()=="torumüts":
            tahvel.create_polygon(50,100,150,100,150,0,350,0,450,100, fill="gray",outline = "black",width = 10)
        if mismüts.lower()=="fedora":
            tahvel.create_oval(150,25,350,100, fill="yellow",outline="black",width=10)
            tahvel.create_polygon(251,76,239,82,265,85,296,74,283,8,135,38,229,17,215,18, fill="yellow",outline="black",width=10)



                 
    else:
        tahvel.create_polygon(93,24,77,146,171,117,245,130,317,112,412,132,392,17,363,40,331,17,307,40,267,17,246,40,205,17,181,40,153,17,122,40,93,17,outline="black",fill="blue")
        if int(kasutajatuju.lower()) == 1:
            tahvel.create_line(150,336,172,365,218,382,285,382,336,365,365,336,fill="black",width=10)
        elif int(kasutajatuju.lower()) == 2:
            tahvel.create_line(150,336,365,336, fill ="black", width = 10)
        elif int(kasutajatuju.lower()) == 3:
            tahvel.create_line(150,382,172,345,218,336,285,336,336,345,365,382, fill="black",width=10)
        elif int(kasutajatuju.lower()) == 4:
            tahvel.create_oval(150,336,350,382, fill="brown", outline="black", width =10)
        elif int(kasutajatuju.lower()) == 5:
            tahvel.create_line(150,382,172,345,218,336,285,336,336,345,365,382,fill="black",width = 10)
            tahvel.create_line(125,200,175,230,width = 10)
            tahvel.create_line(325,230,375,200,width = 10)
        else:
            print("Hell nah")
            
        if hetkeilm.lower() == "pilvitu":
            tahvel.configure(bg="lightblue")
            
        if hetkeilm.lower() == "pilvine":
            tahvel.configure(bg="gray")
            
        if hetkeilm.lower() == "vihmane":
            tahvel.configure(bg="blue")
            
joonistaNägu(nahavärv,kasmüts,mismüts,kasutajatuju,hetkeilm)   
tahvel.pack()
raam.mainloop()
