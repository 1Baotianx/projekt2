# '''
# projekt2.py: Bil lista

# __author__  = "Eric Botander"
# __version__ = "1.0.0"
# __email__   = "eric.botander@elev.ga.dbgy.se"
# '''
from colors import bcolors
import os
os.system('cls')
billista = ["Porsche 911 Turbo S", "BMW M4 F82"]
while True:
    print("Det här är en lista på bra bilar!\n\n---------------------------------\n")
    for nummer, bilar in enumerate(billista, start=1):
        print(bcolors.BLUE+f"{nummer}. {bilar}"+bcolors.DEFAULT)
    inp = input("\n\033[91mTryck q för att avsluta programmet.\n\033[93mVälj respektive nummmer för bil att ändra/ta bort \n\033[92mEller skriv in en ny bil för att lägga till i listan.\n\033[0mInmatning: ")
    if inp == "q":
        os.system('cls')
        break
    elif inp.isdigit():
        inpint = int(inp)-1
        inpint2 = int(inp)
        if inpint2 > len(billista):
                print("\nDu valde inte ett nummer i listan, börja om.\n")
                continue     
        elif len(billista) == 0:
            print("Listan är tom, lägg till en bil.")
            continue
        else:
            inp2 = str(input("Skriv in x för att ta bort eller skriv in det du vill ändra till: "))
            if inp2 == "x":      
                billista.pop(int(inpint))
                os.system('cls')
                continue
            else:
                billista.pop(int(inpint))
                billista.insert(int(inpint), f"{inp2}")
                os.system('cls')
                continue
    elif inp:
        billista.append(inp)
        os.system('cls')
        continue
    