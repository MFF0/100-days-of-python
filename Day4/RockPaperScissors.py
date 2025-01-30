import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpc = [rock, paper, scissors]

randIndex = random.randint(0,2)
userChoiceIndex = int(input("Choose rock, paper, or scissors. (0, 1, 2): "))

userChoice = rpc[userChoiceIndex]
computerChoice = rpc[randIndex]

def win(userChoice, computerChoice):
    if (userChoice == 0 and computerChoice == 1):
        return "You Lose!"
    elif (userChoice == 0 and computerChoice == 2):
        return "You Win!"
    elif (userChoice == 1 and computerChoice == 0):
        return "You Win!"
    elif (userChoice == 1 and computerChoice == 2):
        return "You Lose!"
    elif (userChoice == 2 and computerChoice == 0):
        return "You lose!"
    elif (userChoice == 2 and computerChoice == 1):
        return "You Win!"
    else:
        return "Draw!"
    
print(f"Your choice:\n{userChoice}\n ========================================================================================")
print(f"Computer's choice:\n{computerChoice}\n, {win(userChoiceIndex, randIndex)}")