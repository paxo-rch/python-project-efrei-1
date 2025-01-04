def display_sticks(n):
    print("Remaining sticks: " + "|" * n)

def player_removal(n):
    print("Player's turn.")
    interval = [1, 2, 3]

    i = 0
    while i not in interval:
        i = int(input(f"How many sticks do you want to remove {interval}: "))
        
        if i in interval:
            return i
    
def master_removal(n):
    interval = [1, 2, 3]

    rm = ((n-1)%4)
    if(rm == 0):
        rm = 1

    print("The master removed " + str(rm) + " stick(s).")

    return rm

def nim_game():
    n = 20
    who = True

    while n > 0:
        if(who):
            display_sticks(n)
            n -= player_removal(n)
        else:
            display_sticks(n)
            n -= master_removal(n)
        who = not who


    if(who):
        print("The game master removed the last stick. The player wins!")
    else:
        print("The player removed the last stick. The game master wins!")

    return who  # True if player wins

# Tic Tac Toe

import random

def display_grid(grid):
    for i in grid:
        for r,j in enumerate(i):
            if j == 0:
                print(" ", end="")
            elif j == 1:
                print("X", end="")
            else:
                print("0", end="")
            
            if r != len(i) - 1:
                print(" | ", end="")
        print("\n" + "-" * len(grid)*3)
    print("\n")

def check_victory(grid, symbol):
    for line in grid:   # lines
        win = True
        for i in line:
            if symbol != i:
                win = False
                break
        if(win):
            return True
        
    for col in range(len(grid)):    # columns
        win = True
        for row in range(len(grid)):
            if symbol != grid[row][col]:
                win = False
                break
        if(win):
            return True

    win = True
    for i in range(len(grid)):    # diagonal
        if symbol != grid[i][i]:
            win = False
            break
    if(win):
        return True

    win = True
    for i in range(len(grid)):    # anti-diagonal
        if symbol != grid[i][len(grid)-i-1]:
            win = False
            break
    if(win):
        return True

    return False

def master_move(grid):
    if(grid[1][1] == 0):
        return (1,1)

    canPlay = False
    for row in grid:
        for cell in row:
            if cell == 0:
                canPlay = True
                break
    
    if(not canPlay):
        return None
    
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                grid_c = list(map(list, grid))
                grid_c[i][j] = 2
                if check_victory(grid_c, 2):
                    return (i,j)
                grid_c[i][j] = 1
                if check_victory(grid_c, 1):
                    return (i,j)

    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)

        if(grid[x][y] == 0):
            return (x,y)
        
def player_turn(grid):
    while True:
        print("Player X, it's your turn. Where do you want to place your symbol?")
        y = int(input("Enter the x coordinate: ")) - 1
        x = int(input("Enter the y coordinate: ")) - 1

        if(0 <= x <= 2 and 0 <= y <= 2 and grid[x][y] == 0):
            grid[x][y] = 1
            return

        print("Invalid move. Try again. x and y should be in range (1, 2, 3)")
        
def master_turn(grid):
    move = master_move(grid)
    if move:
        grid[move[0]][move[1]] = 2

def full_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True

def check_result(grid):
    if check_victory(grid, 1):
        return True
    elif check_victory(grid, 2):
        return True
    elif full_grid(grid):
        return True
    else:
        return False

def tictactoe_game():
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    who = True
    while not check_result(grid):
        display_grid(grid)
        if who:
            player_turn(grid)
        else:
            master_turn(grid)
        who = not who

    display_grid(grid)
    if check_victory(grid, 1):
        print("Player wins!")
        return True
    elif check_victory(grid, 2):
        print("Master wins!")
        return False
    else:
        print("Draw!")
        return False

############# With interface version

from graphics.objects import *
import math
from time import *
import points

# We will only do the nim game here

def display_sticks(n):
    print("Remaining sticks: " + "|" * n)

def player_removal(n):
    print("Player's turn.")
    interval = [1, 2, 3]

    i = 0
    while i not in interval:
        i = int(input(f"How many sticks do you want to remove {interval}: "))
        
        if i in interval:
            return i
    
def master_removal(n):
    interval = [1, 2, 3]

    rm = ((n-1)%4)
    if(rm == 0):
        rm = 1

    print("The master removed " + str(rm) + " stick(s).")

    return rm

def nim_game():
    n = 20
    who = True

    win = Win()
    win.loadImage("parchemin.jpg")
    win.add(Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Nim game"))

    text = Label(WIN_WIDTH/2, WIN_HEIGHT/3, 20, 20, "The goal is to not remove the last stick. You can remove 1, 2 or 3 sticks.")
    text.alignment = CENTER
    win.add(text)

    sticks = []

    for i in range(n):
        stick = Box(WIN_WIDTH/2 - 40 * n / 2 + i*40, WIN_HEIGHT/2, 20, 100)
        stick.loadImage("stick.png")
        stick.transparent = True
        win.add(stick)
        sticks.append(stick)

    btn_1 = Label(WIN_WIDTH/2 - 90, WIN_HEIGHT - 120, 60, 100, "1")
    btn_1.alignment = CENTER
    btn_1.loadImage("small_paper.png")
    win.add(btn_1)

    btn_2 = Label(WIN_WIDTH/2 - 10, WIN_HEIGHT - 120, 60, 100, "2")
    btn_2.alignment = CENTER
    btn_2.loadImage("small_paper.png")
    win.add(btn_2)

    btn_3 = Label(WIN_WIDTH/2 + 70, WIN_HEIGHT - 120, 60, 100, "3")
    btn_3.alignment = CENTER
    btn_3.loadImage("small_paper.png")
    win.add(btn_3)

    def move_stick(nb, who):
        sticks_to_move = sticks[n-nb:n]

        for i in range(30):
            for stick in sticks_to_move:
                if(who):
                    stick.y += 2
                else:
                    stick.y -= 2
            win.updateAll()

    while n > 0:
        if(who):
            torm = 0

            def button_listener(t):
                def handler():
                    nonlocal torm
                    torm = t
                return handler

            btn_1.onclick = button_listener(1)
            btn_2.onclick = button_listener(2)
            btn_3.onclick = button_listener(3)

            while torm == 0:
                win.updateAll()

            print("Player's turn.", torm, "stick(s) removed")
            move_stick(torm, who)
            n -= torm
        else:
            torm = master_removal(n)
            move_stick(torm, who)
            n -= torm
        who = not who


    if(who):
        print("The game master removed the last stick. The player wins!")
    else:
        print("The player removed the last stick. The game master wins!")

    return who  # True if player wins

nim_game()