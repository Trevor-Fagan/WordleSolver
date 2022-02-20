# Wordle Solver

import random

list_of_words = []

opening_guess = "crane"

in_the_ans = []
in_correct_place = [" ", " ", " ", " ", " "]

# Initialize Wordle
with open('list_of_words.txt','r') as f:
    for line in f:
        for word in line.split():
           list_of_words.append(word) 

# Recreation of Wordle
the_word = list_of_words[random.randint(0, len(list_of_words))]
user_guess = ""
found = False
num_guesses = 0


def Guess(guess, num_guess):
    result = {}
    for letter in range(len(guess)):
        if guess[letter] in the_word:
            if guess[letter] == the_word[letter]:
                result[guess[letter]] = "Green"
            else:
                result[guess[letter]] = "Yellow"
        else:
            result[guess[letter]] = "Gray"
    
    num_guess += 1

    return [result, num_guess]

# Solving Wordle
def Solve(response):
    pass

# Main Wordle Code
while user_guess != the_word and num_guesses < 6:
    user_guess = input("Guess: ")

    res = Guess(user_guess, num_guesses)
    print(res[0])
    num_guesses = res[1]

if found:
    print("Congrats! Word found in ", num_guesses, "guesses!")
else:
    print("Sorry, maybe next time!")
