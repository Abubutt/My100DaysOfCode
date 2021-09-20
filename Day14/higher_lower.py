from game_data import data
from art import logo, vs
import random
import os


def compare(choice, curr, compare_against, points, game_is_over):
    """Compares the players choice with the other choice and updates game_is_over, 'Compare A' and points. Returns points and game_is_over."""
    if choice == curr and choice["follower_count"] >= compare_against["follower_count"]:
        curr = compare_against
        points += 1
    elif choice == compare_against and choice["follower_count"] >= curr["follower_count"]:
        curr = compare_against
        points += 1
    else:
        os.system("clear")
        game_is_over = True
    return points, game_is_over


def play_game():
    """Starts the game and intializes all variables and print statements. Returns the total amount of points player has recieved."""
    points = 0
    curr = random.choice(data)
    game_is_over = False
    while not game_is_over:
        os.system("clear")
        print(logo)
        compare_against = random.choice(data)
        if points > 0:
            print(f"You're right! Current score: {points}.")
        print("Compare A: " + curr["name"] + ", a " +
              curr["description"] + ", from " + curr["country"]+".")
        print("\n" + vs + "\n")
        print("Against B: " + compare_against["name"] + ", a " +
              compare_against["description"] + ", from " + compare_against["country"]+".")
        if input("Who has more followers? Type 'A' or 'B': ") == "A":
            choice = curr
        else:
            choice = compare_against

        points, game_is_over = compare(
            choice, curr, compare_against, points, game_is_over)
    return points


points = play_game()
print(f"{logo} \n Sorry that's wrong, Final Score: {points} \n")
