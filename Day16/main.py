from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_machine_on:
    item = input("What would you like? (espresso/latte/cappuccino): ")
    if item == "espresso":
        item = menu.menu[1]
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
    elif item == "latte":
        item = menu.menu[0]
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
    elif item == "cappuccino":
        item = menu.menu[2]
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
    elif item == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        is_machine_on = False
