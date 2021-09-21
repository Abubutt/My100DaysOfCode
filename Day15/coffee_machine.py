from menu_resources import MENU, resources

# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]
# money = 0


def update_resources(item, water, milk, coffee):
    water -= item["ingredients"]["water"]
    milk -= item["ingredients"]["milk"]
    coffee -= item["ingredients"]["coffee"]
    return water, milk, coffee


def check_resources(item, water, milk, coffee):
    if item["ingredients"]["water"] > water:
        print("Sorry there is not enough water.")
        return False
    elif item["ingredients"]["milk"] > milk:
        print("Sorry there is not enough milk.")
        return False
    elif item["ingredients"]["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def transaction(item, money, user_choice):
    item_price = item["cost"]
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total_amount = (quarters*0.25) + (dimes*0.10) + \
        (nickels*0.05) + (pennies*0.01)
    if total_amount >= item_price:
        change = total_amount - item_price
        money += item_price
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {user_choice} ☕️. Enjoy!")
        return money
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def print_report(water, milk, coffee, money):
    print(
        f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def start_machine():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    machine_off = False
    while not machine_off:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ")
        item = user_choice
        if item == "espresso":
            item = MENU["espresso"]
            if check_resources(item, water, milk, coffee):
                add_money = transaction(item, money, user_choice)
                if add_money > 0:
                    money += add_money
                    water, milk, coffee = update_resources(
                        item, water, milk, coffee)
        elif item == "latte":
            item = MENU["latte"]
            if check_resources(item, water, milk, coffee):
                add_money = transaction(item, money, user_choice)
                if add_money > 0:
                    money += add_money
                    water, milk, coffee = update_resources(
                        item, water, milk, coffee)
        elif item == "cappucino":
            item = MENU["cappucino"]
            if check_resources(item, water, milk, coffee):
                add_money = transaction(item, money, user_choice)
                if add_money > 0:
                    money += add_money
                    water, milk, coffee = update_resources(
                        item, water, milk, coffee)
        elif item == "report":
            print_report(water, milk, coffee, money)
        else:
            machine_off = True


start_machine()
