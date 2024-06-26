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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

def order_coffee():
    global order
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "espresso":
        print("Making your espresso. Please wait... ")
        return order
    elif order == "latte":
        print("Making your latte. Please wait... ")
        return order

    elif order == "cappuccino":
        print("Making your cappuccino. Please wait... ")
        return order
    elif order == "off":
        turn_off()
    elif order == "report":
        print("Generating report... ")
        return order
    else:
        print("Invalid order")
        order_coffee()


def make_espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    print("Here is your espresso... Enjoy!")
    total_sale(order)
    print_report()

def make_latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    print("Here is your latte... Enjoy!")

def make_cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    print("Here is your cappuccino... Enjoy!")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

def turn_off():
    print("Turning off the coffee machine... Goodbye!")
    exit()

# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

def print_report():

    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print(f"Money: ${total_sale}")

# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(order):
    if order == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif order == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif order == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    else:
        return False

# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    global total
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def check_transaction(order, total):
    if order == "espresso":
        if total < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(total - MENU["espresso"]["cost"], 2)
            print(f"Here is ${change} in change.")
            return True
    elif order == "latte":
        if total < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(total - MENU["latte"]["cost"], 2)
            print(f"Here is ${change} in change.")
            return True
    elif order == "cappuccino":
        if total < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(total - MENU["cappuccino"]["cost"], 2)
            print(f"Here is ${change} in change.")
            return True
    else:
        return False

# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

def make_coffee(order):
    if order == "espresso":
        make_espresso()
    elif order == "latte":
        make_latte()
    elif order == "cappuccino":
        make_cappuccino()
    else:
        print("Invalid order")
        order_coffee()
        make_coffee(order)

# TODO: 8. calculate the profit from each transaction.
# a. The program should maintain a record of sale made from selling coffee when report is
# triggered.

def calculate_sale(order):
    return MENU[order]["cost"]

def total_sale(order):
    global total_sale
    total_sale = 0
    total_sale += calculate_sale(order)
    return total_sale