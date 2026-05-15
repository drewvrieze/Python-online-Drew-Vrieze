#----------------------------
# Name: hangman
# Purpose: create hangman for the final project
#
# Author: DrewV
#
# Created: 05/04/2026
#----------------------------
import random
rng = random.Random()
import os
import sys

# Access the dictionary text file #DONE#
def randomWord(file):
    dictionary = open(file, "r")
    wordlist = dictionary.read().splitlines()
    digit = rng.randrange(len(wordlist))
    word = wordlist[digit]
    dictionary.close()
    return word

def mode():
    while True:
        mode = input("Choose a mode!\n Type e/E for easy.\n Type m/M for medium\n Type h/H for hard\n Type r/R for random\n")
        if mode == "r" or mode == "R":
            return "dictionary.txt"
        if mode == "e" or mode == "E":
            return "dict_easy.txt"
        if mode == "h" or mode == "H":
            return "dict_hard.txt"
        if mode == "m" or mode == "M":
            return "dict_med.txt"
        else:
            print(f"{mode} difficulty does not exist.")


# Create the graphics of the hangman #DONE#
hang1: str = "-----------"
hang2: str = " |      |  "
hang3: str = " |         "
man1: str =  " |     😨  "
man2: str =  " |      |  "
man3: str =  " |     /|  "
man4: str =  " |     /|\\ "
man5: str =  " |     /   "
man6: str =  " |     / \\ "
man7: str =  " |      💀 "

# Display order
def display(part1, part2, part3, hang1, hang2, hang3, wordlist):
    print(hang1)
    print(hang2)
    print(part1)
    print(part2 + "       " + " ".join(wordlist))
    print(part3)
    print(hang3)
    print(hang3)



# Users input of a letter #DONE#
def guess(letters):
    while True:
        guess = input("Guess A Letter: ")
        if guess in letters:
            print("Letter already guessed")
        else:
            if guess.isalpha():
                if len(guess) == 1:
                    guess = guess.lower()
                    return guess, letters
                else:
                    print("Please only type one letter")
            else:
                print("Not Valid Response. (Non-Alpha Guess)")

# check if letter is in word #DONE#
def IsIn(word, guess):
    positions = []
    for i, letter in enumerate(word):
        if letter == guess:
            positions.append(i)
    if positions == []:
        return False
    else:
        return positions
    
# Set up display
def wordDisplay(word):
    pass
    
# Letters guessed #DONE#
def guessed(letters, guess):
    letters.append(guess)
    return letters


# If in word display that letter on the word
def InIt(wordlist, positions, guess):
    for i in positions:
        wordlist[i] = guess


# if not in word do something else, print the correct hangman
def NotIn(wrong, man1, man2, man3, man4, man5, man6, man7, part1, part2, part3):
    if wrong == 1:
        part1 = man1
    if wrong == 2:
        part2 = man2
    if wrong == 3:
        part2 = man3
    if wrong == 4:
        part2 = man4
    if wrong == 5:
        part3 = man5
    if wrong == 6:
        part3 = man6
        part1 = man7
    return part1, part2, part3

    
#parts
def parts(hang3):
    part1 = hang3
    part2 = hang3
    part3 = hang3
    return part1, part2, part3
    
    


# Create the game loop #DONE#
def repeat():
    leave = input("Enter y/Y to try again: ")
    if leave == "y" or leave == "Y":
        main()

# Clear the terminal #DONE#
def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Combine everything into main
def main():
    clearScreen()
    mod = mode()
    word = randomWord(mod)
    wrong = 0
    letters = []
    wordlist = ["_"] *len(word)
    part1, part2, part3 = parts(hang3)
    display(part1, part2, part3, hang1, hang2, hang3, wordlist)
    while True:
        letter, letters = guess(letters)
        clearScreen()
        letters = guessed(letters, letter)
        print(f"Letters Guessed: {letters}")
        positions = IsIn(word, letter)
        if positions == False:
            wrong = wrong + 1
            part1, part2, part3 = NotIn(wrong, man1, man2, man3, man4, man5, man6, man7, part1, part2, part3)
        else:
            InIt(wordlist, positions, letter,)
        display(part1, part2, part3, hang1, hang2, hang3, wordlist)
        if "_" not in wordlist:
            print("Congrats! You solved the hangman!")
            break
        if wrong == 6:
            print(f"The word was {word}")
            break
    repeat()
    
# Make it by level

#DONE#
if __name__ == "__main__":
    main()