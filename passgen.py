import random as rand
import time 
import string as letters
import tkinter as tk
from tkinter import simpledialog as ui


print("")
print("Welcome to the password generator")
time.sleep(0.3)
print("Please answer a few questions to generate your pasworrd(s)")
time.sleep(0.3)


length = ui.askinteger(title="Character count",
                       prompt= """How many characters would you like? 
                    (Recommened 12+)""")
time.sleep(0.5)

#checks for a yes or no answer and returns and error if there isnt one
while True:
    symbols = ui.askstring(title="Symbols",prompt="Would you like to include symbols?")[0].lower()
    if symbols in "y":
        symbols = 1
        break
    elif symbols in "n":
        symbols = 0
        break
    else:
        print("That wasnt a valid answer, please try again")
        time. sleep(0.5)

passcount= ui.askinteger(title="Repeats", prompt="How many passwords would you like to generate?")
print("")
time.sleep(0.5)
print("Generating...")
time.sleep(1)
print("")


def generator(characters, symb, repeats):
#defines lists of characters
    alphabet = list(letters.ascii_letters)
    numbers = list(letters.digits)
    letternumbers = alphabet + numbers
    symbols = list("!@$%*&?")
    password=[]
    passlist=[]
#checks to see if symbols were selected
    if symb == 1:
        allchars = letternumbers+symbols
    else: 
        allchars = letternumbers

    R=0
    for r in range(0,repeats):
        R=R+1

        for c in range(0,characters):#Repeats to add right amount of characters
            password.append(allchars[rand.randint(0,len(allchars)-1)])#adds new charcter onto end of "password" list
        
        final =''.join(password) #Joins the password list together to print the final password

        print(f"password {R}: {final}")
        

        passlist.append(final)
        password = []
        final = ""
    
    print(f"""
    Final list: 
    {passlist}
""")

generator(length, symbols, passcount)

    
                


