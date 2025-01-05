# This is the main file for the treasure room challenge
# Author: Jules

from the_pere_fouras_challenge import load_riddles
import random

def treasure_room():
    tv_game = load_riddles("TRClues.json")
    year = random.choice(list(tv_game["Fort Boyard"].keys()))
    show = random.choice(list(tv_game["Fort Boyard"][year].keys()))
    clues = tv_game["Fort Boyard"][year][show]["Clues"]
    print("The clues are: ",clues[0]," ",clues[1]," ",clues[2])
    print(tv_game["Fort Boyard"][year][show]["Clues"])
    attempt_correct = False
    attempt_counter = 3
    nbr = 2
    while attempt_correct == False and attempt_counter > 0:
        answer = str(input("Your answer: ")).lower()
        if answer == tv_game["Fort Boyard"][year][show]["CODE-WORD"].lower():
            print(tv_game["Fort Boyard"][year][show]["CODE-WORD"])
            attempt_correct = True
        else:
            attempt_counter -= 1
            if attempt_counter > 0:
                nbr += 1
                print("Wrong! You have ",attempt_counter," attempts left")
                print("The new clue is ", clues[nbr])


import graphics.objects as obj
from Utils import *
import pygame
def final_challenge(players):
    w = obj.Win()
    w.loadImage(parchemin)
    title = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/6, 20, 20, "The Final Challenge")
    title.alignment = obj.CENTER
    w.add(title)
    desc = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/4, 20, 20, "Find the code word using the given clues")
    desc.alignment = obj.CENTER
    w.add(desc)
    attempt = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 20, 20, "Attempts left: 3")
    w.add(attempt)
    text_clues = obj.Label(obj.WIN_WIDTH/6, obj.WIN_HEIGHT/1.75, 20, 20, "The clues are: ")
    w.add(text_clues)
    box_code = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 600, 100)
    box_code.hide_bg = True
    box_code.borderWidth = 5
    box_code.radius = 10
    w.add(box_code)
    code_text = obj.Label(obj.WIN_WIDTH/1.35, obj.WIN_HEIGHT/1.75, 0, 0, "")
    w.add(code_text)
    button_submit = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.20, 200, 100)
    button_submit.borderWidth = 5
    button_submit.radius = 10
    button_submit.hide_bg = True
    w.add(button_submit)
    submit_text = obj.Label(0, 0, 200, 100, "Submit")
    button_submit.add(submit_text)
    tvgame = load_riddles("TRClues.json")
    year = random.choice(list(tvgame["Fort Boyard"].keys()))
    show = random.choice(list(tvgame["Fort Boyard"][year].keys()))
    clues = tvgame["Fort Boyard"][year][show]["Clues"]
    code = tvgame["Fort Boyard"][year][show]["CODE-WORD"]
    nbr_attempts = 3
    for i in range(3):
        text_clues.text += "\n" + clues[i]
    code_hover = False
    found = False
    nuage_backward(w)
    def keyboard_listener():
            for key in range(len(obj.Object.keys)):
                        value = obj.Object.keys[key]
                        if value:
                            if pygame.key.name(key) in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
                                if code_hover:
                                    code_text.text += pygame.key.name(key)
                            elif pygame.key.name(key) == "backspace":
                                if code_hover:
                                    code_text.text = code_text.text[:-1]

                            break
    def code_listener():
        nonlocal code_hover
        if code_hover:
            code_hover = False
        else:
            code_hover = True
    def button_listener():
        nonlocal nbr_attempts, found
        nbr_attempts -= 1
        if code_text.text == code.lower() and not found:
            found = True
            nuage_forward(w)
            winner(True,players)
            pygame.quit()
        elif nbr_attempts > 0 and not found:
            attempt.text = "Attempts left: "+str(nbr_attempts)
            code_text.text = ""
            text_clues.text += "\n" + clues[3+nbr_attempts]
        elif not found:
            found = True
            nuage_forward(w)
            winner(False,players)
            pygame.quit()
    obj.Object.onkeyboard = keyboard_listener
    box_code.onstartfocused = code_listener
    box_code.onendfocused = code_listener
    button_submit.onclick = button_listener
    while True:
        w.updateAll()
def winner(who,players):
    w = obj.Win()
    w.loadImage(parchemin)
    title2 = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/4, 20, 20, "You won the game!")
    title2.alignment = obj.CENTER
    title2.hide = True
    w.add(title2)

    title3 = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/4, 20, 20, "You lost the game!")
    title3.alignment = obj.CENTER
    title3.hide = True
    w.add(title3)

    exit = obj.Label(obj.WIN_WIDTH/2.7, obj.WIN_HEIGHT/1.3, obj.WIN_WIDTH/4, obj.WIN_WIDTH/8, "Exit")
    exit.alignment = obj.CENTER
    exit.loadImage(small_paper)
    w.add(exit)
    scores = obj.Grid(obj.WIN_WIDTH/8, obj.WIN_HEIGHT/3, 1000, 200)
    tab = []
    for i in players:
        tab.append([i["name"],i["keys"]])
    scores.setGrid(obj.convertToGrid(tab))
    w.add(scores)
    if(who):
        title2.hide = False
    else:
        title3.hide = False
    loop1 = True
    nuage_backward(w)
    def exit_listener():
        nonlocal loop1
        if loop1:
            loop1 = False
            nuage_forward(w)
    exit.onclick = exit_listener
    while loop1:
        w.updateAll()
