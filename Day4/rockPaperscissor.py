import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("Enter 0 for rock, 1 for paper, or 2 for scissors: "))
choices = [rock, paper, scissors]
computer_choice = random.choice(choices)

print(f"You chose:\n{choices[user_input]}")
print(f"Computer chose:\n{choices[choices.index(computer_choice)]}")

if user_input == 0 and choices.index(computer_choice) == 1:
    print("You lose")
elif user_input == 0 and choices.index(computer_choice) == 2:
    print("You win")
elif user_input == 1 and choices.index(computer_choice) == 0:
    print("You win")
elif user_input == 1 and choices.index(computer_choice) == 2:
    print("You lose")
elif user_input == 2 and choices.index(computer_choice) == 0:
    print("You lose")
elif user_input == 2 and choices.index(computer_choice) == 1:
    print("You win")
else:
    print("Draw")
