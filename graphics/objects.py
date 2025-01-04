import pygame
import time
import math
pygame.init()

WIN_WIDTH = 1280
WIN_HEIGHT = 720

gui = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
clock = pygame.time.Clock()
fps = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

LEFT = 1
CENTER = 2
RIGHT = 3

class Object:
    tx, ty = 0, 0

    mouse = False
    objectFocused = None

    keys = pygame.key.get_pressed()
    onkeyboard = None

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
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

    def add(self, o):
        self.children.append(o)
        o.parent = self
    def getAbsoluteX(self):
        if self.parent is None:
            return self.x
        else:
            return self.parent.getAbsoluteX() + self.x

    def getAbsoluteY(self):
        if self.parent is None:
            return self.y
        else:
            return self.parent.getAbsoluteY() + self.y

    def loadImage(self, path):
        try:
            self.original_image = pygame.image.load(path).convert_alpha()  # Original image copy
            self.rect = self.original_image.get_rect()  # Rect of original image
        except pygame.error as e:
            print(f"Error loading image '{path}': {e}")
            self.original_image = None
            self.rect = None
    def unloadImage(self):
        self.original_image = None
        self.rect = None
    def destroy(self,o):
        self.children.remove(o)

    def privateRender(self):
        if self.original_image and self.rect:
            scaled_image = pygame.transform.scale(self.original_image, (self.w, self.h))
            scaled_rect = scaled_image.get_rect()
            scaled_rect.topleft = (self.getAbsoluteX(), self.getAbsoluteY())
            gui.blit(scaled_image, scaled_rect)


    def renderAll(self):
        if(self.hide):
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

    def updateAll(self):
        if(self.hide):
            return False
        
        if(self.parent is None):
            self.renderAll()
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                Object.tx, Object.ty = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Object.mouse = True

                Object.keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if(Object.onkeyboard):
                        Object.onkeyboard()

        for child in self.children:
            if(child.update()):
                return True
            
        self.update()

        return False

    def update(self):
        if self.getAbsoluteX() < self.tx < self.getAbsoluteX() + self.w and self.getAbsoluteY() < self.ty < self.getAbsoluteY() + self.h:
            if self.onfocused is not None:
                self.onfocused()

            if self.onstartfocused is not None and Object.objectFocused is None:
                Object.objectFocused = self
                self.onstartfocused()
                print("Focused")

            if Object.mouse and self.onclick is not None:
                self.onclick()
                Object.mouse = False
                print("Clicked")
                return True

        elif(Object.objectFocused == self):
            if self.onendfocused is not None:
                self.onendfocused()
            Object.objectFocused = None


class Box(Object):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, 0)
        self.w = w
        self.h = h
        self.backgroundColor = BLUE
        self.radius = 0
        self.borderColor = BLACK
        self.borderWidth = 0
        self.transparent = False
        self.hide_bg = False
    def renderBack(self):
        if not self.transparent:
            if not self.hide_bg:
                pygame.draw.rect(gui, self.backgroundColor, (self.x, self.y, self.w, self.h), 0, self.radius)
            pygame.draw.rect(gui, self.borderColor, (self.x, self.y, self.w, self.h), self.borderWidth, self.radius)

class Label(Object):
    def __init__(self, x, y, w, h, text):
        super().__init__(x, y, 0)
        self.text = text
        self.w = w
        self.h = h
        self.alignment = CENTER  # Default alignment is left
        self.textColor = BLACK
        self.fontSize = 50

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

        gui.blit(text_surface, text_rect)

class Grid(Object):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, 0)
        self.w = w
        self.h = h
        self.grid = []
        self.gridColor = BLACK

    def setGrid(self, grid):
        self.grid = grid

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

                    if isinstance(self.grid[i][j], Label):
                        self.grid[i][j].parent = self
                        self.grid[i][j].x = wf * j
                        self.grid[i][j].y = hf * i
                        self.grid[i][j].w = wf
                        self.grid[i][j].h = hf
                        self.grid[i][j].renderAll()
        except:
            print("Need 2 dimensions")

class Win(Object):
    def __init__(self):
        super().__init__(0, 0, 0)
        self.w = WIN_WIDTH
        self.h = WIN_HEIGHT
        self.hide_bg = False

    def renderBack(self):
        if not self.hide_bg:
            gui.fill((255, 255, 255))    
        pass
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

