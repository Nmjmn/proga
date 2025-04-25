nimed = []
vastus = '0'

while vastus != '':
    vastus = input('Sisestage oma lemmikloomanimesid')
    if vastus!='':
        nimed.append(vastus)
    
for nimi in nimed:
    print(nimi)