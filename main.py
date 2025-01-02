import graphics.objects as obj
import pygame
import utility_functions
import time
from pygamevideo import Video
def Escape():
    global StartMenu, Intro
    if pygame.key.get_pressed()[pygame.K_SPACE] and StartMenu:
        nuages = []
        nuages1 = []
        for i in range(4):
            nuage = obj.Box(-1700, -500+i*200, 1700, 1000)
            nuage.transparent = True
            nuage.loadImage("nuagenobg.png")
            w.add(nuage)
            nuages.append(nuage)
        for i in range(4):
            nuage = obj.Box(obj.WIN_WIDTH, -500+i*200, 1700, 1000)
            nuage.transparent = True
            nuage.loadImage("nuagenobg.png")
            w.add(nuage)
            nuages1.append(nuage)
        for j in range(115):
            for i in nuages:
                i.x += 10
            for i in nuages1:
                i.x -= 10
            video.draw_to(obj.gui, (0, 0))
            w.updateAll()
        video.stop()
        w.destroy(titlebox)
        for j in range(115):
            for i in nuages:
                i.x -= 10
            for i in nuages1:
                i.x += 10
            w.updateAll()
        w.hide_bg = False
        StartMenu = False
        Intro = True
w = obj.Win()
pygame.display.set_caption('Fort Boyard Client v1.0')
running = True
StartMenu = True
Intro = False
init_StartMenu = True
print("test") 
while running:
    if StartMenu:
        if init_StartMenu:
            video = Video("genrique.mp4")
            video.play(True)
            text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/1.25, 20, 20, "PRESS SPACE TO PLAY")
            text.textColor = (255, 255, 255)
            w.add(text)
            titlebox = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/10, 500, 400)
            titlebox.transparent = True
            titlebox.loadImage("titrefort.png")
            w.add(titlebox)
            obj.Object.onkeyboard = Escape
            init_StartMenu = False
        utility_functions.StartMenu(w,video,text)
    else:
        pass
    print(StartMenu)
    w.updateAll()