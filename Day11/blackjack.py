############### Blackjack Project #####################

import random
from art import logo
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(lst):
    if len(lst) == 2 and sum(lst) == 21:
        return 0
    if sum(lst) > 21 and 11 in lst:
        lst[lst.index(11)] = 1
    return sum(lst)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack!"
    elif user_score == 0:
        return "You win, you have blackjack!"
    elif user_score > 21:
        return "Lose, you went over!"
    elif computer_score > 21:
        return "You win, computer went over!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    print(
        f"Your final hand is {user_cards} and your final score is: {user_score}")
    print(
        f"Computer's final hand is {computer_cards} and computer's final score is: {computer_score}")
    print(compare(user_score, computer_score))

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play_game()
