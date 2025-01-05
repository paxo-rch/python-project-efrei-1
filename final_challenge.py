# This is the main file for the treasure room challenge
# Author: Jules

from the_pere_fouras_challenge import load_riddles
import random

def treasure_room():
    tv_game = load_riddles("TRClues.json")
    year = random.choice(clues["Fort Boyard"].keys())
    show = random.choice(clues["Fort Boyard"][year].keys())
    clues = clues["Fort Boyard"][year][show]["Clues"]
    print("The clues are: ",clues[0]," ",clues[1]," ",clues[2])
    attempt_correct = False
    attempt_counter = 3
    nbr = 2
    while attempt_correct == False and attempt_counter > 0:
        answer = str(input("Your answer: ")).lower()
        if answer == show["CODE-WORD"].lower():
            attempt_correct = True
        else:
            attempt_counter -= 1
            if attempt_counter > 0:
                nbr += 1
                print("Wrong! You have ",attempt_counter," attempts left")
                print("The new clue is ", clues[nbr])