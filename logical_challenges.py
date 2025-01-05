# Function to display the remaining sticks
def display_sticks(n):
    """Displays the remaining sticks visually.

    Args:
        n: The number of sticks remaining.
    """
    print("Remaining sticks: " + "|" * n)

# Function for player's stick removal input
def player_removal(n):
    """Gets the number of sticks the player wants to remove.

    Args:
        n: The current number of sticks (not used in this function, but kept for consistency).

    Returns:
        The number of sticks the player wants to remove (1, 2, or 3).
    """
    print("Player's turn.")
    interval = [1, 2, 3]

    i = 0
    while i not in interval:
        i = int(input(f"How many sticks do you want to remove {interval}: "))
        
        if i in interval:
            return i
    
# Function for the master's stick removal
def master_removal(n):
    """Calculates and performs the master's stick removal.

    Args:
        n: The number of sticks remaining.

    Returns:
        The number of sticks the master removed.
    """
    interval = [1, 2, 3]

    rm = ((n-1)%4)  # Calculate the number of sticks to remove (we found this by our own)
    if(rm == 0):
        rm = 1

    print("The master removed " + str(rm) + " stick(s).")

    return rm

# Main Nim game function
def nim_game():
    """Plays the Nim game."""
    n = 20  # Initial number of sticks
    who = True  # True for player's turn, False for master's turn

    while n > 0:
        if(who):
            display_sticks(n)
            n -= player_removal(n)
        else:
            display_sticks(n)
            n -= master_removal(n)
        who = not who  # Switch turns

    # Determine and print the winner
    if(who):
        print("The game master removed the last stick. The player wins!")
    else:
        print("The player removed the last stick. The game master wins!")

    return who  # True if player wins

# Tic Tac Toe section

import random

# Function to display the Tic Tac Toe grid
def display_grid(grid):
    """Displays the Tic Tac Toe grid in the console.

    Args:
        grid: A 2D list representing the game grid.
    """
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

# Function to check for a victory
def check_victory(grid, symbol):
    """Checks if a player has won the game.

    Args:
        grid: The game grid.
        symbol: The player's symbol (1 for X, 2 for 0).

    Returns:
        True if the player has won, False otherwise.
    """
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

# Function for the master's move in Tic Tac Toe
def master_move(grid):
    """Determines the master's move.

    Args:
        grid: The game grid.

    Returns:
        A tuple (row, column) representing the master's move, or None if the grid is full.
    """
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
        
# Function for the player's turn in Tic Tac Toe
def player_turn(grid):
    """Gets the player's move input.

    Args:
        grid: The game grid.
    """
    while True:
        print("Player X, it's your turn. Where do you want to place your symbol?")
        y = int(input("Enter the x coordinate: ")) - 1
        x = int(input("Enter the y coordinate: ")) - 1

        if(0 <= x <= 2 and 0 <= y <= 2 and grid[x][y] == 0):
            grid[x][y] = 1
            return

        print("Invalid move. Try again. x and y should be in range (1, 2, 3)")
        
# Function for the master's turn in Tic Tac Toe
def master_turn(grid):
    """Executes the master's turn.

    Args:
        grid: The game grid.
    """
    move = master_move(grid)
    if move:
        grid[move[0]][move[1]] = 2

# Function to check if the grid is full
def full_grid(grid):
    """Checks if the Tic Tac Toe grid is full.

    Args:
        grid: The game grid.

    Returns:
        True if the grid is full, False otherwise.
    """
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True

# Function to check the result of the Tic Tac Toe game
def check_result(grid):
    """Checks if there's a winner or a draw.

    Args:
        grid: The game grid.

    Returns:
        True if the game has ended (win or draw), False otherwise.
    """
    if check_victory(grid, 1):
        return True
    elif check_victory(grid, 2):
        return True
    elif full_grid(grid):
        return True
    else:
        return False

# Main Tic Tac Toe game function
def tictactoe_game():
    """Plays the Tic Tac Toe game."""
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    who = True # True for player
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

from graphics.objects import *  # This import is likely from a custom graphics library
import math
from time import *
from Utils import *
def master_removal(n):
    """Master removal function for the graphical Nim game.

    Args:
        n: The number of sticks remaining.

    Returns:
        The number of sticks the master removed.
    """
    interval = [1, 2, 3]

    rm = ((n-1)%4)
    if(rm == 0):
        rm = 1

    print("The master removed " + str(rm) + " stick(s).")

    return rm

def nim_game(player):
    """Plays the Nim game with a graphical interface."""
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
    nuage_backward(win)
    def move_stick(nb, who):
        """Animates the movement of the sticks.

        Args:
            nb: The number of sticks to move.
            who: True if it's the player's turn, False if it's the master's turn.
        """
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
                """Creates a button click handler.

                Args:
                    t: The number of sticks to remove when the button is clicked.

                Returns:
                    A function that handles the button click.
                """
                def handler():
                    nonlocal torm
                    torm = t
                    btn_1.onclick = None
                    btn_2.onclick = None
                    btn_3.onclick = None
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
        winner(who)
        return player
    else:
        winner(who)
        return 0

def winner(who):
    w = Win()
    w.loadImage("parchemin.jpg")
    title2 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You won the game!\nDo you want to exit or play again ?")
    title2.alignment = CENTER
    title2.hide = True
    w.add(title2)

    title3 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You lost the game, \ndo you want to exit or play again ?")
    title3.alignment = CENTER
    title3.hide = True
    w.add(title3)

    exit = Label(WIN_WIDTH/8, WIN_HEIGHT/2, WIN_WIDTH/4, WIN_WIDTH/8, "Exit")
    exit.alignment = CENTER
    exit.loadImage("small_paper.png")
    w.add(exit)
    if(who):
        title2.hide = False
    else:
        title3.hide = False
    loop1 = True
    def exit_listener():
        nonlocal loop1
        if loop1:
            loop1 = False
            nuage_forward(w)
    exit.onclick = exit_listener
    while loop1:
        w.updateAll()
