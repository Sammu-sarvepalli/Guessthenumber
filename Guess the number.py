print("Guess The Number Challenge Game!")
import random
Easy_Level_Attempts = 5
Hard_Level_Attempts = 10
def difficulty(level):
    if level =="Easy".lower():
        return Easy_Level_Attempts
    else:
        return Hard_Level_Attempts

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low!")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high!")
        return attempts -1 
    else:
        print(f"Your guess is right.The answer was {answer}")

def game():
    print("Guess the number between 1 to 100")
    answer = random.randint(1,50)
    level = input("Choose the difficulty level....\nType 'Easy' or 'Hard': ")
    attempts = difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} remaining to guess the number")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print(f"Your out of guess.You loose!The answer is {answer}")
            return
        elif guessed_number!= answer:
            print("Guess again")

game()