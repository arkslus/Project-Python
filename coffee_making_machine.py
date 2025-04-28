MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

# initialize profit and resources
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Create a function to check if the user has enough resources for the requested coffee
def check_resources(order_ingredients):
    """Checks if the user has enough resources for the requested coffee."""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, we don't have enough {ingredient}")
            return False
    return True


# Create a function to check if the user has enough money for the requested coffee
def check_money(money_required, order_cost):
    """Checks if the user has enough money for the requested coffee."""
    if money_required >= order_cost:
        change = round(money_required - order_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += order_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Create a function to process coins and make the coffee
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Write a function to make coffee
def make_coffee(drink_type, order_recipe):
    """Simulates making a coffee."""
    for item in order_recipe:
        resources[item] -= order_recipe[item]
    print(f"Here is your {drink_type} ☕️. Enjoy!")


while True:
    # Ask the user the type of coffee they'd like to make: espresso, latte, or cappuccino
    order = input(
        "\nType 'off' to turn off the machine.\nType 'report' to see the current inventory."
        "\nWhat type of coffee would you like to make? (espresso, latte, cappuccino): "
    )

    # turn off the machine by entering 'off'
    if order.lower() == "off":
        print("Machine turned off.")
        break
    # generate a report of the current inventory
    elif order.lower() == "report":
        print(
            f"\nCurrent inventory:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit:.2f}"
        )
    else:
        drink = MENU[order.lower()]
        print(f"\nMaking {order} coffee...")
        # call the check resources function
        if check_resources(drink["ingredients"]):
            # Process the coins and make the coffee
            total_money = process_coins()
            # call the check money function
            if check_money(total_money, drink["cost"]):
                # call the coffee making function
                make_coffee(order, drink["ingredients"])
