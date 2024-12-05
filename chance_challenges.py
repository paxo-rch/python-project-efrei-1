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
chance_challenge()