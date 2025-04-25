nimi = ''

while nimi == '':
    nimi = input('Palun sisetage oma ees nimi ja perekonnanimi').title()
    nimearv = nimi.count(' ')+nimi.count('-')+1
print('Sul on ' +str(nimearv)+' nime')