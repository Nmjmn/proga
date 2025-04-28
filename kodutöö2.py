nimed = []
vastus = '0'
i = False

while i == False:
    perekonna = input('Kas teil on perekonnaliikmeid (jah/ei):')
    if perekonna == 'jah':
        while vastus !='':
            vastus = input('Sisestage oma pereliikmete lemmikloomanimed:')
            i = True            
            nimed.append(vastus)
                
    elif perekonna == 'ei':
        while  i == False:
            vastus1 = input('Kas teil on lemmikloomi? (jah/ei)')
            if vastus1 == 'jah':
                while vastus!='':
                    vastus = input('Sisestage oma lemmikloomanimed:')
                    i = True
                    nimed.append(vastus)
            elif vastus1 == 'ei':
                i = True
                print('Kahju, pesaleidjas on palju kasse kes tahaksid kodu.')
    

for nimi in nimed:
    print(nimi)
    
