import graphics.objects as obj
import pygame
import utility_functions
import time
from pygamevideo import Video
def nuage_forward():
    global nuages,nuages1,sky_box
    nuages = []
    nuages1 = []
    sky_box = obj.Box(0, 0, obj.WIN_WIDTH, obj.WIN_HEIGHT)
    sky_box.hide = True
    w.add(sky_box)
    for i in range(4):
        nuage = obj.Box(-1700, -500+i*200, 1700, 1000)
        nuage.hide = True
        nuage.loadImage("nuagenobg1.png")
        sky_box.add(nuage)
        nuages.append(nuage)
        nuage = obj.Box(obj.WIN_WIDTH, -500+i*200, 1700, 1000)
        nuage.hide = True
        nuage.loadImage("nuagenobg1.png")
        sky_box.add(nuage)
        nuages1.append(nuage)
    rate = 0.75
    for j in range(round(115*rate)):
        for i in nuages:
            i.x += 10/rate
        for i in nuages1:
            i.x -= 10/rate
        video.draw_to(obj.gui, (0, 0))
        w.updateAll()
def nuage_backward():
    rate = 0.75
    for j in range(round(115*rate)):
        for i in nuages:
            i.x -= 10/rate
        for i in nuages1:
            i.x += 10/rate
        w.updateAll()
    w.destroy(sky_box)

def KeyboardListener():
    global StartMenu, Intro, init_Intro
    if pygame.key.get_pressed()[pygame.K_SPACE] and StartMenu:
        StartMenu = False
        init_Intro = True
        Intro = True
def button_skip_listener():
    global Intro_Skiped, Player_Selection, Intro,init_Player_Selection
    if skip_text.text == "Passer":
        Intro_Skiped = True
    else:
        Intro = False
        Player_Selection = True
        init_Player_Selection = True
        
w = obj.Win()
pygame.display.set_caption('Fort Boyard Client v1.0')
running = True
StartMenu = True
Intro = False
Player_Selection = False

init_StartMenu = True
init_Intro = False
init_Player_Selection = False
while running:
    if StartMenu:
        if init_StartMenu:
            video = Video("genrique.mp4")
            video.play(True)
            w.hide_bg = True
            text = obj.Box(obj.WIN_WIDTH/3.4, obj.WIN_HEIGHT/1.5, 600, 200)
            text.hide = True
            text.loadImage("parchemin_menu.png")
            w.add(text)
            titlebox = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/10, 500, 400)
            titlebox.hide = True
            titlebox.loadImage("titrefort.png")
            w.add(titlebox)
            obj.Object.onkeyboard = KeyboardListener
            init_StartMenu = False
        utility_functions.StartMenu(video,text)
    elif Intro:
        if init_Intro:
            Intro_Skiped = False
            button_skip = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            button_skip.borderWidth = 5
            button_skip.radius = 10
            button_skip.hide_bg = True
            button_skip.hide = True
            skip_text = obj.Label(0, 0, 200, 100, "Passer")
            button_skip.add(skip_text)
            w.add(button_skip)
            nuage_forward()
            w.hide_bg = False
            w.destroy(titlebox)
            w.destroy(text)
            w.loadImage("parchemin.jpg")
            button_skip.hide = False
            button_skip.onclick = button_skip_listener
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
            count_text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choisissez le nombre de joueurs")
            count_text.hide = True

            counter_box = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 400, 200)
            counter_box.hide_bg = True
            counter_box.borderWidth = 5
            counter_box.radius = 10
            w.add(counter_box)
            number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "0")
            counter_box.add(number_text)
            plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
            plus_box.hide_bg = True
            plus_box.borderWidth = 5
            plus_box.radius = 10
            counter_box.add(plus_box)
            plus_text = obj.Label(plus_box.x+counter_box.w/2, plus_box.y+plus_box.h/2, 0, 0, "+")
            plus_box.add(plus_text)
            minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
            minus_box.hide_bg = True
            minus_box.borderWidth = 5
            minus_box.radius = 10
            counter_box.add(minus_box)
            minus_text = obj.Label(minus_box.x+minus_box.w/2, minus_box.y+minus_box.h/2, 0, 0, "-")
            minus_box.add(minus_text)
            counter_box.hide = True
            minus_box.hide = True
            plus_box.hide = True
            
            w.add(count_text)
            nuage_forward()
            w.destroy(button_skip)
            w.destroy(label_intro)
            count_text.hide = False
            minus_box.hide = False
            plus_box.hide = False
            counter_box.hide = False
            print(counter_box.x, counter_box.y, counter_box.w, counter_box.h)
            nuage_backward()
            init_Player_Selection = False
    w.updateAll()