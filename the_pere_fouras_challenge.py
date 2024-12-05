import json
import random
def load_riddles(file):
    with open(file,"r") as f:
        riddles = json.load(f)
    return riddles
def pere_fouras_riddles():
    riddles = load_riddles("PFRiddles.json")
    riddle = random.choice(riddles)
    while riddle["type"] != "Key":
        riddle = random.choice(riddles)
    attempt = 3
    while attempt > 0:
        print("Riddle: ",riddle["question"])
        answer = str(input("Your answer: ")).lower()
        if answer == riddle["answer"].lower():
            print("Correct! You win a key")
            return True
        attempt -= 1
        if attempt > 0:
            print("Wrong! You have ",attempt," attempts left")
        else:
            print("You lost the game, the answer was: ",riddle["answer"])
            return False

        