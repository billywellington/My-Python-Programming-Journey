from my_functions import MENU, resources, order_coffee, make_espresso, make_latte, make_cappuccino, turn_off, total_sale
from my_functions import check_resources, check_transaction, make_coffee, print_report, process_coins, calculate_sale
from art import welcome_msg

print(welcome_msg)

def main():
    while True:
        order = order_coffee()
        if order == "off":
            turn_off()
        elif order == "report":
            print_report()
        elif check_resources(order):
            m_total = process_coins()
            if check_transaction(order, m_total):
                make_coffee(order)
                print_report()

            else:
                continue
        else:
            print("Sorry. Code not working properly.")
            continue

main()