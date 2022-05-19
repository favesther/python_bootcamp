from data import menu, resources
resources["money"] = 0
valid_input = ["espresso", "latte", "cappuccino", "report", "off"]


def is_resource_sufficient():
    for ingredients in menu[order]["ingredients"]:
        if menu[order]["ingredients"][ingredients] > resources[ingredients]:
            print(f"Sorry, there is not enough {ingredients}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    q = int(input("how many quarters?\t"))
    d = int(input("how many dimes?\t"))
    n = int(input("how many nickles?\t"))
    p = int(input("how many pennies?\t"))
    paid = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return round(paid - menu[order]["cost"],2)


def make_coffee(order):
    for i in menu[order]["ingredients"]:
        resources[i] -= menu[order]["ingredients"][i]
    print(f"Here is your {order} ☕. Enjoy!")


while True:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
    order = input("What would you like? (espresso/latte/cappuccino)\t")
    while order not in valid_input:
        print("Invalid Input. Try again.")
        order = input("What would you like? (espresso/latte/cappuccino)\t")
    # TODO: 2.Turn off the Coffee Machine by entering “off” to the prompt.
    if order == "off":
        quit()
    # TODO: 3. Print report of all coffee machine resources
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    # TODO: 4. Check resources sufficient

    # TODO: 5. Process coins
    else:
        if is_resource_sufficient():
            change = process_coins()
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["money"] += menu[order]["cost"]
                print(f"Here is ${change} in change.")
                make_coffee(order)
