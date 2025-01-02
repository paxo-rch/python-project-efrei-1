import graphics.objects as obj
import pygame
import time
from pygamevideo import Video
def StartMenuEscape():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        StartMenu = False
        Intro = True
def StartMenu(w,video,text):
        w.hide_bg = True
        video.draw_to(obj.gui, (0, 0))
        if time.time() % 1 > 0.5:
            text.text = "PRESS SPACE TO PLAY"
            Blink_Play_Btn = False
        else:
            text.text = ""
            Blink_Play_Btn = True
def Introduction():
    w = obj.Win()
    pygame.display.set_caption('Fort Boyard Client v1.0')
    text = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/1.25, 20, 20, "PRESS SPACE TO PLAY")
    text.textColor = (255, 255, 255)
    w.add(text)
    title = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 20, 20,"FORT BOYARD")
    w.add(title)
    running = True
    video = Video("genrique.mp4")
    video.play(True)
    Start_Menu = True
    intro = False
    obj.Object.onkeyboard = StartMenuEscape
