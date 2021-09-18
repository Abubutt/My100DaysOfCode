############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): -> range(1,21)
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) -> randint(0,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: -> year >=1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") str(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.") -> f"You can drive at age {age}."

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) -> change == to = for assgining
# total_words = pages * word_per_page
# print(total_words) -> returns zero must fix line 32

# #Use a Debugger
# def mutate(a_list): -> use python tutor as debugger
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) -> indent line 41 so it is in the for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])
