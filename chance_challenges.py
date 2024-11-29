import random
def shell_game():
    shell = ['A','B','C']
    attempt = 0
    selected_shell = random.choice(shell)
    slected_player = ""
    attmpts = 2
    print("Welcome to the shell game\nYou will have to guess the correct shell in which the coin is hidden\nYou have 2 attempts\n Good Luck!")
