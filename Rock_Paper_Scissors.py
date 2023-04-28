import random
import time


def your_turn():
    while True:
        guess_c = random.randint(1, 3)
        a = ""
        if guess_c == 1:
            a = "Rock"
        if guess_c == 2:
            a = "Paper"
        if guess_c == 3:
            a = "Scissors"
        print(f"I chose {a}")

        b = float(input("Enter '1' for Rock, '2' for Paper, '3' for Scissors: "))
        if b != 1:
            if b != 2:
                if b != 3:
                    print("Invalid Input")
                    return
        c = ""
        if b == 1:
            c = "Rock"

        if b == 2:
            c = "Paper"
        if b == 3:
            c = "Scissors"

        if c == a:
            print("Its a DRAW")
        if a == "Rock" and c == "Paper":
            print("Yay! You Won")
        if a == "Scissors" and c == "Rock":
            print("Yay! You Won")
        if a == "Paper" and c == "Scissors":
            print("Yay! You Won")
        if a == "Scissors" and b == "Paper":
            print("You Lose!")
        if a == "Rock" and c == "Scissors":
            print("You Lose!")
        if a == "Paper" and c == "Rock":
            print("You Lose!")
        return


your_turn()

while True:
    user_input = input("Do you want to continue Playing? (Y/N) ")
    if user_input == "Y" or user_input == "y":
        your_turn()
    elif user_input == "N" or user_input == "n":
        break
    else:
        print("Invalid Input")
        break
