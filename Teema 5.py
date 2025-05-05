from urllib.request import urlopen
from webbrowser import*

failVeebis = urlopen('https://jurivaitmaa21.thkit.ee/palmisaargame.txt')
baidid = failVeebis.read()
tekst= baidid.decode()
teksteidadena = tekst.splitlines()
failVeebis.close()
print(teksteidadena[9][16])

filenamefromsite= input("millistfaili avada tahad?")
open('https://jurivaitmaa21.thkit.ee/'+filenamefromsite+'.txt')

