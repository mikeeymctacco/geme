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
        s = input("Which room Candy?(1) or Warning (2)")
    def rm2():
        os.system("clear")
        print("you go left")
        print("you look around the room and see that there is nothing of intrest")
        print("But you see a rug a desk with some papers on it and 2 more doors")
        #time.slee(1)
        print("oh and a torch")
        #time.sleep
    def rm3():
        os.system("clear")
        print("hi")
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
        global a
        global s
        if a == 4:
                inventory.append(str("low-power-amulet"))
                print(f"{Fore.GREEN}You Aquired a low powered amulet{Fore.WHITE}")
        elif s == 3:
            inventory.append(str("basic-sword"))
            print(f"{Fore.GREEN}You Aquired a basic sword{Fore.WHITE}")
        else:
            print("you get nothing")
    items()
    def cont():
        os.system("clear")
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
            if "low-power-amulet" or "basic-sword" in str(*inventory):
                print("you attack the monster ")
                #time.sleep(1)
                print("you damage the monster he looks very wounded")
                print("he attacks what do you do")
            else:
                print("sorry you can't attack it")
        else:
                print("sorry you can't attack it")
    fight()

    def options():
        global gold
        options = [
        
        ]
        if "basic-sword" in str(*inventory):
            options.append(str("parry"))
        if "low-power-amulet" in str(*inventory):
            options.append(str("shield"))
        word = random.choices(options)
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
            print(f"{Fore.YELLOW}You got 20 gold{Fore.WHITE}")
            gold += 20
            time.sleep(3)
            smrm()
        elif one == 'shield':
            print("you block and you zap the monster with lightning and it desintigrates")
            print(f"{Fore.YELLOW}You got 20 gold{Fore.WHITE}")
            gold += 20
            time.sleep(3)
            smrm()
        else:
            print("you protect yourself from death and run away")
            time.sleep(3)
            smrm()
    options()
    
    #everything past this comment needs to stay last
    while True:
        move = input().lower().split()


        if move[0] == "inv":
            inv()
        break
    #os.system("clear")