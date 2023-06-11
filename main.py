MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


our_water = 300
our_milk = 200
our_coffee = 100
money_in_machine = 0


def report():
    print(f"Water: {our_water}ml")
    print(f"Milk: {our_milk}ml")
    print(f"Coffee: {our_coffee}g")
    print(f"Money: ${money_in_machine}")


def is_resources_enough(waterr, milkk, coffeee):
    return our_water >= waterr and our_milk >= milkk and our_coffee >= coffeee


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        report()
    else:
        water = MENU[choice]["ingredients"]["water"]
        milk = MENU[choice]["ingredients"]["milk"]
        coffee = MENU[choice]["ingredients"]["coffee"]
        cost = MENU[choice]["cost"]
        if is_resources_enough(water, milk, coffee):
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            money_paid = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
            if money_paid >= cost:
                our_water -= water
                our_milk -= milk
                our_coffee -= coffee
                money_in_machine += cost
                print(f"Here is ${round(money_paid - cost, 2)} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if our_water < water:
                print("Sorry there is not enough water")
            elif our_milk < milk:
                print("Sorry there is not enough milk")
            elif our_coffee < coffee:
                print("Sorry there is not enough coffee")
