lemmikfilmid = []
i = 1
print("Sisesta oma lemmikfilmid (üks korraga). Tühjaks jätmine lõpetab.")


while i > 0:
    film = input("Film: ").strip().lower()
    if film == "":
        i = 0
    lemmikfilmid.append(film)


lemmik = input("Mis on su kõige lemmikum film? ").strip().lower()

if lemmik in lemmikfilmid:
    print(f"Ossa, oled oma '{lemmik}' isegi kaks korda pannud.")
else:
    print(f"Kus on sinu '{lemmik}'?")


if input("Kas sulle meeldib 'inception'? (jah/ei) ").strip().lower() == "jah":
    if "inception" not in lemmikfilmid:
        lemmikfilmid.append("inception")
else:
    print("Aga miks? See on ju hea.")


if any("terminator" in film for film in lemmikfilmid):
    print("you'll be back")


if any("vanamehe film" in film for film in lemmikfilmid):
    print("aga kuš šu šnikurš on šiiš?")

# Filmide koguarv ja kommentaar
arv = len(lemmikfilmid)
print(f"Sul on lemmikfilmide nimekirjas {arv} filmi.")

if arv <= 5:
    print("Sa ei vaata väga palju filme vist.")
elif arv <= 10:
    print("Käid tihti kinos?")
else:
    print("Siis, pole mul siin midagi öelda härra movieguru, headaega.")