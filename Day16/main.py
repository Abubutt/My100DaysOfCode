from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_machine_on:
    options = menu.get_items()
    item = input(f"What would you like? ({options}): ")

    if item == "off":
        is_machine_on = False
    elif item == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(item)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
