import random
import time

lvl1 = [
 'dodge', 'block', 'parry'
]

word = random.choice(lvl1)
start_time = time.time()
one = input("You have 3 seconds to type: {}\n".format(word))

while time.time() - start_time > 3 or one != word:
    print("Wrong!")
    start_time = time.time()
    one = input("You Die") 
    break
print("you protect  yourself from death") 