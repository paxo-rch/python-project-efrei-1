# Mainly used to move the clouds (animation)
# Author: Jules

import graphics.objects as obj

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