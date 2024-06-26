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

# Function to initialize and get total sales amount
def total_sale():
    if not hasattr(total_sale, 'total_sale_amount'):
        total_sale.total_sale_amount = 0
    return total_sale.total_sale_amount

# Function to add to the total sales amount
def add_sale(amount):
    if not hasattr(total_sale, 'total_sale_amount'):
        total_sale.total_sale_amount = 0
    total_sale.total_sale_amount += amount

def order_coffee():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        turn_off()
    elif order == "report":
        return order
    elif order in MENU:
        print(f"Making your {order}. Please wait... ")
        return order
    else:
        print("Invalid order")
        order_coffee()

def make_espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    print("Here is your espresso... Enjoy!")

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

def turn_off():
    print("Turning off the coffee machine... Goodbye!")
    exit()

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_sale()}")

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

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def check_transaction(order, total):
    cost = MENU[order]["cost"]
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        add_sale(cost)
        return True

def calculate_sale(order):
    return MENU[order]["cost"]

def make_coffee(order):
    if order == "espresso":
        make_espresso()
    elif order == "latte":
        make_latte()
    elif order == "cappuccino":
        make_cappuccino()

def main():
    while True:
        order = order_coffee()
        if order == "off":
            turn_off()
        elif order == "report":
            print_report()
        elif order in MENU:  # Ensure the order is a valid drink option
            if check_resources(order):
                m_total = process_coins()
                if check_transaction(order, m_total):
                    make_coffee(order)
                    print_report()
            else:
                print("Sorry. Code not working properly.")
        else:
            print("Invalid option. Please try again.")

main()
