import random
def Factorial(n):
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
    return challenge()
