#Task1
import random

def flip():
    HT = ['Heads', 'Tails']
    randIndex = random.randint(0,1)
    return HT[randIndex]

print(flip())