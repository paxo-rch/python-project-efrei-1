import graphics.objects as obj
import pygame
import time
from pygamevideo import Video
def nuage_forward(b,c):
    w = obj.Win()
    w.hide_bg = True
    #allows the clouds to be accessed by the backward function
    global nuages,nuages1,sky_box
    #initialize the list containing the cloud objects (nuages for the left and nuages1 for the right)
    nuages = []
    nuages1 = []
    #create a box to contain the clouds
    sky_box = obj.Box(0, 0, obj.WIN_WIDTH, obj.WIN_HEIGHT)
    sky_box.transparent = True
    w.add(sky_box)
    #loop that creates 4 clouds on each sides
    for i in range(4):
        #create a box containing a cloud on the left
        nuage = obj.Box(-1700, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage("nuagenobg1.png")
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages.append(nuage)
        #create a box containing a cloud on the left
        nuage = obj.Box(obj.WIN_WIDTH, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage("nuagenobg1.png")
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages1.append(nuage)
    #adjust the speed of the clouds
    rate = 0.75
    #loop that makes the clouds move forward
    for j in range(round(115*rate)):
        #move the clouds on the left
        for i in nuages:
            i.x += 10/rate
        #move the clouds on the right
        for i in nuages1:
            i.x -= 10/rate
        b.draw_to(obj.gui, (0, 0))
        w.updateAll()
        c.updateAll(False)
        
"""
Function that moves the clouds backward
"""
def nuage_backward():
    #adjust the speed of the clouds
    rate = 0.75
    #loop that makes the clouds move backward
    for j in range(round(115*rate)):
        #move the clouds on the left
        for i in nuages:
            i.x -= 10/rate
        #move the clouds on the right
        for i in nuages1:
            i.x += 10/rate
        w.updateAll()
    w.destroy(sky_box)
"""
Listener for all keyboard events
"""

"""
Listener for events related to the skip button and continue button
"""
def button_listener():
    global Intro_Skiped, Player_Selection, Intro,init_Player_Selection,Player_Name, init_Player_Name
    if Intro:
        if skip_text.text == "Passer":
            Intro_Skiped = True
        else:
            Intro = False
            Player_Selection = True
            init_Player_Selection = True
    elif Player_Selection:
        Player_Selection = False
        Player_Name = True
        init_Player_Name = True
def CounterListenerPlus():
    global counter, number_text
    if counter < 3:
        counter += 1
        number_text.text = str(counter)
def CounterListenerMinus():
    global counter, number_text
    if counter > 1:
        counter -= 1
        number_text.text = str(counter)

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
    StartMenu = True
    def KeyboardListener():
        nonlocal StartMenu
        if pygame.key.get_pressed()[pygame.K_SPACE] and StartMenu:
            StartMenu = False
    #set the keyboard listener
    obj.Object.onkeyboard = KeyboardListener
    def StartMenuAnimation(video,text):
        video.draw_to(obj.gui, (0, 0))
        if time.time() % 1 > 0.5:
            text.loadImage("parchemin_menu.png")
        else:
            text.unloadImage()
    while StartMenu:
        StartMenuAnimation(video,text)
        w.updateAll()
    nuage_forward(video,w)
StartMenufunc()