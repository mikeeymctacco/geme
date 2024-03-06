
from colorama import Fore
inventory = [] 
a = 0
c = 0
s = 0
import time
import os
os.system('clear')
print("Dungeon Master: Welcome to my Dungeon")
#time.sleep(3)
print("Dungeon Master: This is the hardest Dungeon are you sure you want to continue?")
#time.sleep(4)
x = input("y/n? ")
if x == "y":
    print("Ok then lets continue")
    print(f"{Fore.RED}You lose 500G{Fore.WHITE}")
else: 
    print("THEN DIE")
#    time.sleep(2)
    print("you feel your throat close and you die")
print("You walk into a room and you see many bodies on the ground and some have weapons some have amulets")

def AmorWe():
    c = int(input("which one would you like to steal from? amulets (1) or weapons (2) "))
    if c == 1:
      global a 
      a = int(input("which one there is 6 bodies (type a number 1-6)"))
    elif c == 2:
      global s
      s = int(input("which one there is 3 bodies with weapons (type a number 1-3)"))
    else:
        print("nope")
AmorWe()


if a == 4:
        inventory.append(str(['low_power_amulet']))
        print(f"{Fore.GREEN}You Aquired a low powered amulet{Fore.WHITE}")
elif s == 3:
        inventory.append(str(['basic_sword']))
        print(f"{Fore.GREEN}You Aquired a basic sword{Fore.WHITE}")
else:
    print("you get nothing")
print("would you like to continue")
print("y/n? ")
#time.sleep(2)
print("ha you don't get a choice you have to continue")
#time.sleep(2)
print("you get forced into the next room")
print("the door slams behind you")
#time.sleep(1)
print("Old Woman: I've been expecting you")
#time.sleep(1)
print("In this room you need to either use your magic or your sword")
print("Or if you have nothing you may try to spare the monster")
print("a monster drops from the celling")
input("Fight? y/n")
if "basic_sword" or "low_power_amulet" in inventory:
    print("you attack the monster ")
    #time.sleep(1)
    print("you damage the monster he looks very wounded")
    print("he attacks what do you do")

#everything past this comment needs to stay last
while True:
    move = input().lower().split()

    if move[0] == "inv":
        print(*inventory)
os.system('clear')