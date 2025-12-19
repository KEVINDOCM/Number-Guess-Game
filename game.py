import random


def easy():
    numbergen = random.randrange(1, 101)
    chance = 5
    attempts = 0
    print("GREAT! EASY LEVEL CHOICE.")
    while chance > 0:
        try:
            usernum = int(input("ENTER YOUR NUMBER GUESS: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if usernum > numbergen:
            chance -= 1
            print(f"Incorrect! The number is lower than {usernum}")
            print(f"CHANCE REMAIN: {chance}")
        elif usernum < numbergen:
            chance -= 1
            print(f"Incorrect! The number is higher than {usernum}")
            print(f"CHANCE REMAIN: {chance}")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return
    print(f"Sorry, you've used all your chances. The number was {numbergen}.")


def medium():
    numbergen = random.randrange(1, 101)
    chance = 3
    attempts = 0
    print("MEDIUM LEVEL CHOICE.")
    while chance > 0:
        try:
            usernum = int(input("ENTER YOUR NUMBER GUESS: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if usernum > numbergen:
            chance -= 1
            print(f"Incorrect! The number is lower than {usernum}")
            print(f"CHANCE REMAIN: {chance}")
        elif usernum < numbergen:
            chance -= 1
            print(f"Incorrect! The number is higher than {usernum}")
            print(f"CHANCE REMAIN: {chance}")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            return
    print(f"Sorry, you've used all your chances. The number was {numbergen}.")


def hard():
    numbergen = random.randrange(1, 101)
    chance = 1
    attempts = 0
    print("HARD LEVEL CHOICE.")
    while chance > 0:
        try:
            usernum = int(input("ENTER YOUR NUMBER GUESS: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        if usernum == numbergen:
            print(f"Congratulations! You guessed the correct number in {attempts} attempt(s).")
            return
        else:
            chance -= 1
            print("Incorrect!")
            print(f"CHANCE REMAIN: {chance}")
    print(f"Sorry, you've used all your chances. The number was {numbergen}.")