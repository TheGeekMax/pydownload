from selection import *
from blessed import Terminal
import os
import subprocess
from main import *
from time import sleep

print(term.clear)
main = 0
while main != 4:
    main = selection(["Telecharger 1 playlist","Telecharger plusieurs playlists (links.txt)","Lancer le ftp","Lancer le server web","Sortir"])
    if main == 0:
        printAt("lien de la playlist :",1,9)
        link = inputAt(">",1,10)
        try:
            print(term.clear)
            download(link)
            print(term.clear)
            sleep(4)
        except:
            printAt("lien de telechargement non valide !",1,1)
            sleep(4)
            print(term.clear)
    elif main == 2:
        print(term.clear)
        printAt("FTP allumé , restart nessesaire pour le menu",1,term.height-1)
        from ftp import *
    elif main == 3:
        subprocess.call("start npm test",shell = True)
print(term.clear)
