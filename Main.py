from Data import MENU
from Data import resources
from art import logo

coffee_machine_operates = True

#Defining necessary functions:

def report():
    for resource, value in resources.items():
        if resource == "water" or resource == "milk":
            value = str(value) + " ml"
        elif resource == "coffee":
            value = str(value) + " g"
        elif resource == "money":
            value = "$ "+ str(value)
        print(f"{resource} : {value}")

def coffee_finder(coffee):
    return MENU[coffee]

def check_resources(coffee):
    desired_coffe_ingr = coffee_finder(coffee)["ingredients"]
    for resource, value in desired_coffe_ingr.items():
        if value > resources[resource]:
            print(f"Sorry, there is not enough {resource}...")
            print("Type 'recharge' for more coffe!")

def continue_or_not(coffee):
    """Decides wheather to continue or not"""
    desired_coffee_ingr = coffee_finder(coffee)["ingredients"]
    all_ingredients_available = True

    for resource, value in desired_coffee_ingr.items():
        if value > resources[resource]:
            all_ingredients_available = False

    return all_ingredients_available

def check_coins(quarters, dimes, nickles, pennies, coffee):
    """Deals with coins"""
    inserted_coins_value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    desired_coffe_value = coffee_finder(coffee)["cost"]
    if inserted_coins_value < desired_coffe_value:
        print("Sorry, not enough money!")
        return False
    elif inserted_coins_value == desired_coffe_value:
        resources["money"] += inserted_coins_value
        print(f"Here is your {coffee}! Enjoy!")
    elif inserted_coins_value > desired_coffe_value:
        resources["money"] += desired_coffe_value
        print(f"Here is ${(inserted_coins_value - desired_coffe_value):.2f} in change!")
        print(f"Here is your {coffee}! Enjoy!")

def deduct_resources(coffe):
    desired_coffee_ingr = coffee_finder(coffe)["ingredients"]
    for ingredient, value in desired_coffee_ingr.items():
        resources[ingredient] -= value
    return resources

def recharge_resources(resources):
    """Self added function for continuing 'game', refills the machine"""
    for resource, value in resources.items():
        if resource != "money" and resource != "coffee":
            value += 300
        if resource == "coffee":
            value += 100
        resources[resource] = value

#Execution starts here

print(logo)
while coffee_machine_operates:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        coffee_machine_operates = False
        continue
    elif coffee == "report":
        report()
        continue
    elif coffee == "recharge":
        recharge_resources(resources)
        continue
    check_resources(coffee)
    if continue_or_not(coffee):
        print("Please insert coins.")
        inserted_quarters = int(input("How many quarters?"))
        inserted_dimes = int(input("How many dimes?"))
        inserted_nickles = int(input("How many nickles?"))
        inserted_pennies = int(input("How many pennies?"))

        check_coins(inserted_quarters, inserted_dimes, inserted_nickles, inserted_pennies, coffee)

        deduct_resources(coffee)
    else:
        #If wanted to end here change comment under to code
        # coffee_machine_operates = False
        print("Thank you for using machine! Sorry and please come latter!")
