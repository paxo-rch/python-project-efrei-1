# Mainly used to move the clouds (animation)
# Author: Jules
parchemin_menu = "resources/images/parchemin_menu.png"
parchemin = "resources/images/parchemin.jpg"
arrowimg = "resources/images/arrow.png"
nuageimg = "resources/images/nuagenobg1.png"
small_paper = "resources/images/small_paper.png"
stickimg = "resources/images/stick.png"
titre_fort = "resources/images/titrefort.png"
img = "resources/images/img.png"
cupimg = "resources/images/cup.png"
import graphics.objects as obj
def history(text):
    """
    Write the text in the history file
    args: text (the text to write)
    return: None
    """
    try:
        with open("output/history.txt", "a") as f:
            f.write(str(text)+"\n")
    except:
        with open("output/history.txt", "w") as f:
            f.write(str(text)+"\n")

def nuage_forward(w,c=None):
    """
    Function to create and move the clouds forward
    args: w (the window object)
    return: None
    """
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
        nuage.loadImage(nuageimg)
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages.append(nuage)
        #create a box containing a cloud on the left
        nuage = obj.Box(obj.WIN_WIDTH, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage(nuageimg)
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
    """
    Function to create and move the clouds backward
    args: w (the window object)
    return: None
    """
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
        nuage.loadImage(nuageimg)
        #adding the cloud to the main box
        sky_box.add(nuage)
        nuages.append(nuage)
        #create a box containing a cloud on the left
        nuage = obj.Box(130, -500+i*200, 1700, 1000)
        #hiding the box
        nuage.transparent = True
        #loading the cloud image
        nuage.loadImage(nuageimg)
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