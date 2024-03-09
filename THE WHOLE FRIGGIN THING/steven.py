from michael import michael
from dante import dante
from ian import ian
import random
from colorama import Fore
import time
import os
os.system("clear")
print ("Shopkeeper: Hello traveler, you must be tired")
#This is temporary --> time.sleep(3)
print ("Shopkeeper: I have three options for you as you start this new adventure")
#time.sleep(4)
print("Shopkeeper: The first option is the luxury life style. (high risk high reward)")
#time.sleep(4)
print("Shopkeeper: The second is the middle class. (medium risk medium reward)")
#time.sleep(4)
print("Shopkeeper: And the third is kill your self becase you are poor. (low risk crappy reward)")
#time.sleep
choose = int(input("Choose your quest high risk (1) medium risk (2) low risk (3) "))
if choose == 1:
    michael() #finish rm2
elif choose == 2:
    dante()
elif choose == 3:
    ian()


