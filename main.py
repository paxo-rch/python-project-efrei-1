import graphics.objects as obj
import pygame
import utility_functions
from pygamevideo import Video
def Escape():
    global StartMenu, Intro
    if pygame.key.get_pressed()[pygame.K_SPACE] and StartMenu:
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
            titlebox = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/4, 20, 20).loadImage("titrefort.png")
            w.add(titlebox)
            obj.Object.onkeyboard = Escape
            init_StartMenu = False
        utility_functions.StartMenu(w,video,text)
    else:
        video.stop()
        w.hide_bg = False
    print(StartMenu)
    w.updateAll()