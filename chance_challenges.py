import random
def shell_game():
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


############# With interface version

from graphics.objects import *
import points

def shell_game():
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

    loop1 = True
    def global_exit():
        nonlocal loop1, loop2
        loop1 = False
        loop2 = False
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
        result = random.choice([True, False]) #challenge()

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


chance_challenge()