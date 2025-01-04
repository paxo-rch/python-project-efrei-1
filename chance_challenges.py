import random
from Utils import *
"""def shell_game():
    shell = ['A','B','C']
    attempt = 0
    
    slected_player = ""
    print("Welcome to the shell game\nYou will have to guess the correct shell in which the coin is hidden\nYou have 2 attempts\n Good Luck!")
    print("Guess between A, B, C")
    for i in range(2):
        selected_shell = random.choice(shell)
        print("Remaining attempts: ", 2-attempt)
        input_shell = str(input("Your guess: ")).capitalize()
        while input_shell not in shell:
            print("Please guess between A, B, C")
            input_shell = str(input("Your guess: ")).capitalize()
        if input_shell == selected_shell:
            print("Correct! You win a key")
            return True
        elif i!=1:
            print("Wrong! Try again")
        attempt += 1

    print("You lost the game, the key was under the shell : ", selected_shell)
    return False

def roll_dice_game():
    attempts = 3
    for i in range(3):
        print("Remaining attempts: ", attempts-i)
        input("Press enter to roll the dice")
        pdice = (random.randint(1,6),random.randint(1,6))
        print("You rolled ", pdice[0]," and ", pdice[1])
        if 6 in pdice:
            print("You win a key")
            return True
        print("Game master turn !")
        gdice = (random.randint(1,6),random.randint(1,6))
        print("The game master rolled ", gdice[0]," and ", gdice[1])
        if 6 in gdice:
            print("The game master has won !")
            return False
        print("No one got 6 moving on the next round")
    print("No one scored a 6, thats a draw")
    return False

def chance_challenge():
    functions = [shell_game,roll_dice_game]
    challenge =  random.choice(functions)
    return challenge()
"""

############# With interface version

from graphics.objects import *
import math
from time import *
import points



def shell_game():
    win = Win()
    win.loadImage("parchemin.jpg")

    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Welcome to the shell game\nYou will have to guess the correct shell in which the coin is hidden\nYou have 2 attempts\n Good Luck!")
    title.alignment = CENTER
    win.add(title)

    coin = Box(WIN_WIDTH/4 + 200 + 200/2-66/2, WIN_HEIGHT/2+200, 66, 66)
    coin.radius = 33
    coin.backgroundColor = YELLOW
    win.add(coin)

    cups = []
    cups_pos_goal = []

    for i in range(3):
        cup = Box(WIN_WIDTH/4 + 200*i, WIN_HEIGHT/2, 200, 200)
        cups_pos_goal.append([[cup.x,cup.y],[cup.x,cup.y],0])
        cup.loadImage("cup.png")
        cup.transparent = True
        win.add(cup)
        cups.append(cup)

    print("Welcome to the shell game\nYou will have to guess the correct shell in which the coin is hidden\nYou have 2 attempts\n Good Luck!")
    print("Guess between A, B, C")


    # ANIMATION OF THE COIN

    for i in range(30):
        coin.y -= 100/30
        win.updateAll()
    coin.hide = True

    # ANIMATION OF THE CUPS

    time = 5 # seconds
    j = 0
    for l in range(30*time+1):
        if(j%10 == 0):
            if(l >= 30*time-10):
                for i,cup in enumerate(cups_pos_goal):
                    cup[1] = [WIN_WIDTH/4 + 200*i, WIN_HEIGHT/2]
                    cup[2] = math.sqrt((cup[0][0]-cup[1][0])**2 + (cup[0][1]-cup[1][1])**2)
            else:
                for cup in cups_pos_goal:
                    cup[1] = [random.randint(0,WIN_WIDTH-200),random.randint(int(WIN_HEIGHT/3),WIN_HEIGHT - 200),0]
                    cup[2] = math.sqrt((cup[0][0]-cup[1][0])**2 + (cup[0][1]-cup[1][1])**2)
            print(cups_pos_goal[0],cups_pos_goal[1],cups_pos_goal[2])
        j+=1
        
        win.updateAll()

        for i,cup in enumerate(cups_pos_goal):
            dx = (cup[0][0] - cup[1][0])
            dy = (cup[0][1] - cup[1][1])
            d = math.sqrt(dx**2 + dy**2)
            if(d != 0):
                dx = dx/d
                dy = dy/d
                cup[0][0] -= dx/10*cup[2]
                cup[0][1] -= dy/10*cup[2]

                cups[i].x = cup[0][0]
                cups[i].y = cup[0][1]

    # END OF THE ANIMATION

    answer = random.randint(0,2)
    coin.x = WIN_WIDTH/4 + 200*answer + 200/2-66/2
    coin.y = WIN_HEIGHT/2+100
    coin.hide = False

    for i in range(2):
        cup_selected = None

        for i, cup in enumerate(cups):
            def create_handler(i):
                def handler():
                    nonlocal cup_selected
                    cup_selected = i
                return handler
            cup.onclick = create_handler(i)

        while (cup_selected is None):
            win.updateAll()

        for i in range(30):
            cups[cup_selected].y -= 150/30
            win.updateAll()
        
        if(cup_selected == answer):
            sleep(1)
            return True
        else:
            print("Wrong! Try again")
    return False

def roll_dice_game():
    win = Win()
    win.loadImage("parchemin.jpg")

    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Roll the dice game")
    title.alignment = CENTER
    win.add(title)

    name = ["Player", "Master"]
    whoid = 0
    who = Label(WIN_WIDTH/2, WIN_HEIGHT/3, 20, 20, "The " + name[whoid] + " plays now:")
    who.alignment = CENTER
    win.add(who)

    list_faces = [1,2,3,4,5,6]
    
    def move_list():
        nonlocal list_faces
        list_faces = list_faces[1:] + [list_faces[0]]

    roll = Label(WIN_WIDTH/4, WIN_HEIGHT/2, WIN_WIDTH/2, 40, str(" | ".join(str(list_faces).split(", "))))
    roll.alignment = CENTER
    win.add(roll)

    arrow = Box(WIN_WIDTH/2-135, WIN_HEIGHT/2+30, 40, 40)
    arrow.loadImage("arrow.png")
    arrow.transparent = True
    win.add(arrow)

    button = Label(WIN_WIDTH/3, WIN_HEIGHT/1.5, WIN_WIDTH/3, WIN_WIDTH/8, "Roll the dice")
    button.alignment = CENTER
    button.loadImage("small_paper.png")
    win.add(button)
    def roll_dice():
        for i in range(random.randint(1,12)):
            move_list()
        for i in range(40):
            move_list()
            sleep((0.05+i/2/30)**4)
            roll.text = str(" | ".join(str(list_faces).split(", ")))
            win.updateAll()
        return list_faces[0]
    
    win.updateAll()

    while True:
        if(whoid == 0):
            button.hide = False
            waiting = True
            def set_waiting_false():
                nonlocal waiting
                waiting = False
            button.onclick = set_waiting_false
            while waiting:
                win.updateAll()
        else:
            button.hide = True
        r = roll_dice()
        whoid = 1-whoid
        who.text = "The " + name[whoid] + " plays now:"
        
        if(whoid == 1):
            sleep(2)

        if(whoid == 0 and r == 6):
            who.text = "The " + name[whoid] + " wins!"
            for i in range(30):
                win.updateAll()
            return True
        elif(whoid == 1 and r == 6):
            return False
        
def chance_challenge():
    win = Win()
    win.loadImage("parchemin.jpg")

    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Chance Challenge")
    title.alignment = CENTER
    win.add(title)

    title2 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You won a key!\nDo you want to exit or play again ?")
    title2.alignment = CENTER
    title2.hide = True
    win.add(title2)

    title3 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You lost the game, \ndo you want to exit or play again ?")
    title3.alignment = CENTER
    title3.hide = True
    win.add(title3)


    button = Label(WIN_WIDTH/3, WIN_HEIGHT/2, WIN_WIDTH/3, WIN_WIDTH/8, "Choose a random \nchallenge")
    button.alignment = CENTER
    button.loadImage("small_paper.png")
    win.add(button)

    exit = Label(WIN_WIDTH/8, WIN_HEIGHT/2, WIN_WIDTH/4, WIN_WIDTH/8, "Exit")
    exit.alignment = CENTER
    exit.loadImage("small_paper.png")
    exit.hide = True
    win.add(exit)

    replay = Label(WIN_WIDTH*5/8, WIN_HEIGHT/2, WIN_WIDTH/4, WIN_WIDTH/8, "Play again")
    replay.alignment = CENTER
    replay.loadImage("small_paper.png")
    replay.hide = True
    win.add(replay)
    
    nuage_backward(win)

    loop1 = True
    def global_exit():
        nonlocal loop1, loop2
        if loop1:
            loop1 = False
            loop2 = False
            nuage_forward(win)
    exit.onclick = global_exit

    while loop1:
        loop2 = True
        def set_loop_false():
            nonlocal loop2
            loop2 = False
        button.onclick = set_loop_false
        replay.onclick = set_loop_false

        while loop2:
            win.updateAll()

        functions = [shell_game,roll_dice_game]
        challenge =  random.choice(functions)
        result = challenge()
        
        title.hide = True
        button.hide = True
        exit.hide = False
        replay.hide = False
        

        if(result):
            points.register_points("chance_challenge", 1)
            title2.hide = False
            title3.hide = True
            button.hide = True
        else:
            title2.hide = True
            title3.hide = False

