from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
valid_input = ["espresso", "latte", "cappuccino", "report", "off"]

menu = Menu()
while True:
    order_name = input(f"What would you like? {menu.get_items()}\t")
    while order_name not in valid_input:
        print("Invalid Input. Try again.")
        order_name = input(f"What would you like? {menu.get_items()}\t")
    if order_name == "off":
        quit()
    elif order_name == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(order_name)
        if drink:
            if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)



