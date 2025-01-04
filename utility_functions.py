import graphics.objects as obj
import pygame
import time
from pygamevideo import Video
def nuage_forward(w,c=None):
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
        if c is not None:
            c.draw_to(obj.gui, (0, 0))
        w.updateAll()
    w.children.clear()

        
        
"""
Function that moves the clouds backward
"""
def nuage_backward(w):
    nuages = []
    nuages1 = []
    #create a box to contain the clouds
    sky_box = obj.Box(0, 0, obj.WIN_WIDTH, obj.WIN_HEIGHT)
    sky_box.transparent = True
    w.add(sky_box)
    #loop that creates 4 clouds on each sides
    for i in range(4):
        #create a box containing a cloud on the left
        nuage = obj.Box(-550, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage("nuagenobg1.png")
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages.append(nuage)
        #create a box containing a cloud on the left
        nuage = obj.Box(130, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage("nuagenobg1.png")
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages1.append(nuage)
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
    nuage_forward(w,video)
    Introduction()
def Introduction():
    w = obj.Win()
    Intro_Skiped = False
    text_done = False
    button_skip = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_skip.borderWidth = 5
    button_skip.radius = 10
    button_skip.hide_bg = True
    button_skip.transparent = True
    skip_text = obj.Label(0, 0, 200, 100, "Passer")
    button_skip.add(skip_text)
    w.add(button_skip)
    w.loadImage("parchemin.jpg")
    button_skip.transparent = False
    def button_listener():
        nonlocal Intro_Skiped, text_done
        if skip_text.text == "Passer":
            Intro_Skiped = True
        if text_done:
            text_done = False
            nuage_forward(w)
            PlayerSelection()
    button_skip.onclick = button_listener
    nuage_backward(w)
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
    text_done = True
    while True:
        w.updateAll()
def PlayerSelection():
    w = obj.Win()
    w.hide_bg = False
    w.loadImage("parchemin.jpg")
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
    count_text.transparent = False
    minus_box.transparent = False
    plus_box.transparent = False
    plus_text.transparent = False
    minus_text.transparent = False
    number_text.transparent = False
    counter_box.transparent = False
    button_continuer.transparent = False
    nuage_backward(w)
    def CounterListenerPlus():
        nonlocal counter, number_text
        if counter < 3:
            counter += 1
            number_text.text = str(counter)
    def CounterListenerMinus():
        nonlocal counter, number_text
        if counter > 1:
            counter -= 1
            number_text.text = str(counter)
    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False
            nuage_forward(w)
            PlayerName()
    continuer = True
    plus_box.onclick = CounterListenerPlus
    minus_box.onclick = CounterListenerMinus
    button_continuer.onclick = button_listener
    while True:
        w.updateAll()
def PlayerName():
    players = []
    w = obj.Win()
    w.hide_bg = False
    w.loadImage("parchemin.jpg")
    texte = obj.Label(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/3, 15, 15,"Choisissez les caractéristiques du joueur 1")
    texte.transparent = True
    nuage_backward(w)
    while True:
        w.updateAll()
StartMenufunc()