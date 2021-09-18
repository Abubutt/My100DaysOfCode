# Number Guessing Game
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def easy_game():
    guesses = EASY_LEVEL_TURNS
    actual_guess = random.randint(1, 100)
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < actual_guess:
            guesses -= 1
            print("Too low")
            if guesses > 0:
                print("Guess again.")
        elif guess > actual_guess:
            guesses -= 1
            print("Too high")
            if guesses > 0:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {actual_guess}")
            return
    print("You've run out of guesses. You lose.")


def hard_game():
    guesses = HARD_LEVEL_TURNS
    actual_guess = random.randint(1, 100)
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < actual_guess:
            guesses -= 1
            print("Too low")
            if guesses > 0:
                print("Guess again.")
        elif guess > actual_guess:
            guesses -= 1
            print("Too high")
            if guesses > 0:
                print("Guess again.")
        else:
            print(f"You got it! The answer was {actual_guess}")
            return
    print("You've run out of guesses. You lose.")


print(logo)
print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    easy_game()
else:
    hard_game()
