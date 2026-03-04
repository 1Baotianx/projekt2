# '''
# projekt2.py: Bil lista

# __author__  = "Eric Botander"
# __version__ = "1.0.0"
# __email__   = "eric.botander@elev.ga.dbgy.se"
# '''
from colors import bcolors #importerar färger
import os

carart = r'''
          .---;-,
       __/_,{)|__;._
    ."` _     :  _  `.  .:::;.    .::'
    '--(_)------(_)--' `      '::'
'''

os.system('cls') #clearar cmd 
billista = ["Porsche 911 Turbo S", "BMW M4 F82"] #Lista på bilar
while True: #Gör allt i en loop så användaren får välja när den e klar
    print(f"Favoritbilslistan! ({len(billista)} Bilar i listan).") # Rubrik på listan och hur många bilar som är i listan
    print(carart)
    for nummer, bilar in enumerate(billista, start=1): #gör det möjligt att snyggt printa ut listan med nummer 
        print(bcolors.BLUE+f"{nummer}. {bilar}"+bcolors.DEFAULT) #printar listan med nummer och färger
    inp = input("\n\033[91mTryck q för att avsluta programmet.\n\033[93mVälj respektive nummmer för bil att ändra/ta bort \n\033[92mEller skriv in en ny bil för att lägga till i listan.\n\033[0mInmatning: ") # Instruktioner till användaren med färger samt anvisning till vart inmatning ska ske.
    if inp == "q": 
        os.system('cls') # Om man matar in q avslutas programmet
        break
    elif inp.isdigit():
        inpint = int(inp)-1 
        inpint2 = int(inp)              #Motverkar error och ser till så att användaren lägger till en bil ifall listan blir tom
        if len(billista) == int(0):
            print("Listan är tom, lägg till en bil.")
            continue 
        elif inpint2 > len(billista):        
                print("\nDu valde inte ett nummer i listan, börja om.\n") #Motverkar error genom att säga till användaren att de inte valde ett nummer i listan istället för att få error
                continue 
        else:
            inp2 = str(input("Skriv in x för att ta bort eller skriv in det du vill ändra till: ")) #Så man kan ta bort eller ändra namn på en bil i listan
            if inp2 == "x":      
                billista.pop(int(inpint)) #Tar bort bil som valdes
                os.system('cls')
                continue
            else:
                billista.pop(int(inpint)) #Tar bort bil som valdes 
                billista.insert(int(inpint), f"{inp2}") #Skriver in bil som man ville ändra till
                os.system('cls')
                continue
    elif inp:
        billista.append(inp) # Om man skriver in en bil så läggs den till längst ner i listan
        os.system('cls')
        continue
    