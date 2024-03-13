def ian():
    import random
    from colorama import Fore
    import time
    import os
    inventory = []
    gold = 500
    def inv():
        print(*inventory)
        print(gold)
    os.system("clear")
    print ("Old Man: Welcome all who dare challenge my dungeon")
    time.sleep(1)
    print ("Old Man: all who enter my dungeon shall die")
    time.sleep(1)
    print ("Old Man: would you like to enter CHILD")
    time.sleep(1)

    entrance = input("y/n? ")
    if entrance == "y":
        print("Old Man (laughing): Good Luck!")
        time.sleep(1)
        print("you black out")
        time.sleep(1)
        print("as you wake up in a dimly lit room you realize that 100G is gone from your inventory")
        time.sleep(1)
        gold -= 100
    elif entrance == "n":
        print("Old Man: Are You Sure")
        time.sleep(1)
        sure = input("y/n? ")
        if sure == "y":
            print("Old Man (laughing): Good Luck!")
            time.sleep(1)
            print("you black out")
            time.sleep(1)
            print("as you wake up in a dimly lit room you realize that 100G is gone from your inventory")
            gold -= 100
        elif sure == "n":
            print("Old Man: Then DIE!")
            time.sleep(1)
            print("You feel yourself slowly fall over as you hear the Old Man laughing")
            quit()
    print("as you pick yourself up you realize that you have a Weak Stick in your inventory")
    inventory.append(str('weak stick'))
    print("you keep looking around and you see a single doorway")
    time.sleep(1)
    print("will you walk through the door or stay here?")
    time.sleep(1)
    first_room = input("y/n? ")
    if first_room == "y":
        print("you slowly peer through the doorway")
    elif first_room == "n":
        print("your eyes glaze back into your head and you Die")
        quit()
    print("you see 3 short green men conversing in the center of the room")
    time.sleep(1)
    print("will you fight, run, or try to talk to them?")
    time.sleep(1)
    first_room_one = input("f/r/t? ")
    if first_room_one == "r":
        print("your eyes glaze back into your head and you Die")
        quit()
    elif first_room_one == "t":
        print("you walk up to the short green men you say hello to them")
        time.sleep(1)
        print("they immediatly turn in unison each pulling out there swords and killing you")
        quit()
    elif first_room_one == "f":
        print("will you pull out your stick or fight with your hands?")
        time.sleep(1)
    first_room_two = input("stick/hands? ")
    time.sleep(1)
    if first_room_two == "stick":
        print("you pull out your weak stick and go into a ready battle stance")
    elif first_room_two == "hands":
        print("you put yourself in a battle ready stance and get ready to run at the three green men")
        time.sleep(1)
        print("you run out there and hit the closest green man and knock him out")
        time.sleep(1)
        print("you take a deep breath and run at the first one hitting on the head knocking it out")
        time.sleep(1)
        print("the other two green men turn to kill you")
        time.sleep(1)
        print("you have to doge or you will die")
        time.sleep(1)
        print("the other two green men turn immediatly and cut you to peices")
        quit()
    print("you take a deep breath and run at the first one hitting on the head knocking it out")
    time.sleep(1)
    print("the other two green men turn to kill you")
    time.sleep(1)
    print("you have to dodge or you will die")
    time.sleep(4)
    options = [
    'd'
    ]
    word = random.choices(options)
    startTime = time.time()



    inventory.ap
    time.sleep(4)
    print("the one on the left, and the one right in front of you")
    time.sleep(4)
    print("which will you choose?")
    time.sleep(1)
    doorchoice = input("straight/left? ")
    if doorchoice == "straight":
        print("you walk up to the door right in front of you")
        time.sleep(4)
        print("this door has a crazy disign on it")
        time.sleep(3)
        print("you try the key it does not work")
        print("then suddenly the floor opens up right below you then you fall in and die")
        quit()
    elif doorchoice == "left":
        print("you walk up to the door to the left of you")
        time.sleep(4)
        print("its just a plain Iron door with a handle and key hole")
        time.sleep(4)
        print("you try the Key")
        time.sleep(1)
        print("it works you think as a wave of relief washes over you")
    print("you then open the door and boooom a long is swinging straight at your face")
    print("quick you have 2 seconds to doge")
    time.sleep(2)
    options = [
    'd'
    ]
    word = random.choices(options)
    startTime = time.time()



    inventory.ap
    print("whoa you skillfully doge the log as you jump away from the door")
    time.sleep(2)
    print("you then look around the room")
    time.sleep(2)
    print("as you scan your old room again you see that the green man that you knocked out is gone")
    time.sleep(5)
    print("you quickly turn around to see the green man running towards you with its sword pointed forwars")
    time.sleep(5)
    print("quick you have 2 seconds to doge")
    time.sleep(2)
    options = [
    'd'
    ]
    word = random.choices(options)
    startTime = time.time()



    inventory.ap
    print("you doge his attack and take your weak sword and kill him")
    time.sleep(2)
    print("now you can go into that new room")
    time.sleep(3)
    print("as you walk in you see 5 green men guarding a chest")
    time.sleep(5)
    print("you feel a sudden urge to run in screaming head on at the green men")
    time.sleep(6)
    will = input("will you give in to this urge? " )
    if will == "yes, y":
        print("you run into the room screaming at the top of your lungs")
        time.sleep(4)
        print("the front one cuts you down")
        time.sleep(3)
        print("you lay there bleeding until you die")
        quit()
    elif will == "no, n":
        print("you made a good choice")
        time.sleep(3)
        print("if you had gone running in there you would have been dead for sure")
        time.sleep(6)
    print("now you have two choices you can sneak around them or fight")
    time.sleep(4)
    wall = input("s/f")
    if wall == "f":
        print("you go out to figh them and they surround you")
        time.sleep(3)
        print("you are then cut up into pieces and you die")
        quit()
    elif wall == "s":
        print("you slowly crawl around the room against the wall hoping that they dont notice you")
        time.sleep(7)
        print("you get all the way around them and now you are behind them")
        time.sleep(4)
        print("you kill all 5 of them in one blow")
    print("now you can open the chest and see whats inside")
    time.sleep(3)
    print("its a boss key")
    time.sleep(1)
    print("that must be what opens the other door you think to yourself")
    time.sleep(4)
    print("you then go back into the other room and unlock the other door")
    time.sleep(3)
    print("then you hear what sounds like battle music starting")
    time.sleep(8)
    print("you then just walk right in")
    time.sleep(3)
    print("goblin sorcerer: WHO DARES ENTER MY DUNGEON KILL MY GUARDS AND CHALLENGE ME")
    time.sleep(6)
    name = input("what is your name player?: ")
    print("SO YOUR NAME IS" + name)
    time.sleep(3)
    print("WELL NOW I WILL HAVE TO KILL YOU FOR WHAT YOU HAVE DONE")
    time.sleep(5)
    print("KILL THEM SKELETRON")
    time.sleep(3)
    print("then you see this floating skull with floating arms right next to it come down from the ceiling")
    time.sleep(8)

    #stuff after this stays at the end
    while True:
        move = input().lower().split()


        if move[0] == "inv":
            inv()
        break
    