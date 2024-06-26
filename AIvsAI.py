from Flame import *

import random

print("Let's start the game!")
randomKey = random.choice(list(Database.keys()))
randomKey = random.choice(Database[randomKey])
print("First word is {}".format(randomKey))
mvs = 0
while True:
    mvs += 1
    response = Negamax(randomKey[-1], 4, -float('inf'), float('inf'))[1]
    print("AI: {}".format(response))
    History.add(response)
    if response == '':
        print("AI: GG! Game end in {} moves!".format(mvs))
        break
    randomKey = response[-1]
    if not IsInDatabase(response):
        print("AI: GG! Game end in {} moves!".format(mvs))
        break