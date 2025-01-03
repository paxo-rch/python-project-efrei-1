import graphics.objects as obj
import pygame
import utility_functions
import time
from pygamevideo import Video
def Escape():
    global StartMenu, Intro, init_Intro
    if pygame.key.get_pressed()[pygame.K_SPACE] and StartMenu:
        StartMenu = False
        init_Intro = True
        Intro = True
w = obj.Win()
pygame.display.set_caption('Fort Boyard Client v1.0')
running = True
StartMenu = True
Intro = False
init_StartMenu = True
init_Intro = False
while running:
    if StartMenu:
        if init_StartMenu:
            video = Video("genrique.mp4")
            video.play(True)
            w.hide_bg = True
            text = obj.Box(obj.WIN_WIDTH/3.4, obj.WIN_HEIGHT/1.5, 600, 200)
            text.transparent = True
            text.loadImage("parchemin_menu.png")
            w.add(text)
            titlebox = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/10, 500, 400)
            titlebox.transparent = True
            titlebox.loadImage("titrefort.png")
            w.add(titlebox)
            obj.Object.onkeyboard = Escape
            init_StartMenu = False
        utility_functions.StartMenu(video,text)
    else:
        if init_Intro:
            nuages = []
            nuages1 = []
            sky_box = obj.Box(0, 0, obj.WIN_WIDTH, obj.WIN_HEIGHT)
            sky_box.transparent = True
            button_skip = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
            button_skip.borderWidth = 5
            button_skip.radius = 10
            button_skip.hide_bg = True
            button_skip.transparent = True
            w.add(button_skip)
            w.add(sky_box)
            for i in range(4):
                nuage = obj.Box(-1700, -500+i*200, 1700, 1000)
                nuage.transparent = True
                nuage.loadImage("nuagenobg.png")
                sky_box.add(nuage)
                nuages.append(nuage)
                nuage = obj.Box(obj.WIN_WIDTH, -500+i*200, 1700, 1000)
                nuage.transparent = True
                nuage.loadImage("nuagenobg.png")
                sky_box.add(nuage)
                nuages1.append(nuage)
            for j in range(115):
                for i in nuages:
                    i.x += 10
                for i in nuages1:
                    i.x -= 10
                video.draw_to(obj.gui, (0, 0))
                w.updateAll()
            w.hide_bg = False

            w.destroy(titlebox)
            w.destroy(text)
            w.loadImage("parchemin.jpg")
            button_skip.transparent = False
            for j in range(115):
                for i in nuages:
                    i.x -= 10
                for i in nuages1:
                    i.x += 10
                w.updateAll()
            w.destroy(sky_box)
            text_intro = "Bienvenue à vous jeunes aventuriers\nVous recherchez la gloire, le pouvoir et la richesse ?\nVous êtes au bon endroit.\nIci vous pourrez obtenir tous ce que vous désirez,\nmais pour cela il faudra réussir les épreuves choisis par le maitre du jeu\nBonne chance!"
            label_intro = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 15, 15,"")
            w.add(label_intro)
            for i in text_intro:
                label_intro.text += i
                time.sleep(0.05)
                w.updateAll()
            init_Intro = False
    w.updateAll()