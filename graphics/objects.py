import pygame
import time
import math
pygame.init()

WIN_WIDTH = 1600
WIN_HEIGHT = 800

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

    keys = []
    Object.onkeyboard = None

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.children = []
        self.parent = None
        self.onclick = None
        self.onfocused = None
        self.onstartfocused = None
        self.onendfocused = None

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

    def renderAll(self):
        self.render()
        for child in self.children:
            child.render()

        if(self.parent is None):
            pygame.display.flip()

    def updateAll(self):
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
                        print(Object.tx, Object.ty)

                if event.type == pygame.KEYDOWN:
                    if(Object.onkeyboard):
                        Object.onkeyboard()
                pygame.key.get_pressed()

        for child in self.children:
            if(child.update()):
                return True
        self.update()

    def update(self):
        if self.getAbsoluteX() < self.tx < self.getAbsoluteX() + self.w and self.getAbsoluteY() < self.ty < self.getAbsoluteY() + self.h:
            if self.onfocused is not None:
                self.onfocused()

            if self.onstartfocused is not None and Object.objectFocused is None:
                Object.objectFocused = self
                self.onstartfocused()
                print("Focused")
                return True

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

        print("a")

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

    def render(self):
        gui.fill((255, 255, 255))    

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

w = Win()

g = Grid(0, 0, WIN_WIDTH/4, WIN_HEIGHT/4)
g.setGrid(convertToGrid([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

"""g.setGrid(convertToGrid([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],                      # example of syntax with grids
                       lambda label, i, j: setattr(label, 'textColor', BLUE)))"""
w.add(g)

g.onclick = lambda: print("You clicked the grid")
g.onstartfocused = lambda: setattr(g, 'gridColor', RED)
g.onendfocused = lambda: setattr(g, 'gridColor', BLACK)

running = True
i = 0

while running:
    g.w = WIN_WIDTH/4 + (WIN_WIDTH/6) * math.cos(i/20)
    g.h = WIN_HEIGHT / 4 + (WIN_HEIGHT / 6) * math.sin(i / 20)
    i+=1
    w.updateAll()
