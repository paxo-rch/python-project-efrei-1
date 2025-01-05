# This is the main file for the pere fouras challenge
# Authors: Jules for the no-gui part, Gabriel for the gui

import json
import random

def load_riddles(file):
    with open(file,"r") as f:
        riddles = json.load(f)
    return riddles

def pere_fouras_riddles():
    riddles = load_riddles("PFRiddles.json")
    riddle = random.choice(riddles)
    while riddle["type"] != "Key":
        riddle = random.choice(riddles)
    attempt = 3
    while attempt > 0:
        print("Riddle: ",riddle["question"])
        answer = str(input("Your answer: ")).lower()
        if answer == riddle["answer"].lower():
            print("Correct! You win a key")
            return True
        attempt -= 1
        if attempt > 0:
            print("Wrong! You have ",attempt," attempts left")
        else:
            print("You lost the game, the answer was: ",riddle["answer"])
            return False

### Version with the GUI

from graphics.objects import *  # This import is likely from a custom graphics library
import math
from time import *
from Utils import *

from the_pere_fouras_challenge import load_riddles
import random
from graphics.objects import *
from time import *
from Utils import *

def pere_fouras_riddles(player):
    # Loads riddles from a JSON file.
    riddles = load_riddles("PFRiddles.json")
    # Selects a random riddle of type "Key".
    riddle = random.choice(riddles)
    while riddle["type"] != "Key":
        riddle = random.choice(riddles)

    attempt = 3
    game_over = False

    win = Win()
    win.loadImage(parchemin)

    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Pere Fouras Challenge")
    title.alignment = CENTER
    win.add(title)

    # Create a label to display the question.
    question_label = Label(WIN_WIDTH/2, WIN_HEIGHT/2, 20, 20, "")
    question_label.alignment = CENTER
    win.add(question_label)

    # Create a box for user input.
    input_box = Box(WIN_WIDTH/3, WIN_HEIGHT/1.5, WIN_WIDTH/3, 100)
    input_box.hide_bg = True
    input_box.borderWidth = 5
    input_box.radius = 10
    win.add(input_box)

    # Create a label to display user input.
    input_label = Label(input_box.x + input_box.w/2, input_box.y + input_box.h/2, 20, 20, "")
    input_label.alignment = CENTER
    win.add(input_label)

    # Create a button to submit the answer.
    submit_button = Box(WIN_WIDTH/1.3, WIN_HEIGHT/1.25, 200, 100)
    submit_button.borderWidth = 5
    submit_button.radius = 10
    submit_button.hide_bg = True
    submit_text = Label(0, 0, 200, 100, "Submit")
    submit_button.add(submit_text)
    win.add(submit_button)

    # Function to handle answer submission
    def submit_answer():
        nonlocal attempt, game_over, result
        answer = input_label.text.lower()
        input_label.text = ""

        if answer == riddle["answer"].lower():
            print("Correct! You win a key")
            title.text = "Correct! You win a key"
            game_over = True
            result = True
        else:
            attempt -= 1
            if attempt > 0:
                print("Wrong! You have ", attempt, " attempts left")
                title.text = "Wrong! You have " + str(attempt) + " attempts left"
            else:
                print("You lost the game, the answer was: ", riddle["answer"])
                title.text = "You lost the game, the answer was: " + riddle["answer"]
                game_over = True
                result = False

    # Function to handle user input from the keyboard.
    def keyboard_listener():
        nonlocal input_label
        for key in range(len(Object.keys)):
            value = Object.keys[key]
            if value:
                if pygame.key.name(key) in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]:
                    input_label.text += pygame.key.name(key)
                elif pygame.key.name(key) == "backspace":
                    input_label.text = input_label.text[:-1]
                elif pygame.key.name(key) == "space":
                    input_label.text = input_label.text + " "
                break

    Object.onkeyboard = keyboard_listener
    submit_button.onclick = submit_answer
    question_label.text = riddle["question"]
    nuage_backward(win)
    result = None

    while not game_over:
        win.updateAll()

    sleep(2)
    nuage_forward(win)
    if result:
        return player
    else:
        return 0

