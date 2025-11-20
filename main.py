import random
import os
from time import sleep
from colorama import Fore, Style

def lvl1():
    password = "let mee in"
    while True:  
        os.system("cls")  
        print("This is level one while im writing this i have no idea what im doing")
        print("Whzzdvyk:(sla tll pu)")
        guess = input("Password: ")
        if guess == password:
            print("Great! you got the first level")
            break  
        else:
            print(Fore.RED + "Wrong, try again!" + Style.RESET_ALL)
            input("Press Enter to try again...")
    lvl2()
def lvl2():
    while True:
        password = "incorrectly"
        os.system("cls")
        guess = input("What word in the English Language is always spelled incorrectly?")
        if guess.lower() == password:
            print("Damn, you are good!")
            break
        else:
            print(Fore.RED + "Wrong, try again!" + Style.RESET_ALL)
            input("Press Enter to try again...")
    lvl3()
def lvl3():
    password = "iloveboys"
    while True:
        os.system("cls")
        print("Tip:Don't use space between them")
        print("16,1,19,19,23,15,18,4,9,19,9,12,15,22,5,2,15,25,19")
        guess = input("Password: ")
        if guess.lower() == password:
            print("Good job. level 3 completed")
            break
        else:
            print(Fore.RED + "Wrong, try again!" + Style.RESET_ALL)
            input("Press Enter to try again...")


print("Hey Guys!")
print("I felt bored so i made this game")
print("So it could be ass")
print("Try figuring out how levels work")
print("Enjoy!")
sleep(5)
os.system("cls")
lvl1()