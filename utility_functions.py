import graphics.objects as obj
import pygame
import time
from pygamevideo import Video
import chance_challenges
import math_challenges
import logical_challenges
from Utils import *


def StartMenufunc():

    #set the window name
    pygame.display.set_caption('Fort Boyard Client v1.0')
    #set the window icon
    programIcon = pygame.image.load('titrefort.png')
    pygame.display.set_icon(programIcon)
    w = obj.Win()
    video = Video("genrique.mp4")
    video.play(True)
    #hide the main window background
    w.hide_bg = True
    #create a box for the image the PRESS SPACE TO PLAY
    text = obj.Box(obj.WIN_WIDTH/3.4, obj.WIN_HEIGHT/1.5, 600, 200)
    #hide the box
    text.transparent = True
    #load the image	
    text.loadImage("parchemin_menu.png")
    #add the PRESS SPACE TO PLAY box to the window
    w.add(text)
    #create a box for the title
    titlebox = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/10, 500, 400)
    #hide the box
    titlebox.transparent = True
    #load the image
    titlebox.loadImage("titrefort.png")
    w.add(titlebox)
    animation = True
    def KeyboardListener():
        nonlocal animation
        if pygame.key.get_pressed()[pygame.K_SPACE] and animation:
            animation = False
            nuage_forward(w,video)
            video.stop()
            video.release()
            Introduction()
    #set the keyboard listener
    obj.Object.onkeyboard = KeyboardListener
    def StartMenuAnimation(video,text):

        video.draw_to(obj.gui, (0, 0))
        if time.time() % 1 > 0.5:

            text.loadImage("parchemin_menu.png")
        else:

            text.unloadImage()

    while True: 

        StartMenuAnimation(video,text)
        w.updateAll()
    


def Introduction():

    w = obj.Win()
    Intro_Skiped = False
    text_done = False
    button_skip = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_skip.borderWidth = 5
    button_skip.radius = 10
    button_skip.hide_bg = True
    skip_text = obj.Label(0, 0, 200, 100, "Skip")
    button_skip.add(skip_text)
    w.add(button_skip)
    w.loadImage("parchemin.jpg")

    def button_listener():

        nonlocal Intro_Skiped, text_done
        if skip_text.text == "Skip":

            Intro_Skiped = True
        if text_done:

            text_done = False
            nuage_forward(w)
            PlayerCount()
    button_skip.onclick = button_listener
    nuage_backward(w)
    text_intro = "Welcome to you young adventurers\nAre you looking for glory, power and wealth?\nYou are in the right place.\nHere you can get everything you want,\nbut for that you will have to succeed in the tests\nchosen by the master of the game\nGood luck!"
    label_intro = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 15, 15,"")
    w.add(label_intro)

    for i in text_intro:

        label_intro.text += i
        time.sleep(0.05)
        w.updateAll()
        if Intro_Skiped:

            label_intro.text = text_intro
            break

    skip_text.text = "Continue"
    text_done = True

    while True:

        w.updateAll()


def PlayerCount():
    global counter
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    count_text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choose the number of players")
    counter = 1
    counter_box = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 400, 200)
    counter_box.hide_bg = True
    counter_box.borderWidth = 5
    counter_box.radius = 10
    w.add(counter_box)
    number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "1")
    w.add(number_text)
    plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
    plus_box.hide_bg = True
    plus_box.borderWidth = 5
    plus_box.radius = 10
    w.add(plus_box)
    plus_text = obj.Label(counter_box.x+counter_box.w/1.25, counter_box.y+counter_box.h/1.75, 0, 0, "+")
    w.add(plus_text)
    minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
    minus_box.hide_bg = True
    minus_box.borderWidth = 5
    minus_box.radius = 10
    w.add(minus_box)
    minus_text = obj.Label(counter_box.x+counter_box.w/4, counter_box.y+counter_box.h/1.75, 0, 0, "-")
    w.add(minus_text)
    w.add(count_text)

    nuage_backward(w)

    def CounterListenerPlus():
        global counter
        nonlocal number_text
        if counter < 3:

            counter += 1
            number_text.text = str(counter)

    def CounterListenerMinus():
        global counter
        nonlocal number_text
        if counter > 1:

            counter -= 1
            number_text.text = str(counter)

    def button_listener():

        nonlocal continuer
        if continuer:

            continuer = False
            nuage_forward(w)
            Compose_Equipe(counter)

    continuer = True
    plus_box.onclick = CounterListenerPlus
    minus_box.onclick = CounterListenerMinus
    button_continuer.onclick = button_listener
    while True:

        w.updateAll()

def Compose_Equipe(nbr):
    global players
    nbr_joueurs = nbr+1
    players = []
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    texte = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choose player 1 informations")
    w.add(texte)
    box_name = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 600, 100)
    box_name.hide_bg = True
    box_name.borderWidth = 5
    box_name.radius = 10
    w.add(box_name)
    name_text = obj.Label(obj.WIN_WIDTH/1.35, obj.WIN_HEIGHT/1.75, 0, 0, "")
    w.add(name_text)
    box_profession = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/1.5, 600, 100)
    box_profession.hide_bg = True
    box_profession.borderWidth = 5
    box_profession.radius = 10
    w.add(box_profession)
    profession_text = obj.Label(obj.WIN_WIDTH/1.35, obj.WIN_HEIGHT/1.35, 0, 0, "")
    w.add(profession_text)
    box_leader = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/1.2, 100, 100)
    box_leader.hide_bg = True
    box_leader.borderWidth = 5
    box_leader.radius = 100
    box_leader.backgroundColor = obj.BLACK
    w.add(box_leader)
    text_leader = obj.Label(obj.WIN_WIDTH/2.4, obj.WIN_HEIGHT/1.1, 0, 0, "Leader")
    w.add(text_leader)
    text_profession = obj.Label(obj.WIN_WIDTH/2.4, obj.WIN_HEIGHT/1.35, 0, 0, "Job")
    w.add(text_profession)
    text_name = obj.Label(obj.WIN_WIDTH/2.4, obj.WIN_HEIGHT/1.7, 0, 0, "Name")
    w.add(text_name)
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.20, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    w.add(button_continuer)
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    nuage_backward(w)
    leader = False
    name_hover = False
    job_hover = False
    def keyboard_listener():
            for key in range(len(obj.Object.keys)):
                        value = obj.Object.keys[key]
                        if value:
                            if pygame.key.name(key) in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
                                if name_hover:
                                    name_text.text += pygame.key.name(key)
                                else:
                                    profession_text.text += pygame.key.name(key)
                            elif pygame.key.name(key) == "backspace":
                                if name_hover:
                                    name_text.text = name_text.text[:-1]
                                else:
                                    profession_text.text = profession_text.text[:-1]
                            break

    def name_listener():
        nonlocal name_hover
        if name_hover:
            name_hover = False
        else:
            name_hover = True
    def job_listener():
        nonlocal job_hover
        if job_hover:
            job_hover = False
        else:
            job_hover = True
    def checkbox_listener():
        nonlocal leader
        if leader == False:
            leader = True
            box_leader.hide_bg = False
        else:
            leader = False
            box_leader.hide_bg = True
    def button_listener():
        nonlocal nbr, leader
        nbr -= 1
        players.append({"name":name_text.text,"profession":profession_text.text,"leader":leader,"key":0})
        if nbr > 0:
            name_text.text = ""
            profession_text.text = ""
            leader = False
            box_leader.hide_bg = True
            texte.text = "Enter player "+str(nbr_joueurs-nbr) + " informations"
    obj.Object.onkeyboard = keyboard_listener
    box_name.onstartfocused = name_listener
    box_name.onendfocused = name_listener
    box_leader.onclick = checkbox_listener
    box_profession.onstartfocused = job_listener
    box_profession.onendfocused = job_listener
    button_continuer.onclick = button_listener
    while nbr != 0:
        w.updateAll()
    leaded = False
    for i in players:
        if i["leader"] == True:
            leaded = True
            break
    if leaded == False:
        players[0]["leader"] = True
    nuage_forward(w)
    ChallengeMenu()
def ChallengeMenu():
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    texte = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/4, 0, 0, "Choose the challenge")
    w.add(texte)
    math_button = obj.Box(obj.WIN_WIDTH/2.3, obj.WIN_HEIGHT/3, 200, 100)
    math_button.borderWidth = 5
    math_button.radius = 10
    math_button.hide_bg = True
    w.add(math_button)
    math_texte = obj.Label(obj.WIN_WIDTH/1.95, obj.WIN_HEIGHT/2.5, 0, 0, "Math")
    w.add(math_texte)
    logic_button = obj.Box(obj.WIN_WIDTH/2.3, obj.WIN_HEIGHT/2, 200, 100)
    logic_button.borderWidth = 5
    logic_button.radius = 10
    logic_button.hide_bg = True
    w.add(logic_button)
    logic_texte = obj.Label(obj.WIN_WIDTH/1.95, obj.WIN_HEIGHT/1.75, 0, 0, "Logic")
    w.add(logic_texte)
    #logic_button.onclick = logic_challenge
    chance_button = obj.Box(obj.WIN_WIDTH/2.3, obj.WIN_HEIGHT/1.5, 200, 100)
    chance_button.borderWidth = 5    
    chance_button.radius = 10
    chance_button.hide_bg = True
    w.add(chance_button)
    chance_texte = obj.Label(obj.WIN_WIDTH/1.95, obj.WIN_HEIGHT/1.35, 0, 0, "Gambling")
    w.add(chance_texte)
    perefourras_button = obj.Box(obj.WIN_WIDTH/2.3, obj.WIN_HEIGHT/1.2, 200, 100)
    perefourras_button.borderWidth = 5    
    perefourras_button.radius = 10
    perefourras_button.hide_bg = True
    w.add(perefourras_button)
    perefourras_texte = obj.Label(obj.WIN_WIDTH/1.95, obj.WIN_HEIGHT/1.1, 0, 0, "Riddle")
    w.add(perefourras_texte)
    #perefourras_button.onclick = perefourras_challenge
    nuage_backward(w)
    animation = True
    def chance_listener():
        nonlocal animation
        if animation:
            animation = False
            nuage_forward(w)
            PlayerChoice("luck")
    def math_listener():
        nonlocal animation
        if animation:
            animation = False
            nuage_forward(w)
            PlayerChoice("math")
    def logic_listener():
        nonlocal animation
        if animation:
            animation = False
            nuage_forward(w)
            PlayerChoice("logical")
    math_button.onclick = math_listener
    chance_button.onclick = chance_listener
    logic_button.onclick = logic_listener
    while True:
        w.updateAll()
def PlayerChoice(game):

    w = obj.Win()
    w.loadImage("parchemin.jpg")
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    count_text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choose the player")
    count = 1
    counter_box = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 400, 200)
    counter_box.hide_bg = True
    counter_box.borderWidth = 5
    counter_box.radius = 10
    w.add(counter_box)
    number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "1")
    w.add(number_text)
    plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
    plus_box.hide_bg = True
    plus_box.borderWidth = 5
    plus_box.radius = 10
    w.add(plus_box)
    plus_text = obj.Label(counter_box.x+counter_box.w/1.25, counter_box.y+counter_box.h/1.75, 0, 0, "+")
    w.add(plus_text)
    minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
    minus_box.hide_bg = True
    minus_box.borderWidth = 5
    minus_box.radius = 10
    w.add(minus_box)
    minus_text = obj.Label(counter_box.x+counter_box.w/4, counter_box.y+counter_box.h/1.75, 0, 0, "-")
    w.add(minus_text)
    w.add(count_text)

    nuage_backward(w)

    def CounterListenerPlus():

        nonlocal count, number_text
        if count < counter:

            count += 1
            number_text.text = str(count)

    def CounterListenerMinus():

        nonlocal count, number_text
        if count > 1:

            count -= 1
            number_text.text = str(count)

    def button_listener():

        nonlocal continuer
        if continuer:

            continuer = False
            nuage_forward(w)
            if game == "luck":
                key_player = chance_challenges.chance_challenge(counter)
                if key_player != 0:
                    players[key_player-1]["key"] += 1
                ChallengeMenu()
            elif game == "math":
                key_player = math_challenges.math_challenge(counter)
                if key_player != 0:
                    players[key_player-1]["key"] += 1
                ChallengeMenu()
            elif game == "logical":
                key_player = logical_challenges.nim_game(counter)
                if key_player != 0:
                    players[key_player-1]["key"] += 1
                ChallengeMenu()

    continuer = True
    plus_box.onclick = CounterListenerPlus
    minus_box.onclick = CounterListenerMinus
    button_continuer.onclick = button_listener
    while True:
        w.updateAll()