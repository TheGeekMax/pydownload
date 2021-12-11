from blessed import Terminal
from time import sleep

term = Terminal()
end = True
choose = 0

def printAt(text,x,y):
    with term.location(x=x, y=y):
            print(text)

def inputAt(text,x,y):
    var = ""
    with term.location(x=x, y=y):
        var = input(text)
    return var

def clamp(val,mins,maxs):
    temp = val
    if temp < mins:
        temp = mins
    elif temp > maxs:
        temp = maxs
    return temp

def selection(choices,y=0,selection = ["- ","> "],titre = "selectionne un choix"): # a add , selection, titre
    var = ''
    choosen = 0
    with term.cbreak():
        while var == "" or not var.name == "KEY_ENTER":
            printAt(titre,0,y)
            for i in range(len(choices)):
                printAt(selection[int(i==choosen)]+choices[i],1,y+2+i)
            var = term.inkey(timeout=1)
            if var and var.is_sequence:
                if var.name == "KEY_UP":
                    choosen = clamp(choosen -1,0,len(choices)-1)
                elif var.name == "KEY_DOWN":
                    choosen = clamp(choosen +1,0,len(choices)-1)
    return choosen
        
