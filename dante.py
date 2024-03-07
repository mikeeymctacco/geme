import random
from colorama import Fore
import time
import os
inventory = []
def smrm():
    print("Once you enter the door you see a small room with a chest and a door.")
    #time.sleep(4)
    usr2 = int(input("Would you like to open the chest (1) or continue without opening the chest (2)? "))
    if usr2 == 1:
        print(f"{Fore.GREEN}You have accuired a Strong Sword. {Fore.WHITE}")
        inventory.append(str(['strong_sword']))
        print(f"{Fore.YELLOW}You have accuired 10 gold. {Fore.WHITE}")
        rm2()
    else:
        print("You have entered the room without opening the chest.")
        rm2()
os.system('clear')
print("Dungeon Guardian: Welcome traveler!")
#time.sleep(3)
print("Dungeon Guardian: If you would like to enter this dungeon you will have to pay me 250 gold.")
#time.sleep(5)
def rm3():
    usr = input("Do you want to enter the door on the left, or the right? ").strip()
    if usr == "right":
        print("You enter a room with a big chest.")
        #time.sleep(1)
        usr3 = input("Do you open the chest? y/n ").strip()
        if usr3 == "y":
         print(f"{Fore.GREEN}You have found a Long Sword! {Fore.WHITE}")
         inventory.append(str(['long_sword']))
         print("You then turn back and go to the other door.")
         rm3()
        else:
            print("You ignore the chest and you turn back to go the other way.")
    elif usr == "left":
     print("You go to the door on the left and enter the next room.")
     print("Right as you enter the room a monster attacks you!")
    if 'strong_sword' in inventory:
            print("Quick dodge!")
            dodge()

global lvl1
lvl1 = [
     'dodge'
    ]
def dodge():
 

    word = random.choice(lvl1)
    start_time = time.time()
    global one
    one = input("You have 3 seconds to type: {}\n".format(word))

    while time.time() - start_time > 2 or one != word:
        print("you try to dodge but")
        start_time = time.time()
        one = input("You Die") 
        quit()
    print("you protect  yourself from death") 
def death():
    print("You have died nerd now you have to restart loser.")
def rm2():
    print("In the next room you find a monster")
    usr2 = input("Would you like to kill the monster? y/n ").strip()
    if usr2 == "y":
      if 'strong_sword' in inventory:
         print("You have killed the monster")
         print(f"{Fore.YELLOW}The monster dropped 5 gold. {Fore.WHITE}")
      else:
        print("You tried to kill the monster but the monster was too strong for you.")
        death()
    else:
     print("The monster attacked you and you did not fight back.")
     death()

usr1 = input("Do you pay the Dungeon Guardian 250 gold to enter the dungeon? y/n ").strip()

if (usr1 == "y"):
    print("You pay the Dungeon Guardian 250 gold and you enter the dungeon.")
    print(f"{Fore.RED}-250G {Fore.WHITE}")
else:
    print("Dungeon Guardian: That's a shame")
#    time.sleep(2)
    print("Dungeon Guardian: You can always come back another time.")
#    time.sleep(3)
    print("You turn around and leave the dungeon.")
#    time.sleep(3)

print("When you enter the dungeon you find a small room with 4 doors on each side of the room.")
#time.sleep(4)
    
usr = input("Do you want to go to the door straight, left, or right? ").strip()
if usr == "straight":
    print("You continue going straight and enter the door.")
elif usr == "right":
    print("You turn right and go through the door.")
    time.sleep(3)
elif usr == "left":
        print("You turn left and go through the door.")
        time.sleep(3)
        print("You see a monster.")
        time.sleep(2)
        print("The monster takes a step towards you and the lights turn off.")
        time.sleep(3)
        print("The lights have turned back on but the monster was not there.")
        time.sleep(2)
        print("Suddenly the monster attacked you from behind.")
        time.sleep(1)
        death()

print("When you go through the door you see a small room with 2 doors on both sides of the room.")
rm3()
#time.sleep(4)


#everything after this stays at the end
while True:
    move = input().lower().split()

    if move[0] == "inv":
        print(*inventory)

os.system('clear')
