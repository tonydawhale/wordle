import os
from random import random
import requests

content = requests.get('https://api.github.com/gists/8b382c3c614d9007846635235ae7ff04').json().get('files').get('wordle_word_list.txt').get('content')
content = content.replace("\n", " ")
wordlist = content.split(" ")

os.system("")
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    GRAY = '\33[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{style.BOLD}Welcome to Tony's Wordle Project!\n{style.RESET}")
print(f"Before you start, I will briefly explain the rules and how to play.\n - You will have six tries to guess the word\n - Each guess must be a valid five-letter word\n - After each guess, the color of the tiles will change to show how close your guess was to the word.")
print(f"\nHere are some examples:\n")
print(f"[{style.GREEN}W{style.WHITE}][E][A][R][Y]\nThe letter {style.BOLD}W{style.RESET} is in the word and is in the correct spot.\n")
print(f"[P][{style.YELLOW}I{style.WHITE}][L][L][S]\nThe letter {style.BOLD}I{style.RESET} is in the word but is in the wrong spot.\n")
print(f"[V][A][G][{style.GRAY}U{style.RESET}][E]\nThe letter {style.BOLD}U{style.RESET} is not in the word in any spot.\n")
print(f"If you would like to view a keyboard of letters to see which ones you have used, type {style.BOLD}KEYBOARD{style.RESET}.\n")
print(f"Good luck!{style.RESET}\n")

selectedWord = wordlist[int(random() * len(wordlist))]
guesses: int = 0
won = False
lost = False
usedLetters = []
keyboard = "[Q] [W] [E] [R] [T] [Y] [U] [I] [O] [P]\n [A] [S] [D] [F] [G] [H] [J] [K] [L]\n   [Z] [X] [C] [V] [B] [N] [M]"

while (won != True or lost != True) and guesses < 6:
    guessed = False
    while guessed == False:
        guess = input("Please enter a word > ").lower()
        if guess == "keyboard":
            print(keyboard)
            continue
        if guess not in wordlist:
            print(f"{style.BOLD}{guess.upper()}{style.RESET} is not a valid word!")
            continue
        responseParts = []
        for letterIndex in range(len(guess)):
            if guess[letterIndex] in selectedWord and guess[letterIndex] != selectedWord[letterIndex]:
                responsePart = f"[{style.YELLOW}{guess[letterIndex].upper()}{style.RESET}]"
                keyboard = keyboard.replace(f"[{guess[letterIndex].upper()}]", responsePart)
                responseParts.append(responsePart)
                continue
            if guess[letterIndex] == selectedWord[letterIndex]:
                responsePart = f"[{style.GREEN}{guess[letterIndex].upper()}{style.RESET}]"
                keyboard = keyboard.replace(f"[{guess[letterIndex].upper()}]", responsePart)
                responseParts.append(responsePart)
                continue
            else:
                responsePart = f"[{style.GRAY}{guess[letterIndex].upper()}{style.RESET}]"
                keyboard = keyboard.replace(f"[{guess[letterIndex].upper()}]", responsePart)
                responseParts.append(responsePart)
                continue
        print("".join(responseParts))
        guessed = True
        if guess == selectedWord:
            won = True
            break
    if won == True:
        break
    guesses += 1

if won is True:
    print(f"\nCongratulations you have successfully guessed the word!\nRerun the program if you would like to play again.")
else:
    print(f"Sorry but you have lost. The word was {style.BOLD}{style.UNDERLINE}{selectedWord}{style.RESET}.\nRerun the program if you would like to play again.")