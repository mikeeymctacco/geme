import random
import time

lvl1 = [
 'Hi', 'Friend', 'Say', 'Smelly',
 'Made', 'Tree', 'Python', 'Freak'
]

word = random.choice(lvl1)
start_time = time.time()
one = input("You have 3 seconds to type: {}\n".format(word))

while time.time() - start_time > 3 or one != word:
    print("Wrong!")
    start_time = time.time()
    one = input("Try again: ")
print("Correct")