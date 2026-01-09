MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def resource_usage(item,cost):
    resources["water"] -= MENU[item]["ingredients"]["water"]
    resources["milk"] -= MENU[item]["ingredients"]["milk"]
    resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
    resources["money"] += cost

def resource_available(item):
    if resources["water"]>MENU[item]["ingredients"]["water"]:
        if resources["milk"] > MENU[item]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[item]["ingredients"]["coffee"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def cost_of(item):
    cost=MENU[item]["cost"]
    print(f"The cost of {item} is ${cost}")
    print("Insert Coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies= int(input("Pennies: "))
    total_coins=round((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01),2)
    if total_coins<MENU[item]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(total_coins-cost,2)
        resource_usage(item,cost)
        if change!=0:
            print(f"Here's your change: ${change}")
        print(f"Here's your {item} ☕. Enjoy 😁")




def check_input():
    while True:
        item = input("What would you like? (espresso/latte/cappuccino):").lower()
        if item=="off":
            print("Powering Off...\nGoodbye")
            
            break
        elif item=="report":
            print(f"Water: {resources["water"]}")
            print(f"Milk: {resources["milk"]}")
            print(f"Coffee: {resources["coffee"]}")
            print(f"Money: ${resources["money"]}")
        elif item=="espresso" or item=="cappuccino" or item=="latte":
            if resource_available(item):
                cost_of(item)
            else:
                print("Resource's not available, Sorry:(")
                break





check_input()


