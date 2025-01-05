# imports, useful libraries like pygame for the graphics, and time and maths to manage events and rendering
import pygame
import time
import math

# Some pygame initializations...
pygame.init()

WIN_WIDTH = 1280
WIN_HEIGHT = 720

gui = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
clock = pygame.time.Clock()
fps = 60

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# define text alignements
LEFT = 1
CENTER = 2
RIGHT = 3

# Object will be the base class for all widgets, it includes functions to manage the events, the properties and the rendering
class Object:
    # static variables that are shared between all objects
    tx, ty = 0, 0

    mouse = False
    objectFocused = None

    keys = pygame.key.get_pressed()
    onkeyboard = None

    # constructor that takes the position (x,y) and returns nothing
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 0
        self.h = 0
        self.radius = 0
        self.children = []
        self.parent = None
        self.onclick = None
        self.onfocused = None
        self.onstartfocused = None
        self.onendfocused = None
        self.hide = False
        # image
        self.image = None
        self.original_image = None

    # function that takes an object (o) and add it to the object as a child
    def add(self, o):
        self.children.append(o)
        o.parent = self
    
    # function that returns the absolute x position of the object in the hierarchy
    def getAbsoluteX(self):
        if self.parent is None:
            return self.x
        else:
            return self.parent.getAbsoluteX() + self.x

    # function that returns the absolute y position of the object in the hierarchy
    def getAbsoluteY(self):
        if self.parent is None:
            return self.y
        else:
            return self.parent.getAbsoluteY() + self.y

    # function that takes a path to an image and returns nothing, load an image in the background of the object
    def loadImage(self, path):
        try:
            self.original_image = pygame.image.load(path).convert_alpha()  # Original image copy
            self.rect = self.original_image.get_rect()  # Rect of original image
        except pygame.error as e:
            print(f"Error loading image '{path}': {e}")
            self.original_image = None
            self.rect = None
    
    # function that returns nothing, unload the image
    def unloadImage(self):
        self.original_image = None
        self.rect = None

    # function that takes an object (o) and remove it from the object
    def destroy(self,o):
        self.children.remove(o)

    # function used to render the background of the object if it has an image. This is called independently of the private render function
    def privateRender(self):
        if self.original_image and self.rect:
            scaled_image = pygame.transform.scale(self.original_image, (self.w, self.h))
            scaled_rect = scaled_image.get_rect()
            scaled_rect.topleft = (self.getAbsoluteX(), self.getAbsoluteY())
            gui.blit(scaled_image, scaled_rect)

    # function that renders the object and manage the hierarchy of rendering
    def renderAll(self):
        if self.hide:
            return
        try:
            self.renderBack()
        except:
            pass
        self.privateRender()
        try:
            self.render()
        except:
            pass

        for child in self.children:
            child.renderAll()

        if(self.parent is None):
            pygame.display.flip()

    # function that updates the object and manage the hierarchy of updates, including events and rendering
    def updateAll(self, delay=True):
        if self.hide:
            return False
        
        if(self.parent is None):
            self.renderAll()

            if(delay):  # limit the frame rate
                clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                Object.tx, Object.ty = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:   # register left click
                        Object.mouse = True

                Object.keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if(Object.onkeyboard):  # call the onkeyboard function if it exists when a key is pressed
                        Object.onkeyboard()

        for child in self.children:
            if(child.update()):
                return True
        self.update()

    # function that updates the object and manage the local events
    def update(self):
        # if the mouse is over the object
        if self.getAbsoluteX() < self.tx < self.getAbsoluteX() + self.w and self.getAbsoluteY() < self.ty < self.getAbsoluteY() + self.h:
            if self.onfocused is not None:  # call the onfocused function if it exists (when the mouse is over the object)
                self.onfocused()

            if self.onstartfocused is not None and Object.objectFocused is None: # call the onstartfocused function if it exists (when the mouse is over the object for the first time)
                Object.objectFocused = self
                self.onstartfocused()
                print("Focused")

            if Object.mouse and self.onclick is not None:   # call the onclick function if it exists (when the mouse is clicked on the object)
                self.onclick()
                Object.mouse = False
                print("Clicked")
                return True

        elif(Object.objectFocused == self):  # if the mouse is not over the object, and the object is focused, call the onendfocused function
            if self.onendfocused is not None:
                self.onendfocused()
            Object.objectFocused = None

# Widget box, it is a customizable box (color, radius and border)
class Box(Object):
    # constructor
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.backgroundColor = BLUE
        self.radius = 0
        self.borderColor = BLACK
        self.borderWidth = 0
        self.transparent = False
        self.hide_bg = False

    # function that renders the background of the object
    def renderBack(self):
        if not self.transparent:
            pygame.draw.rect(gui, self.borderColor, (self.x, self.y, self.w, self.h), self.borderWidth, self.radius) # Draw the border
            if not self.hide_bg:
                pygame.draw.rect(gui, self.backgroundColor, (self.x, self.y, self.w, self.h), 0, self.radius) # Draw the background
        # We render the larger rectangke with a border first, then the background rectangle because it will be on top, and smaller than the border rectangle

# Label: a text label
class Label(Object):
    # constructor
    def __init__(self, x, y, w, h, text):
        super().__init__(x, y)
        self.text = text
        self.w = w
        self.h = h
        self.alignment = CENTER  # Default alignment is left
        self.textColor = BLACK
        self.fontSize = 50
        self.transparent = False

    # function that renders the text
    def render(self):
        font = pygame.font.Font(None, self.fontSize)

        text_surface = font.render(self.text, True, self.textColor)

        zone_rect = pygame.Rect(self.getAbsoluteX(), self.getAbsoluteY(), self.w, self.h)

        if self.alignment == LEFT:
            text_rect = text_surface.get_rect(midleft=zone_rect.midleft)
            text_rect.x += 5  # Add a small left padding
        elif self.alignment == CENTER:
            text_rect = text_surface.get_rect(center=zone_rect.center)
        elif self.alignment == RIGHT:
            text_rect = text_surface.get_rect(midright=zone_rect.midright)
            text_rect.x -= 5 # Add a small right padding
        else:
            text_rect = text_surface.get_rect(center=zone_rect.center) #Default
        if not self.transparent:
            gui.blit(text_surface, text_rect)

# Input: a text input (a custom box with a text property)
class Input(Box):
    # constructor
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.backgroundColor = BLUE
        self.borderColor = BLACK
        self.borderWidth = 5
        self.radius = 10
        self.transparent = False
        self.hide_bg = True
        self.text = ""

    # does not need to render anything because it is a custom box and the rendering is managed by the Box class

# Grid: a grid of any number of rows and columns
class Grid(Object):
    # constructor
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
        self.grid = []
        self.gridColor = BLACK

    # function that sets the grid
    def setGrid(self, grid):
        self.grid = grid

    # function that renders the grid
    def render(self):
        h = len(self.grid)
        hf = self.h / h

        try:
            w = len(self.grid[0])
            wf = self.w / w

            for i in range(h):
                for j in range(w):
                    pygame.draw.rect(gui, self.gridColor, (self.x + wf * j, self.y + hf * i, wf, hf), 1)
                    pygame.draw.rect(gui, self.gridColor, (self.x + wf * j, self.y + hf * i, wf, hf), 1)

                    self.grid[i][j].parent = self   # The widget will be considered as a child but not in the tree, just local, same effect
                    self.grid[i][j].x = wf * j      # to manage efficiently the 2D array
                    self.grid[i][j].y = hf * i
                    self.grid[i][j].w = wf
                    self.grid[i][j].h = hf
                    self.grid[i][j].renderAll()
        except:
            print("Need 2 dimensions")

# Window: The main object of any hierarchy. It fills the whole screen and is made to have children. This is the one that will manage events and rendering
class Win(Object):
    # constructor
    def __init__(self):
        super().__init__(0, 0)
        self.w = WIN_WIDTH
        self.h = WIN_HEIGHT
        self.hide_bg = False

    # function that clear the screen
    def renderBack(self):
        if not self.hide_bg:
            gui.fill((255, 255, 255))    
        pass

# Function that converts a list to a 2D grid of widgets that can be added to a grid
def convertToGrid(l, forEach = None):
    if isinstance(l[0], list):
        grid = []
        for i, row in enumerate(l):
            row_labels = []
            for j, text in enumerate(row):
                l = Label(0, 0, 0, 0, str(text))
                if(forEach is not None):
                    forEach(l, i, j)
                row_labels.append(l)
            grid.append(row_labels)
        print(grid)
        return grid
    else:
        return [Label(0, 0, 0, 0, str(text)) for i, text in enumerate(l)]

