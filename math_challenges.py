import random
from Utils import *
from graphics.objects import *
"""def Factorial(n):
    for i in range(1,n):
        n = n * i
    return n

def math_challenge_factorial():
    n = random.randint(1,10)
    print("Math Challenge: Calculate the factorial of ",n)
    p = int(input("Your answer is : "))
    if p == Factorial(n):
        print("Correct! You win a key")
        return True
    return False

def solve_linear_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    return a, b , -b/a

def math_challenge_equation():
    a,b,c = solve_linear_equation()
    print("Math Challenge: Solve the linear equation ",a,"x + ",b," = 0")
    
    x = float(eval(input("What is the value of x: ")))
    if x == c:
        print("Correct! You win a key")
        return True
    return False

def math_roulette_challenge():
    roulette = [random.randint(1,20) for i in range(5)]
    f = random.randint(0,2)
    opp = ["+","-","*"]
    print("Solve the : " + opp[f])
    reponse = 0
    for i in roulette:
        reponse = eval("reponse" + opp[f] + str(i))
    print("Numbers on the roulette: " + str(roulette))
    answer = int(input("Your answer: "))
    if answer == reponse:
        print("Correct! You win a key")
        return True
    return False

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    if is_prime(n):
        return n
    d = 1
    e = -1
    while not is_prime(n + d):
        d += 1
    while not is_prime(n + e):
        e -= 1
    if abs(d) < abs(e):
        return n + d
    else:
        return n + e
    
def math_challenge_prime():
    n = random.randint(10,20)
    print("Math Challenge: Find the nearest prime to ",n)
    ans = int(input("Your answer : "))
    if ans == nearest_prime(n):
        print("Correct! You win a key")
        return True
    return False

def math_challenge():
    functions = [math_challenge_factorial,math_challenge_equation,math_roulette_challenge,math_challenge_prime]
    challenge =  random.choice(functions)
    return challenge()"""
def solve_linear_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    return a, b , -b/a
def equation_challenge():
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    a,b,c = solve_linear_equation()
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Solve the following linear equation :\n"+str(a)+"x + "+ str(b)+" = 0")
    title.alignment = CENTER
    w.add(title)
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    
    box_solution = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 100, 100)
    box_solution.hide_bg = True
    box_solution.borderWidth = 5
    box_solution.radius = 10
    w.add(box_solution)
    solution_text = obj.Label(obj.WIN_WIDTH/2.75, obj.WIN_HEIGHT/1.75, 0, 0, "1")
    w.add(solution_text)
    solution_hover = False
    box_solution1 = obj.Box(obj.WIN_WIDTH/2, obj.WIN_HEIGHT/2, 100, 100)
    box_solution1.hide_bg = True
    box_solution1.borderWidth = 5
    box_solution1.radius = 10
    w.add(box_solution1)
    solution_text1 = obj.Label(obj.WIN_WIDTH/1.85, obj.WIN_HEIGHT/1.75, 0, 0, "1")
    w.add(solution_text1)
    slash_text = obj.Label(obj.WIN_WIDTH/2.2, obj.WIN_HEIGHT/1.75, 0, 0, "/")
    w.add(slash_text)
    box_minus = obj.Box(obj.WIN_WIDTH/5, obj.WIN_HEIGHT/2, 100, 100)
    box_minus.hide_bg = True
    box_minus.borderWidth = 5
    box_minus.radius = 100
    box_minus.backgroundColor = obj.BLACK
    w.add(box_minus)
    solution_hover1 = False
    minus = False
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
    
    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False
    def solution_listener():
        nonlocal solution_hover
        if solution_hover:
            solution_hover = False
        else:
            solution_hover = True
    def solution_listener1():
        nonlocal solution_hover1
        if solution_hover1:
            solution_hover1 = False
        else:
            solution_hover1 = True
    continuer = True
    obj.Object.onkeyboard = keyboard_listener
    box_solution.onstartfocused = solution_listener
    box_solution.onendfocused = solution_listener
    box_solution1.onstartfocused = solution_listener1
    box_solution1.onendfocused = solution_listener1
    button_continuer.onclick = button_listener
    box_minus.onclick = checkbox_listener
    while continuer:
        w.updateAll()
    print(c)
    print(int(solution_text.text)/int(solution_text1.text))

    if int(solution_text.text)/int(solution_text1.text) == c:
        return True
    return False
def Factorial(n):
    for i in range(1,n):
        n = n * i
    return n
def factorial_challenge():
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    n = random.randint(1,10)
    factorial = Factorial(n)
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Find the factorial of " + str(n))
    title.alignment = CENTER
    w.add(title)
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
    while continuer:
        w.updateAll()
    if int(factorial_text.text) == factorial:
        return True
    return False
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def nearest_prime(n):
    if is_prime(n):
        return n
    d = 1
    e = -1
    while not is_prime(n + d):
        d += 1
    while not is_prime(n + e):
        e -= 1
    if abs(d) < abs(e):
        return n + d
    else:
        return n + e
def prime_challenge():
    w = obj.Win()
    w.loadImage("parchemin.jpg")
    n = random.randint(10,20)
    prime = nearest_prime(n)
    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Find the nearest prime to " + str(n))
    title.alignment = CENTER
    w.add(title)
    button_continuer = obj.Box(obj.WIN_WIDTH/1.3, obj.WIN_HEIGHT/1.25, 200, 100)
    button_continuer.borderWidth = 5
    button_continuer.radius = 10
    button_continuer.hide_bg = True
    continuer_text = obj.Label(0, 0, 200, 100, "Continue")
    button_continuer.add(continuer_text)
    w.add(button_continuer)
    counter = 0
    counter_box = obj.Box(obj.WIN_WIDTH/3, obj.WIN_HEIGHT/2, 400, 200)
    counter_box.hide_bg = True
    counter_box.borderWidth = 5
    counter_box.radius = 10
    w.add(counter_box)
    number_text = obj.Label(counter_box.x+counter_box.w/2, counter_box.y+counter_box.h/2, 0, 0, "0")
    w.add(number_text)
    plus_box = obj.Box(counter_box.x+counter_box.w/1.5, counter_box.y+counter_box.h/3.25, 100, 100)
    plus_box.hide_bg = True
    plus_box.borderWidth = 5
    plus_box.radius = 10
    w.add(plus_box)
    plus_text = obj.Label(counter_box.x+counter_box.w/1.25, counter_box.y+counter_box.h/1.75, 0, 0, "+")
    w.add(plus_text)
    minus_box = obj.Box(counter_box.x+counter_box.w/8, counter_box.y+counter_box.h/3.25, 100, 100)
    minus_box.hide_bg = True
    minus_box.borderWidth = 5
    minus_box.radius = 10
    w.add(minus_box)
    minus_text = obj.Label(counter_box.x+counter_box.w/4, counter_box.y+counter_box.h/1.75, 0, 0, "-")
    w.add(minus_text)
    w.updateAll()
    def CounterListenerPlus():
            nonlocal number_text, counter
            counter += 1
            number_text.text = str(counter)

    def CounterListenerMinus():
        nonlocal number_text, counter
        if counter > 0:

            counter -= 1
            number_text.text = str(counter)

    def button_listener():
        nonlocal continuer
        if continuer:
            continuer = False

    continuer = True
    plus_box.onclick = CounterListenerPlus
    minus_box.onclick = CounterListenerMinus
    button_continuer.onclick = button_listener
    while continuer:
        w.updateAll()
    if counter == prime:
        return True
    return False

def math_challenge(player):
    # Presents a graphical interface for selecting and playing a random mini-game.
    # Parameters: None
    # Returns: None. This function manages the game flow and doesn't directly return a meaningful value.
    win = Win()
    win.loadImage("parchemin.jpg")

    title = Label(WIN_WIDTH/2, WIN_HEIGHT/4, 20, 20, "Maths Challenge")
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

    exit = Label(WIN_WIDTH/2.7, WIN_HEIGHT/2, WIN_WIDTH/4, WIN_WIDTH/8, "Exit")
    exit.alignment = CENTER
    exit.loadImage("small_paper.png")
    exit.hide = True
    win.add(exit)
    nuage_backward(win)

    loop1 = True
    def global_exit():
            nonlocal loop1
            # Sets flags to exit both loops.
            if loop1:
                loop1 = False
                nuage_forward(win)
            
            
    exit.onclick = global_exit

    def btn_click():
        global result
        # Select and play a random challenge.
        win.destroy(button)
        functions = [prime_challenge,factorial_challenge,equation_challenge]
        challenge =  random.choice(functions)
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

    button.onclick = btn_click


    while True:
        if not loop1:
            if result:
                return player
            else:
                return 0
        win.updateAll()
