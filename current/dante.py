def dante():
    import random
    from colorama import Fore
    import time
    import os
    inventory = []
    #steven code
    def endd():
     print("You put in your ear buds and start playing the avengers theme song as you walk out of the dungeon.")
    #end steven code
    def smrm():
        print("Once you enter the door you see a small room with a chest and a door.")
        time.sleep(4)
        usr2 = int(input("Would you like to open the chest (1) or continue without opening the chest (2)? "))
        if usr2 == 1:
            print(f"{Fore.GREEN}You have accuired a Strong Sword. {Fore.WHITE}")
            inventory.append(str('strong_sword'))
            print(f"{Fore.YELLOW}You have accuired 10 gold. {Fore.WHITE}")
        else:
            print("You have entered the room without opening the chest.")
    os.system('clear')
    print("Dungeon Guardian: Welcome traveler!")
    time.sleep(3)
    print("Dungeon Guardian: If you would like to enter this dungeon you will have to pay me 250 gold.")
    time.sleep(5)

    global lvl1
    lvl1 = [
        'dodge'
        ]
    def dodge():
    

        word = random.choice(lvl1)
        start_time = time.time()
        global one
        one = input("You have 5 seconds to type: {}\n".format(word))

        while time.time() - start_time > 5 or one != word:
            print("you try to dodge but")
            start_time = time.time()
            one = input("You Die") 
            quit()

    def rm3():
        usr = input("Do you want to enter the door on the left, or the right? ").strip()
        if usr == "right":
            print("You enter a room with a big chest.")
            time.sleep(1)
            usr3 = input("Do you open the chest? y/n ").strip()
            if usr3 == "y":
                print(f"{Fore.GREEN}You have found a Long Sword and a key! {Fore.WHITE}")
                time.sleep(2)
                inventory.append(str('long_sword'))
                inventory.append(str("key"))
                print("I wonder what the key is for?")
                time.sleep(2)
                print("You then turn back and go to the other door.")
            else:
                print("You ignore the chest and you turn back to go the other way.")
        elif usr == "left":
            print("You go to the door on the left and enter the next room.")
            print("Right as you enter the room a monster attacks you!")
            if 'strong_sword' in inventory:
             print("Quick dodge!")
             dodge()


        print("you protect  yourself from death") 
    def death():
        print("You have died nerd now you have to restart loser.")
        quit()

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
        time.sleep(2)
        print("Dungeon Guardian: You can always come back another time.")
        time.sleep(3)
        print("You turn around and leave the dungeon.")
        time.sleep(3)

    print("When you enter the dungeon you find a small room with 4 doors on each side of the room.")
    time.sleep(4)
        
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
    os.system("clear")

    print("When you go through the door you see a small room with 2 doors on both sides of the room.")
    rm3()
    time.sleep(4)

    print("After you get away from the monster and you look around and you see stairs that leed further down into the dungeon.")
    time.sleep(3)
    print("Once you get down the stairs you see two doors.")
    time.sleep(2)
    def rm4():
        x = input("Do you choose the door on the left or the door on the right? right/left ").strip()
        if x == "right":
            if "key" in inventory:
                print("The door is locked.")
                time.sleep(1)
                print(".", time.sleep(1), ".",  time.sleep(1), ".")
                print("Oh right! The key!")
                time.sleep(2)
                print("You insert the key and it is a perfect fit and the door is now unlocked.")
            else:
                print("Looks like the door is locked and you don't have a key.")
                time.sleep(2)
                print("You will need to go to the other door instead.")
                time.sleep(2)
                print("You walk to the other door and open it.")
                time.sleep(1)
                print("Once you open the door you look around and see a chest on the right side.")
                time.sleep(2)
                print("You go to oppen the chest and you find 25 gold and a key!")
                time.sleep(1)
                print(f"{Fore.YELLOW}+25G {Fore.WHITE}")
                if "key" in inventory:
                    print("You already have a key so you don't need this key.")
                else:
                    print(f"{Fore.GREEN}You have accuired a a key! {Fore.WHITE}")
                    inventory.append(str('key'))
                    time.sleep(2)
                    print("Let's try the other door.")
                    time.sleep(1)
                    print("You try to open the door but it is locked, but you have a key so you unlock it and enter the next room.")
        elif x == "left":
            print("Once you open the door you look around and see a chest on the right side.")
            time.sleep(2)
            print("You go to oppen the chest and you find 25 gold and a key!")
            time.sleep(1)
            print(f"{Fore.YELLOW}+25G {Fore.WHITE}")
            if "key" in inventory:
                print("You already have a key so you don't need this key.")
            else:
                print(f"{Fore.GREEN}You have accuired a a key! {Fore.WHITE}")
                inventory.append(str('key'))
                time.sleep(2)
                print("Let's try the other door.")
                time.sleep(1)
                print("You try to open the door but it is locked, but you have a key so you unlock it and enter the next room.")
        os.system("clear")
    rm4()

    print("Right as soon as you enter the room you get attaked by a monster from above!")
    time.sleep(0.5)
    print("Quick dodge it!")
    time.sleep(0.5)
    dodge()
    
    print("Just after you dodged the monster you look back and a bunch of monsters start chasing you.")
    time.sleep(2)
    print("You start runing as fast as you can.")
    time.sleep(1)
    print("as you are running down the halls you come to a split in the hall.")
    time.sleep(2)

    def dec():
        y = input("Do you go left or do you go right? ")
        if y == "l":
            print("You turn the corner and you trip on a wire that was on the ground and it activates a trap.")
            time.sleep(3)
            print("The floor moves and a pit of spikes is bellow.")
            time.sleep(1)
            death()
        else:
            print("You turn the corner and you see a door.")
            time.sleep(1)
            print("You run up to the door and slam it oppen.")
            time.sleep(1)
            print("You quickly turn around, slam the door closed.")
            time.sleep(1)
            print("You reach in your pocket and grab your key, you then lock the door.")
            time.sleep(1)
            print("Good job, you have escaped the monsters.")
            os.system('clear')
    dec()

    print("After you catch your breath you look around and see a big door with a chest next to the door.")
    time.sleep(2)
    def ch():
        t = input("Do you want to open the chest? y/n ")
        if t == "y":
            print("You walk over to the chest and you open it.")
            time.sleep(2)
            print(f"{Fore.GREEN}You found a giant key! {Fore.WHITE}")
        else:
            print("You did not open the chest and now you feel like you are expanding.")
            time.sleep(2)
            print("You ignor it and start walking to the door.")
            time.sleep(2)
            print("As you touch the door you vilontly explode in to small pieces.")
            death()
    ch()
    print("You start to insirt the giant key into the door.")
    time.sleep(2)
    print("You unlock the door and you push the door wide open.")
    time.sleep(2)
    print("As you walk into the final room a giant monster comes out from the shaddows.")
    time.sleep(2)
    print("???: Welcome to my home.")
    time.sleep(1)
    print("You charge towards the monster while pulling out your sword.")
    time.sleep(2)
    print("You swing as hard as you can and you make a big cut on his stomach.")
    time.sleep(2)
    print("???: Ouchie!")
    time.sleep(1)
    print("???: Here take this, just leave me alone!!")
    print(f"{Fore.YELLOW}+1000G {Fore.WHITE}")
    time.sleep(2)
    print("The monster runs away and you leave the dungeon.")
    time.sleep(2)
    endd()


    #everything after this stays at the end
    while True:
        move = input().lower().split()

        if move[0] == "inv":
            print(*inventory)
            break
    os.system('clear')