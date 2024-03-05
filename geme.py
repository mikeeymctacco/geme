#you 'go' directions and you find 3 items and if you have all of the items when you get to a certin room you win there is another place you can go and its basically just another place where you can move around and collect 3 more items
import os #making console smooth

rooms = {
  'stage1':{
    'Hall':{'south': 'Kitchen','east': 'Danger Room','west':'Study','item': 'key'},
    'Kitchen':{'north': 'Hall','down': 'Dungeon'},
    'Danger Room':{'west': 'Hall','south': 'Driveway','item': 'mummy'},
    'Dungeon':{'west': 'Skeleton Room','item': 'bat'},
    'Skeleton Room':{'east': 'Dungeon','up': 'Stairs','down': 'Trap','item': 'bone'},
    'Trap':{'check': 'ufo'},
    'Stairs':{'down': 'Skeleton Room','north': 'Room of Secrets'},
    'Room of Secrets':{'south': 'Stairs','east': 'Hall','item': 'potion'},
    'Driveway':{'north': 'Hall','item': 'gem'},
    'Study':{'east':'Hall','up':'Room of Secrets','item':'notepad'}
  },
  'stage2':{
    'Plains':{'south':'Castle'},
    'Castle':{'north':'Plains', 'west':'Corridor'},
    'Corridor':{'east':'Castle','west':'Court','north':'Stairs','south':'Banquet Hall','item':'staff'},
    'Court':{'east':'Corridor','south':'Trophy Room'},
    'Trophy Room':{'up':'Throne Room','north':'Court'},
    'Throne Room':{'down':'Trophy Room','secret':'secret','up':'Knight Room','check':'king'},
    'secret':{'check':'ufo'},
    'Banquet Hall':{'north':'Corridor','west':'broom closet','east':'Room Full Of Secrets','item':'food'},
    'Dungeon':{'up':'Stairs','item':'dagger'},
    'Stairs':{'south':'Corridor','down':'Dungeon'},
    'Room Full Of Secrets':{'west':'Banquet Hall','item':'orb_of_power'},
    'broom closet':{'east':'Banquet Hall','item':'king_bone'},
    'Knight Room':{'down':'Throne Room','item':'dagger_of_power'}
  }
} 

def showInstructions(turn): #Instructionsd
  if stage == 'stage1':
    print("Explorartion Game")
    print("=======================================")
  else:
    print("Space Game")
    print("***************************************")
  print("Controls:", turn)
  print("go [North, South, East, West, Up, Down]")
  print("get [item]")
  print("attack [enemy]")
  if 'king' in inventory:
    print("WHY WOULD YOU DO THIS, GAURDS SAVE ME")

def showStatus(): #status
  if stage == 'stage1':
    print("=======================================")
  else:
    print("***************************************")
  print('You are in the ' + currentRoom)     
  #shows the current room
  if True:
    if currentRoom == 'Hall':
      print("You can go South or East or West")
    elif currentRoom == 'Kitchen':
      print("You can go North or Down")  
    if currentRoom == 'Dungeon':
      print("You can go West")
    if currentRoom == 'Danger Room':
      print("You can go West or South") 
    if currentRoom == 'Skeleton Room':
      print("You can go Down or East")
    if currentRoom == 'Trap':
      print("You are trapped")
    if currentRoom == 'Stairs':
      print("You can go North or Down")
    if currentRoom == 'Room of Secrets':
      print("You can go South or East")
    if currentRoom == 'Driveway':
      print("You can go North")
    if currentRoom == 'Study':
      print("You can go East")
    if currentRoom == 'Kitchen': 
      print("going somewhere?")
    if currentRoom == 'Room of secrets': 
      print("No don/'t go in there!")  
    if currentRoom == 'Skeleton Room': 
      print("Why are you here?") 
    if currentRoom == 'Driveway':
      print("idiot")
    if currentRoom == 'Stairs':
      print("im bored")
    if currentRoom == 'Trap':
      print("Imagine being trapped")

  print('Inventory:')
  print(*inventory)
  if "item" in rooms[stage][currentRoom]:
    print('You see a ' + rooms[stage][currentRoom]['item'])
  if "check" in rooms[stage][currentRoom]:
    print('You see a ' + rooms[stage][currentRoom]['check'])
  if stage == 'stage1':
    print("=======================================")
  else:
    print("***************************************")
  print('What would you like to do?')
  
print("YOU HAVE MADE A MISTAKE TRYING TO BREAK INTO MY HOUSE")
print("YOU WILL NOW PAY WITH YOUR LIFE")
#print("Although you could appease me by getting x items")

stage = 'stage1'
currentRoom = 'Hall'
inventory = [] 
turn = 0
end = ''

while True:
  if 'mummy' in inventory:
    print('you failed to catch the mummy','#Don\'t grab the mummy')
    break

  if currentRoom == 'Driveway': #checking to see if the game has ended
    if 'key' not in inventory:
      print('you are missing the key')
    elif 'potion' not in inventory:
      print('you are missing the potion')
    elif 'gem' not in inventory:
      print('you are missing the gem')
    else:
      print("you escape with your life but realize that the Adventure you went on could have been avoided by breaking in through the driveway")
      print("You could have gotten The Orb Of POWER, And the Dagger Of Superioraty, And Last But Certenly Not Least THE BONE!!!!")#end
      break

  if currentRoom == 'Study': #checking to see if the game has ended
    if 'king_bone' not in inventory:
      print('you are missing the king bone')
    elif 'dagger_of_power' not in inventory:
      print('you are missing the dagger of power')
    elif 'orb_of_power' not in inventory:
      print('you are missing the orb of power')
    else:
      print("i made you not want to go there so you went there reverse psycology")
      w = input("buut  you finally got the items of power who knew that you could do that honestly not be but never the less i will be taking those now")
      break

  if end != '':
    print(end)
    end = ''
    
  showInstructions(turn)
  showStatus()
  move = input().lower().split()
  
  if move[0] == 'go': #going somewhere
    if move[1] in rooms[stage][currentRoom]:
      currentRoom = rooms[stage][currentRoom][move[1]]
    else:
      end = 'There isn\'t a room that way!'

  elif move[0] == 'get': #getting something
    if "item" in rooms[stage][currentRoom]:
      if move[1] in rooms[stage][currentRoom]['item']:
        inventory.append(str(rooms[stage][currentRoom]['item']))
        print('you got a', rooms[stage][currentRoom]['item'])
        del rooms[stage][currentRoom]['item']
      else:
        end = 'Can\'t get ' + move[1] + '!'
    elif "check" in rooms[stage][currentRoom]:
      if 'notepad' in inventory:
        if move[1] in rooms[stage][currentRoom]['check']:
          inventory.append(str(rooms[stage][currentRoom]['check']))
          print('you got a', rooms[stage][currentRoom]['check'])
          if rooms[stage][currentRoom]['check'] == 'king':
            del rooms[stage][currentRoom]['check']
      else:
        end = "Go back and find the notepad"
        currentRoom = 'Dungeon' 
    else:
      end = "There isn't an Item here"

  elif move[0] == 'attack': #attacking something
    if 'bat'in inventory:
      if 'item' in rooms[stage][currentRoom]:
        end = rooms[stage][currentRoom]['item'], 'defeated'
        del rooms[stage][currentRoom]['item']
      elif 'check' in rooms[stage][currentRoom]:
        end = rooms[stage][currentRoom]['check'], 'defeated'
        del rooms[stage][currentRoom]['check']
    if 'dagger' in inventory:
      if 'item' in rooms[stage][currentRoom]:
        end = rooms[stage][currentRoom]['item'], 'defeated'
        del rooms[stage][currentRoom]['item']
      elif 'check' in rooms[stage][currentRoom]:
        end = rooms[stage][currentRoom]['check'], 'defeated'
        del rooms[stage][currentRoom]['check']
    
    else:
      end = 'You don\'t have a weapon'

  elif move[0] == 'pie':
    if 'notepad' not in inventory:
      inventory.append('notepad')
      del rooms['stage1']['Study']['item']
    if stage == 'stage1':
      stage = 'stage2'
      currentRoom = 'Plains'
    else:
      stage = 'stage1'
      currentRoom = 'Hall'
      
  elif move[0] == 'throne':
    if 'notepad' not in inventory:
      inventory.append('notepad')
      del rooms['stage1']['Study']['item']
    stage = 'stage2'
    currentRoom = 'Throne Room'
    
  elif move[0] == 'dun':
    if 'notepad' not in inventory:
      inventory.append('notepad')
      del rooms['stage1']['Study']['item']
    stage = 'stage2'
    currentRoom = 'Dungeon'  
    
  elif move[0] == 'broom':
    if 'notepad' not in inventory:
      inventory.append('notepad')
      del rooms['stage1']['Study']['item']
    stage = 'stage2'
    currentRoom = 'broom closet'
    
  elif move[0] == 'trap':
    #if 'notepad' not in inventory:
      #inventory.append('notepad')
      #del rooms['stage1']['Study']['item']
    stage = 'stage1'
    currentRoom = 'Trap'

  os.system('clear')
  turn += 1

  if 'ufo' in inventory:
    print("You have been transported to a new plane of existence")
    if input("What do you do ") == "die":
      print("Goodnight")
      break
    else:
      if stage == 'stage1':
        stage = 'stage2'
        inventory.pop(-1)
        currentRoom = 'Plains'
        print("Welcome to Ibreon XII.")
      else:
        stage = 'stage1'
        currentRoom = 'Hall'
        inventory.pop(-1)