def michael():
    import random
    from colorama import Fore
    import time
    import os
    global inventory
    global gold
    inventory = []
    gold = 500
    a = 0
    c = 0
    s = 0
 
    #steven code
    def endm():
        print("you return to the town")
        print("GM: Good job you have won")
        print("GM: by the whay the moon lord was protekting the town")
    #end steven code
    #room functions
    def smrm():
        global gold
        os.system("clear")
        print("you enter a room and you see a small room with a chest and a door.")
        #time.sleep(4)
        usr2 = int(input("Would you like to open the chest (1) or continue without opening the chest (2)? "))
        if usr2 == 1:
            print(f"{Fore.GREEN}You have accuired a Strong Sword. {Fore.WHITE}")
            inventory.append(str('strong_sword'))
            print(f"{Fore.YELLOW}You have accuired 10 gold. {Fore.WHITE}")
            gold += 10
        else:
            print("You have entered the room without opening the chest.")
        x = input("do you want to go left, straight or right (l,s,r)")
        if x == 'r':
            rm1()
        elif x == 'l':
            rm2()
        elif x == 's':
            rm3()
    def rm1():
        global gold
        os.system("clear")
        print("you go right")
        #time.sleep(1)
        print("Cthulhu (os): I see you've made it this far but can you make it further?")
        #time.sleep(2)
        print("you see something float down, it looks like a eye")
        #time.sleep(2)
        print("this is my eye, it will be watching you for now, i'll be leaving you now")
        #time.sleep(2)
        x = input("you feel the sudden urge to attack it but do you (y/n?) ")
        if x == 'y' and 'strong_sword' in inventory:
            print("you try to attack the moster but in manuvers out of the way")
            #sleep.time(2)
            print("it shoots a laser from it's eye ")
            #time.sleep(1)
            print("right")
            #time.sleep(1)
            print("through")
            #time.sleep(1)
            print("your heart")
            print("you not so sadily parish")
            quit()
        else:
            print("you realize you can't fight this it's too strong")
        print("you notice a chest that wasn't there before")
        usr2 = int(input("Would you like to open the chest (1) or continue without opening the chest (2)? "))
        if usr2 == 1:
            print(f"{Fore.GREEN}You have accuired a Staff with a lighting emblem on it. {Fore.WHITE}")
            inventory.append(str('lightning_staff'))
            print(f"{Fore.YELLOW}You have accuired 10 gold. {Fore.YELLOW}")
            gold += 10
        print("you see 2 more doors one is marked with:")
        print(f"{Fore.RED}WARNING DO NOT ENTER{Fore.WHITE}")
        print("and you see one with a sign that says:")
        print(f"{Fore.GREEN}this room has candy{Fore.WHITE}")
        input("Which room Candy?(1) or Warning (2)")
        #time.sleep(2)
        rm2()
    def rm2():
        os.system("clear")
        print("you go left")
        print("you look around the room and see that there is nothing of intrest")
        print("But you see a rug a desk with some papers on it and 2 more doors")
        #time.sleep(1)
        print("oh and a torch")
        #time.sleep(1)
        rmrm()
    def rmrm():
        s = input("what would you like to do, look at the desk (1) or pick up the torch (3) ")
        if s == 1:
            print("you go and look at the papers and they read:")
            #time.sleep(2)
            print("2/20/1942")
            print("i've been in this doungen for 3 days now and I don't see any way i'm making it out")
            #time.sleep(3)
            print("I figured out that the torch never stops burning it's like the eternal flame or something...")
            #time.sleep(4)
            rmrm()
        elif s == 2:
            print("you go to the rug and pick it up and you see a trap door")
            #time.sleep(2)
            print("you drop inside")
            rm4()
        elif s == 3:
            print("you walk up to the torch")
            print("you pick it up")
            print("the torch and it goes out")
            #time.sleep(2)
            print("you hear stone sliding across the ground")
            #time.sleep(2)
            print("you see a small light and you walk towards it")
            finalfight()
    def rm3():
        global gold
        os.system("clear")
        print("you go straight")
        print("you just see a door a chest")
        usr2 = int(input("Would you like to open the chest (1) or continue without opening the chest (2)? "))
        if usr2 == 1:
            print("You have accuired a Mace.")
            inventory.append(str('mace'))
            print("You have accuired 10 gold.")
            gold += 10
            print("a monster walks in the room and strikes toward you")
            print("Quick DODGE!")
            options2()
        elif usr2 == 2:
            print("you leave the room")
            rm4()
    def finalfight():
        print("Moon Lord: welcome child to your DOOM!")
        if 'zennith' in inventory:
            print("NO YOU WILL NOT BEAT ME WIH THAT WEAPON")
            if 'zennith' not in inventory:
                print("What a pitiful weapon you'll never be able to beat me")
                print("he shoots you with his laser and you die")
                quit()
        options1 = [
        'd'
        ]
        word = random.choices(options1)
        startTime = time.time()
        one = input("he shoots you with the laser  type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 2 or one != str(*word):
            print("you react too late and moon lord hits you with the laser")
            startTime = time.time()
            one = input("You Die")
            break
        if one == 'd':
            print("you dodge the laser he tries to grab you")
            options2 = [
        'd', 'b'
        ]
        word = random.choices(options2)
        startTime = time.time()
        two = input("You have 2 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 2 or two != str(*word):
            print("he grabs you and crushes you")
            startTime = time.time()
            two = input("You Die")
        if two == 'd' or 'b':
            print("you dodge again")
            #time.sleep(2)
            print("he attacks again!")
        options3 = [
        
        ]
        if "zennith" in str(inventory):
            options3.append(str('zennith'))
        word = random.choices(options3)
        startTime = time.time()
        print("you see the oppurtunity to attack")
        three = input("You have 3 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 3 or three != str(*word):
            print("you react too late and the moon lord chokes you")
            startTime = time.time()
            three = input("You Die")
        if three == "zennith":
            print("you react fast enough, but he barely looks hurt")
            #time.sleep(2)
            print("the sword starts glowing")
            #time.sleep(2)
            print("there is a button on it")
            #time.sleep(1)
            print("you click it")
            #time.sleep(1)
            print("it makes a familiar of the moon lord")
            #time.sleep(2)
            print("your familiar fights and eventually killed moon lord")
            #time.sleep(2)
            print("a chest appears")
            #time.sleep(2)
            t = input("open it? (y/n)")
            if t == "y":
                print("you open they chest and you don't see anything just some teeth?")
                #time.sleep(2)
                print("IT'S A MIMIC")
                print("it bites off your head and you die")
                quit()
            else:
                print("you leave the dungeon and you get nothing")
                endm()
    def rm4():
        print("Dungeon Master: How did you escape the eye? No one ever has before")
        #time.sleep(2)
        print("Dungeon Master: It was destined that one day someone could stop Chthulu")
        print("No No theres no way")
        x = input("Dungeon Master: Son?")
        if x == "y":
            print("Dungeon Master: I knew it")
        else:
            print("then you must die")
            print("he shoots you with the M2 Browning Machine Gun")
            quit()
        print("he attacks you but before he hits you a light blue beam comes out of the darkness and cuts his head off")
        #time.sleep(3)
        print("Dungeon masters disembodied head: TAKE WHAT'S IN MY POCKET")
        inventory.append(str('zennith'))
        #time.sleep(1)
        print("you take what in his pocket and you feel it's energy run through you")
        #time.sleep(2)
        print("you start to hover and the ground below you crubmbles revelaing the final room")
        finalfight()

    #end room functions
    def inv():
        print(*inventory)
        print(gold)
    os.system("clear")
    def intro():
        global gold
        print("Dungeon Master: Welcome to my Dungeon")
        #time.sleep(3)
        print("Dungeon Master: This is the hardest Dungeon are you sure you want to continue?")
        #time.sleep(4)
        w = input("y/n? ")
        if w == "y":
            print("Ok then lets continue")
            print(f"{Fore.RED}You lose 500G{Fore.WHITE}")
            gold -= 500
        else:
            print("THEN DIE")
            #time.sleep(2)
            print("you feel your throat close and you die")
            quit()
    intro()
    def AmorWe():
        print("You walk into a room and you see many bodies on the ground and some have weapons some have amulets")
        c = int(input("which one would you like to steal from? amulets (1) or weapons (2) "))
        if c == 1:
            global a
            a = int(input("which one there is 6 bodies (type a number 1-6) "))
        elif c == 2:
            global s
            s = int(input("which one there is 3 bodies with weapons (type a number 1-3) "))
        else:
            print("nope")
    AmorWe()
    def items():

        if a == 4:
            inventory.append(str('low-power-amulet'))
            print("You Aquired a low powered amulet")
        elif s == 3:
            inventory.append(str('basic-sword'))
            print("You Aquired a basic sword")
        else:
            print("you get nothing")
    items()
    def cont():
        #os.system("clear")
        print("would you like to continue")
        print("y/n? ")
        #time.sleep(2)
        print("ha you don't get a choice you have to continue")
        #time.sleep(2)
        print("you get forced into the next room")
        print("the door slams behind you")
        #time.sleep(2)
        print("Old Woman: I've been expecting you")
        #time.sleep(3)
        print("In this room you need to either use your magic or your sword")
        #time.sleep(4)
        print("Or if you have nothing you may try to spare the monster")
        #time.sleep(3)
        print("a monster drops from the celling")
    cont()
    
    global x
    def fight():
        if input("Fight? y/n ") == "y":
            if 'low-power-amulet' or 'basic-sword' in str(*inventory):
                print("you attack the monster ")
                #time.sleep(1)
                print("you damage the monster he looks very wounded")
                print("he attacks what do you do")
            else:
                print("sorry you can't attack it")
        else:
                print("sorry you can't attack it")
    fight()
    def options2():
        global gold
        options1 = [
        'd'
        ]
        word = random.choices(options1)
        startTime = time.time()
        one = input("You have 2 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 2 or one != str(*word):
            print("you react too late and the monster stabs you")
            startTime = time.time()
            one = input("You Die")
            break
        if one == 'd':
            print("you dodge the monster but he attacks again")
            options2 = [
        'd', 'b'
        ]
        word = random.choices(options2)
        startTime = time.time()
        two = input("You have 2 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 2 or two != str(*word):
            print("you react too late and the monster stabs you")
            startTime = time.time()
            two = input("You Die")
        if two == 'd' or 'b':
            print("you dodge again")
            #time.sleep(2)
            print("he attacks again!")
        options3 = [
        
        ]
        if "mace" in str(inventory):
            options3.append(str('mace'))
        word = random.choices(options3)
        startTime = time.time()
        print("you see the oppurtunity to attack")
        three = input("You have 3 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 3 or three != str(*word):
            print("you react too late and the monster stabs you")
            startTime = time.time()
            three = input("You Die")
        if three == "mace":
            print("you react fast enough, you bash the monsters skull and it drops to the ground")
            #time.sleep(2)
            print("the eye that's following you tries to zap you")
            #time.sleep(2)
        options4 = [
        'dodge'
        ]
        word = random.choices(options4)
        startTime = time.time()
        seven = input("You have 4 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 4 or seven != str(*word):
            print("you react too late and the monster stabs you")
            startTime = time.time()
            seven = input("You Die")
        if seven == 'dodge':
            print("you dodge the eye, run to the next room and slam the door behind you")
            rm4()
    def options():
        global gold
        opt = [
            'dodge'
        ]
        if 'basic-sword' in str(*inventory):
            opt.append(str('parry'))
        if 'low-power-amulet' in str(*inventory):
            opt.append(str('shield'))
        word = random.choices(opt)
        startTime = time.time()
        one = input("You have 6 seconds to type: {}\n".format(*word))
        #where the functions go

        while time.time() - startTime > 6 or one != str(*word):
            print("you react too late and the monster slits your throat")
            startTime = time.time()
            one = input("You Die")
            break
        if one == 'parry':
            print("you parry and cut the monster's head off")
            print("You got 20 gold")
            gold += 20
            #time.sleep(3)
            smrm()
        elif one == 'shield':
            print("you block and you zap the monster with lightning and it desintigrates")
            print("You got 20 gold")
            gold += 20
            #time.sleep(3)
            smrm()
        else:
            print("you protect yourself from death and run away")
            #time.sleep(3)
            smrm()
    options()
   
    #everything past this comment needs to stay last
    while True:
        move = input().lower().split()
        if move[0] == "inv":
            inv()
        break
    #os.system("clear")