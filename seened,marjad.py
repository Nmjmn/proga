seened = ["pilvik", "kukeseen", "kõrvetis"]
seene_info = [
    "Pilvik on suur ja ümar seen, mida süüakse pärast kuumutamist.",
    "Kukeseen on kollakas ja hea söögiseen.",
    "Kõrvetis on mürgine ja tuleks ära tunda."
]
marjad = ["maasikas", "pohl", "mustikas"]
marja_info = [
    "Maasikas on punane ja magus marja.",
    "Pohl on hapukas marja, mida kasutatakse moosides.",
    "Mustikas on tume metsamarja, mis sisaldab palju antioksüdante."
]
i = 1
while i > 0:
    valik = input("Kas otsid seent või marja? ('seent', 'marja', 'välju'): ").strip().lower()

    if valik == "välju":
        print("Head aega!")
        i = 0  
   
    elif valik == "seent":
        j = 1
        
        while j > 0:
            print("\nSeened:")
            for k in range(len(seened)):
                print(f"{k+1}. {seened[k]}")
            print(f"{len(seened)+1}. lisa juurde")
            print(f"{len(seened)+2}. tagasi")

            sisend = input("Vali number: ").strip()
            if sisend.isdigit():
                nr = int(sisend)
                
                if nr == len(seened)+1:
                    nimi = input("Uue seene nimi: ").strip().lower()
                    kirjeldus = input("Info selle seene kohta: ").strip()
                    seened.append(nimi)
                    seene_info.append(kirjeldus)
                    print("Uus seen lisatud.\n")
                
                elif nr == len(seened)+2:
                    j = 0  
               
                elif 1 <= nr <= len(seened):
                    print(f"\n{seened[nr-1].capitalize()}: {seene_info[nr-1]}\n")
               
                else:
                    print("Vale number.")
           
            else:
                print("Sisesta number.")

    elif valik == "marja":
        l = 1
        while l > 0:
            print("\nMarjad:")
            for k in range(len(marjad)):
                print(f"{k+1}. {marjad[k]}")
            print(f"{len(marjad)+1}. lisa juurde")
            print(f"{len(marjad)+2}. tagasi")
            
            sisend = input("Vali number: ").strip()
            if sisend.isdigit():
                nr = int(sisend)

                if nr == len(marjad)+1:
                    nimi = input("Uue marja nimi: ").strip().lower()
                    kirjeldus = input("Info selle marja kohta: ").strip()
                    marjad.append(nimi)
                    marja_info.append(kirjeldus)
                    print("Uus marja lisatud.\n")

                elif nr == len(marjad)+2:
                    l = 0  

                elif 1 <= nr <= len(marjad):
                    print(f"\n{marjad[nr-1].capitalize()}: {marja_info[nr-1]}\n")

                else:
                    print("Vale number.")
            else:
                print("Sisesta number.")
    else:
        print("Palun vali 'seent', 'marja' või 'välju'.")
