import graphics.objects as obj
import pygame
import utility_functions
import time
from pygamevideo import Video
    
#set the window name
pygame.display.set_caption('Fort Boyard Client v1.0')
#set the window icon
programIcon = pygame.image.load('titrefort.png')
pygame.display.set_icon(programIcon)
#initialize game state variables
running = True
StartMenu = True
Intro = False
Player_Selection = False
Player_Name = False

init_StartMenu = True
init_Intro = False
init_Player_Selection = False
init_Player_Name = False
#main game loop
while running:
    #Start menu
    if StartMenu:
        #initialize the start menu once
        if init_StartMenu:
            #load the background video
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
            #set the keyboard listener
            obj.Object.onkeyboard = KeyboardListener
            init_StartMenu = False
        #function to flicker the PRESS SPACE TO PLAY image
        utility_functions.StartMenu(video,text)
    elif Intro:
        if init_Intro:
            Intro_Skiped = False
            button_skip = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            button_skip.borderWidth = 5
            button_skip.radius = 10
            button_skip.hide_bg = True
            button_skip.transparent = True
            skip_text = obj.Label(0, 0, 200, 100, "Passer")
            button_skip.add(skip_text)
            w.add(button_skip)
            nuage_forward()
            w.hide_bg = False
            w.destroy(titlebox)
            w.destroy(text)
            w.loadImage("parchemin.jpg")
            button_skip.transparent = False
            button_skip.onclick = button_listener
            nuage_backward()
            text_intro = "Bienvenue à vous jeunes aventuriers\nVous recherchez la gloire, le pouvoir et la richesse ?\nVous êtes au bon endroit.\nIci vous pourrez obtenir tous ce que vous désirez,\nmais pour cela il faudra réussir les épreuves choisis par le maitre du jeu\nBonne chance!"
            label_intro = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 15, 15,"")
            w.add(label_intro)
            for i in text_intro:
                label_intro.text += i
                time.sleep(0.05)
                w.updateAll()
                if Intro_Skiped:
                    label_intro.text = text_intro
                    break
            skip_text.text = "Continuer"
            init_Intro = False
    elif Player_Selection:
        if init_Player_Selection:
            button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            button_continuer.borderWidth = 5
            button_continuer.radius = 10
            button_continuer.hide_bg = True
            button_continuer.transparent = True
            continuer_text = obj.Label(0, 0, 200, 100, "Continuer")
            button_continuer.add(continuer_text)
            w.add(button_continuer)
            count_text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choisissez le nombre de joueurs")
            count_text.transparent = True
            counter = 0
            counter_box = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 400, 200)
            counter_box.hide_bg = True
            counter_box.borderWidth = 5
            counter_box.radius = 10
            w.add(counter_box)
            number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "1")
            number_text.transparent = True
            w.add(number_text)
            plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
            plus_box.hide_bg = True
            plus_box.borderWidth = 5
            plus_box.radius = 10
            w.add(plus_box)
            plus_text = obj.Label(counter_box.x+counter_box.w/1.25, counter_box.y+counter_box.h/1.75, 0, 0, "+")
            plus_text.transparent = True
            w.add(plus_text)
            minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
            minus_box.hide_bg = True
            minus_box.borderWidth = 5
            minus_box.radius = 10
            w.add(minus_box)
            minus_text = obj.Label(counter_box.x+counter_box.w/4, counter_box.y+counter_box.h/1.75, 0, 0, "-")
            minus_text.transparent = True
            w.add(minus_text)
            minus_box.transparent = True
            plus_box.transparent = True
            counter_box.transparent = True
            w.add(count_text)
            nuage_forward()
            w.destroy(button_skip)
            w.destroy(label_intro)
            count_text.transparent = False
            minus_box.transparent = False
            plus_box.transparent = False
            plus_text.transparent = False
            minus_text.transparent = False
            number_text.transparent = False
            counter_box.transparent = False
            button_continuer.transparent = False
            plus_box.onclick = CounterListenerPlus
            minus_box.onclick = CounterListenerMinus
            button_continuer.onclick = button_listener
            nuage_backward()
            init_Player_Selection = False
    elif Player_Name:
        if init_Player_Name:
            button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            button_continuer.borderWidth = 5
            button_continuer.radius = 10
            button_continuer.hide_bg = True
            button_continuer.transparent = True
            continuer_text = obj.Label(0, 0, 200, 100, "Continuer")
            button_continuer.add(continuer_text)
            button_continuer.onclick = button_listener
            w.add(button_continuer)
            input_box = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            input_box.borderWidth = 5
            input_box.radius = 10
            input_box.hide_bg = True
            input_box.transparent = True
            input_text = obj.Label(0, 0, 200, 100, "Continuer")
            input_box.add(input_text)
            w.add(input_box)
            nuage_forward()
            w.destroy(count_text)
            w.destroy(plus_box)
            w.destroy(minus_box)
            w.destroy(plus_text)
            w.destroy(minus_text)
            w.destroy(number_text)
            w.destroy(counter_box)
            input_box.transparent = False
            input_text.transparent = False
            button_continuer.transparent = False
            nuage_backward()
            init_Player_Name = False
    w.updateAll()