# Tip Calculator
# Project 2

bill = float(input("Enter total bill amount: "))
tip = int(input("Enter tip amount (percentage): "))
total_people = int(input("How many people splitting bill: "))
total_bill = bill * (1+tip/100)
total_per_person = total_bill/total_people
formatted_bill = "{:.2f}".format(total_per_person)
print(f"Each person will pay ${formatted_bill}")
