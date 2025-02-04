import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

# TODO-4: Create a "placeholder" with the same number of blanks as the chosen_word

# TODO-5: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

chosen_word = word_list[random.randint(0,2)]
print(chosen_word)

placeholder = []
for letter in chosen_word:
    placeholder.append("_")
    
print(placeholder)
    
guess = input("Guess a letter: ").lower()

def check_letter(guess):
    if(chosen_word.find(guess) == True):
        print("Right")
    else:
        print("Wrong")
        
check_letter(guess)
