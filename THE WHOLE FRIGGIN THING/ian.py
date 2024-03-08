def ian():
    import random
    from colorama import Fore
    import time
    import os
    inventory = []
    health = []
    os.system("clear")
    print ("Old Man: Welcome all who dare challenge my dungeon")
    print ("Old Man: all who enter my dungeon shall die")
    print ("Old Man: would you like to enter CHILD")

    entrance = input("y/n? ")
    if entrance == "y":
        print("Old Man (laughing): Good Luck!")
        print("you black out")
        print("as you wake up in a dimly lit room you realize that 100G is gone from your inventory")
    elif entrance == "n":
        print("Old Man: Are You Sure")
        sure = input("y/n? ")
        if sure == "y":
            print("Old Man (laughing): Good Luck!")
            print("you black out")
            print("as you wake up in a dimly lit room you realize that 100G is gone from your inventory")
        elif sure == "n":
            print("Old Man: Then DIE!")
            print("You feel yourself slowly fall over as you hear the Old Man laughing")
    print("as you pick yourself up you realize that you have a Weak_Stick in your inventory")
    inventory.append(str(['Weak_Stick']))
    print("you keep looking around and you see a single doorway")
    print("will you walk through the door or stay here?")
    first_room = input("y/n? ")
    if first_room == "y":
        print("you slowly peer through the doorway")
    elif first_room == "n":
        print("your eyes glaze back into your head and you Die")
        quit()
    print("you see 3 short green men conversing in the center of the room")
    print("will you fight, run, or try to talk to them?")
    first_room_one = input("f/r/t? ")
    if first_room_one == "r":
        print("your eyes glaze back into your head and you Die")
        quit()
    elif first_room_one == "t":
        print("you walk up to the short green men you say hello to them")
        print("they immediatly turn in unison each pulling out there swords and killing you")
        quit()
    elif first_room_one == "f":
        pass #<-- delete that when you want to edit it all its for is to have it not error