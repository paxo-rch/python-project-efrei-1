# This is the main file for the math challengess
# Author: Jules

import random
from Utils import *
from graphics.objects import *

def Factorial(n):
    """
    Calculates the factorial of a given number.

    Parameters:
        n: An integer for which the factorial is calculated.

    Returns:
        The factorial of n (n!).
    """
    # Loop to multiply each number from 1 to n.
    for i in range(1,n):
        n = n * i
    return n

def math_challenge_factorial():
    """
    Presents a factorial calculation challenge to the player.

    Parameters:
        None

    Returns:
        True if the player's answer is correct, False otherwise.
    """
    # Generate a random number between 1 and 10.
    n = random.randint(1,10)
    print("Math Challenge: Calculate the factorial of ",n)
    # Get the player's input.
    p = int(input("Your answer is : "))
    # Check if the player's input is the factorial of the number.
    if p == Factorial(n):
        print("Correct! You win a key")
        return True
    return False

def solve_linear_equation():
    """
    Generates random values for a linear equation (ax + b = 0).

    Parameters:
        None

    Returns:
        A tuple containing:
        a: The coefficient of x.
        b: The constant term.
        -b/a: The solution for x.
    """
    # Generate random values for a and b.
    a = random.randint(1,10)
    b = random.randint(1,10)
    # Return the values for the linear equation.
    return a, b , -b/a

def math_challenge_equation():
    """
    Presents a linear equation solving challenge to the player.

    Parameters:
        None

    Returns:
        True if the player's solution is correct, False otherwise.
    """
    # Generate values for the linear equation.
    a,b,c = solve_linear_equation()
    print("Math Challenge: Solve the linear equation ",a,"x + ",b," = 0")
    
    # Get the player's input and check if it matches the solution.
    x = float(eval(input("What is the value of x: ")))
    if x == c:
        print("Correct! You win a key")
        return True
    return False

def math_roulette_challenge():
    """
    Presents a math roulette challenge involving random numbers and operations.

    Parameters:
        None

    Returns:
        True if the player's calculation is correct, False otherwise.
    """
    # Create a list of 5 random numbers.
    roulette = [random.randint(1,20) for i in range(5)]
    # Choose a random operation.
    f = random.randint(0,2)
    opp = ["+","-","*"]
    print("Solve the : " + opp[f])
    
    # Calculate the expected solution by applying the operation to all roulette numbers
    reponse = 0
    for i in roulette:
        reponse = eval("reponse" + opp[f] + str(i))

    print("Numbers on the roulette: " + str(roulette))
    # Get the player's answer
    answer = int(input("Your answer: "))
    # Check if the player's answer is correct
    if answer == reponse:
        print("Correct! You win a key")
        return True
    return False

def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
        n: The number to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    """
    Finds the nearest prime number to a given number.

    Parameters:
        n: The number for which to find the nearest prime.

    Returns:
        The nearest prime number to n.
    """
    # Check if n is already a prime
    if is_prime(n):
        return n
    d = 1
    e = -1
    # Increment d until (n+d) is a prime
    while not is_prime(n + d):
        d += 1
    # Decrement e until (n+e) is a prime
    while not is_prime(n + e):
        e -= 1
    # Return the nearest prime
    if abs(d) < abs(e):
        return n + d
    else:
        return n + e
    
def math_challenge_prime():
    """
    Presents a challenge to find the nearest prime to a given number.

    Parameters:
        None

    Returns:
        True if the player's answer is correct, False otherwise.
    """
    # Generate a random number between 10 and 20
    n = random.randint(10,20)
    print("Math Challenge: Find the nearest prime to ",n)
    # Get the player's answer and check if it is correct
    ans = int(input("Your answer : "))
    if ans == nearest_prime(n):
        print("Correct! You win a key")
        return True
    return False

def math_challenge():
    """
    Selects and runs a random math challenge.

    Parameters:
        None

    Returns:
        The return value of the selected math challenge (True or False).
    """
    # List of available math challenges
    functions = [math_challenge_factorial,math_challenge_equation,math_roulette_challenge,math_challenge_prime]
    # Choose one math challenge at random
    challenge =  random.choice(functions)
    # Run the chosen challenge and return its result
    return challenge()

# with gui version (we overwrite the functions)

def solve_linear_equation():
    """
    Generates random values for a linear equation (ax + b = 0).

    Parameters:
        None

    Returns:
        A tuple containing:
        a: The coefficient of x.
        b: The constant term.
        -b/a: The solution for x.
    """
    # Generate random values for a and b.
    a = random.randint(1,10)
    b = random.randint(1,10)
    # Return the values for the linear equation.
    return a, b , -b/a

def equation_challenge():
    """
    Presents a linear equation solving challenge to the player with a graphical interface.

    Parameters:
        None

    Returns:
        True if the player's solution is correct, False otherwise.
    """
    # Create a window
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    # Generate a random equation
    a,b,c = solve_linear_equation()
    # Display a title with the equation
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Solve the following linear equation :\n"+str(a)+"x + "+ str(b)+" = 0")
    title.alignment = CENTER
    w.add(title)
    
    # Add a button to continue
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    
    # Add boxes to get the player's answer
    box_solution = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 100, 100)
    box_solution.hide_bg = True
    box_solution.borderWidth = 5
    box_solution.radius = 10
    w.add(box_solution)
    # Add labels to display the answer
    solution_text = obj.Label(obj.WIN_WIDTH/2.75, obj.WIN_HEIGHT/1.75, 0, 0, "1")
    w.add(solution_text)
    # Add a box for the second value of the answer
    solution_hover = False
    box_solution1 = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 100, 100)
    box_solution1.hide_bg = True
    box_solution1.borderWidth = 5
    box_solution1.radius = 10
    w.add(box_solution1)
    # Add labels to display the second value of the answer
    solution_text1 = obj.Label(obj.WIN_WIDTH/1.85, obj.WIN_HEIGHT/1.75, 0, 0, "1")
    w.add(solution_text1)
    # Add a label to display the slash (/)
    slash_text = obj.Label(obj.WIN_WIDTH/2.2, obj.WIN_HEIGHT/1.75, 0, 0, "/")
    w.add(slash_text)
    # Add a box for the minus sign
    box_minus = obj.Box(obj.WIN_WIDTH/5, obj.WIN_HEIGHT/2, 100, 100)
    box_minus.hide_bg = True
    box_minus.borderWidth = 5
    box_minus.radius = 100
    box_minus.backgroundColor = obj.BLACK
    w.add(box_minus)
    # Set a bool to know if the second value is selected
    solution_hover1 = False
    minus = False
    # Define a function for the checkbox
    def checkbox_listener():
        nonlocal minus
        if minus == False:
            minus = True
            box_minus.hide_bg = False
            solution_text.text = "-" + solution_text.text
        else:
            minus = False
            box_minus.hide_bg = True
            solution_text.text = solution_text.text.removeprefix("-")
    # Define a function for the keyboard
    def keyboard_listener():
        for key in range(len(obj.Object.keys)):
            value = obj.Object.keys[key]
            if value:
                if pygame.key.name(key) in ["1","2","3","4","5","6","7","8","9","0"]:
                    if solution_hover:
                        solution_text.text += pygame.key.name(key)
                    elif solution_hover1:
                        solution_text1.text += pygame.key.name(key)
                elif pygame.key.name(key) == "backspace":
                    if solution_hover:
                        solution_text.text = solution_text.text[:-1]
                    elif solution_hover1:
                        solution_text1.text = solution_text1.text[:-1]
                break
    # Define a function for the button
    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False
    # Define a function to verify which box is selected
    def solution_listener():
        nonlocal solution_hover
        if solution_hover:
            solution_hover = False
        else:
            solution_hover = True
    # Define a function to verify which box is selected
    def solution_listener1():
        nonlocal solution_hover1
        if solution_hover1:
            solution_hover1 = False
        else:
            solution_hover1 = True
    # Set a variable to know when to continue
    continuer = True
    # Assign the function to their button/checkbox
    obj.Object.onkeyboard = keyboard_listener
    box_solution.onstartfocused = solution_listener
    box_solution.onendfocused = solution_listener
    box_solution1.onstartfocused = solution_listener1
    box_solution1.onendfocused = solution_listener1
    button_continuer.onclick = button_listener
    box_minus.onclick = checkbox_listener
    # Wait while the player does not continue
    while continuer:
        w.updateAll()
    # Print the answer to verify the values
    print(c)
    print(int(solution_text.text)/int(solution_text1.text))
    # Verify if the answer is correct
    if int(solution_text.text)/int(solution_text1.text) == c:
        return True
    return False

def Factorial(n):
    """
    Calculates the factorial of a given number.

    Parameters:
        n: An integer for which the factorial is calculated.

    Returns:
        The factorial of n (n!).
    """
    # Loop to multiply each number from 1 to n.
    for i in range(1,n):
        n = n * i
    return n

def factorial_challenge():
    """
    Presents a factorial calculation challenge with a graphical interface.

    Parameters:
        None

    Returns:
        True if the player's answer is correct, False otherwise.
    """
    # Create a new window
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    # Generate a random number
    n = random.randint(1,10)
    # Calculate the factorial for verification
    factorial = Factorial(n)
    # Display a title
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Find the factorial of " + str(n))
    title.alignment = CENTER
    w.add(title)
    # Add a button to continue
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)

    box_factorial = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 600, 100)
    box_factorial.hide_bg = True
    box_factorial.borderWidth = 5
    box_factorial.radius = 10
    w.add(box_factorial)
    factorial_text = obj.Label(obj.WIN_WIDTH/1.35, obj.WIN_HEIGHT/1.75, 0, 0, "")
    w.add(factorial_text)
    factorial_hover = False
    def keyboard_listener():
            for key in range(len(obj.Object.keys)):
                        value = obj.Object.keys[key]
                        if value:
                            if pygame.key.name(key) in ["1","2","3","4","5","6","7","8","9","0"]:
                                if factorial_hover:
                                    factorial_text.text += pygame.key.name(key)
                            elif pygame.key.name(key) == "backspace":
                                if factorial_hover:
                                    factorial_text.text = factorial_text.text[:-1]

                            break
    def factorial_listener():
        nonlocal factorial_hover
        if factorial_hover:
            factorial_hover = False
        else:
            factorial_hover = True

    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False

    obj.Object.onkeyboard = keyboard_listener
    continuer = True
    box_factorial.onclick = factorial_listener
    button_continuer.onclick = button_listener
    # Wait until the player does not continue
    while continuer:
        w.updateAll()
    if int(factorial_text.text) == factorial:
        return True
    return False

def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
        n: The number to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    """
    Finds the nearest prime number to a given number.

    Parameters:
        n: The number for which to find the nearest prime.

    Returns:
        The nearest prime number to n.
    """
    # Check if n is already a prime
    if is_prime(n):
        return n
    d = 1
    e = -1
    # Increment d until (n+d) is a prime
    while not is_prime(n + d):
        d += 1
    # Decrement e until (n+e) is a prime
    while not is_prime(n + e):
        e -= 1
    # Return the nearest prime
    if abs(d) < abs(e):
        return n + d
    else:
        return n + e
    
def prime_challenge():
    """
    Presents a challenge to find the nearest prime to a given number with a graphical interface.

    Parameters:
        None

    Returns:
        True if the player's answer is correct, False otherwise.
    """
    # Create a new window
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    # Generate a random number
    n = random.randint(10,20)
    # Calculate the nearest prime for verification
    prime = nearest_prime(n)
    # Display a title
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Find the nearest prime to " + str(n))
    title.alignment = CENTER
    w.add(title)
    # Add a button to continue
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    # Set a variable to know the answer of the player
    counter = 0
    # Add a box to contain the player's answer
    counter_box = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 400, 200)
    counter_box.hide_bg = True
    counter_box.borderWidth = 5
    counter_box.radius = 10
    w.add(counter_box)
    # Create a label to display the player's answer
    number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "0")
    w.add(number_text)
    # Create a button to increment the answer
    plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
    plus_box.hide_bg = True
    plus_box.borderWidth = 5
    plus_box.radius = 10
    w.add(plus_box)
    # Create a label to display the '+' symbol
    plus_text = obj.Label(counter_box.x+counter_box.w/1.25, counter_box.y+counter_box.h/1.75, 0, 0, "+")
    w.add(plus_text)
    # Create a button to decrement the answer
    minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
    minus_box.hide_bg = True
    minus_box.borderWidth = 5
    minus_box.radius = 10
    w.add(minus_box)
    # Create a label to display the '-' symbol
    minus_text = obj.Label(counter_box.x+counter_box.w/4, counter_box.y+counter_box.h/1.75, 0, 0, "-")
    w.add(minus_text)

    w.updateAll()
    # Define a function to increment the answer
    def CounterListenerPlus():
            nonlocal number_text, counter
            counter += 1
            number_text.text = str(counter)
    # Define a function to decrement the answer
    def CounterListenerMinus():
        nonlocal number_text, counter
        if counter > 0:

            counter -= 1
            number_text.text = str(counter)
    # Define a function for the button to continue
    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False
    # Set a variable to know when to continue
    continuer = True
    # Assign the functions to their buttons
    plus_box.onclick = CounterListenerPlus
    minus_box.onclick = CounterListenerMinus
    button_continuer.onclick = button_listener
    # Wait until the player does not continue
    while continuer:
        w.updateAll()
    # Verify if the answer is correct
    if counter == prime:
        return True
    return False

def math_challenge(player):
    """
    Presents a graphical interface for selecting and playing a random math mini-game.

    Parameters:
        player: The player number who is playing this challenge (not used in the current implementation).

    Returns:
         The player number if the player wins the challenge, 0 otherwise.
    """
    # Create a new window
    win = Win()
    win.loadImage("parchemin.jpg")
    # Add a title
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Maths Challenge")
    title.alignment = CENTER
    win.add(title)
    # Add a title to inform the player if he won
    title2 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You won a key!\nDo you want to exit?")
    title2.alignment = CENTER
    title2.hide = True
    win.add(title2)
    # Add a title to inform the player if he lost
    title3 = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "You lost the game, \ndo you want to exit?")
    title3.alignment = CENTER
    title3.hide = True
    win.add(title3)
    # Add a button to select the math challenge
    button = Label(WIN_WIDTH/3, WIN_HEIGHT/2, WIN_WIDTH/3, WIN_WIDTH/8, "Choose a random \nchallenge")
    button.alignment = CENTER
    button.loadImage("small_paper.png")
    win.add(button)

    exit = Label(WIN_WIDTH/2.7, WIN_HEIGHT/2, WIN_WIDTH/4, WIN_WIDTH/8, "Exit")
    exit.alignment = CENTER
    exit.loadImage("small_paper.png")
    exit.hide = True
    win.add(exit)
    # Make the background animation
    nuage_backward(win)

    loop1 = True
    # Define a function to quit the math challenge
    def global_exit():
            nonlocal loop1
            # Sets flags to exit both loops.
            if loop1:
                loop1 = False
                history("Ended math challenge")
                nuage_forward(win)
    # Assign the function to the exit button       
    exit.onclick = global_exit
    # Define a function for the math challenges
    def btn_click():
        global result
        # Select and play a random challenge.
        win.destroy(button)
        functions = [prime_challenge,factorial_challenge,equation_challenge]
        challenge =  random.choice(functions)
        history("Started challenge " + str(challenge.__name__))
        # Show appropriate messages and buttons based on the game result.
        title.hide = True
        button.hide = True
        result = challenge()
        exit.hide = False
        if(result):
            title2.hide = False
            title3.hide = True
            button.hide = True
        else:
            title2.hide = True
            title3.hide = False
    # Assign the function to their buttons
    button.onclick = btn_click

    # Main loop for the game
    while True:
        if not loop1:
            if result:
                return player
            else:
                return 0
        win.updateAll()