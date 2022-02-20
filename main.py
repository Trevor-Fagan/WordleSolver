# Wordle Solver

import random

list_of_words = []

opening_guess = "crane"

in_the_ans = []
in_correct_place = [" ", " ", " ", " ", " "]
letter_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
def NextGuess(res):
    global list_of_words
    next_guess = ""

    if num_guesses < 2:
        return opening_guess

    ## THIS AREA IN PROGRESS ##
    itr = 0
    for key in res[0]: # for each letter in dictionary
        if res[0][key] == "Green": # If its in the right place
            for word in list_of_words:
                if word[itr] != key:
                    list_of_words.remove(word)
        itr += 1

    ## IN PROGRESS END ##

    if len(list_of_words) > 1:
        next_guess = list_of_words[random.randint(0, len(list_of_words) - 1)]
    else:
        next_guess = list_of_words[0]

    return next_guess



# Main Wordle Code
res = ""
while user_guess != the_word and num_guesses < 6:
    my_next_guess = NextGuess(res)
    print(len(list_of_words), my_next_guess)
    user_guess = NextGuess(res)

    res = Guess(user_guess, num_guesses)
    num_guesses = res[1]

if found:
    print("Congrats! Word found in ", num_guesses, "guesses!")
else:
    print("Sorry, maybe next time!")
