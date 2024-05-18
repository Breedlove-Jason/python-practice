from menu import MENU, resources

machine_on = True

coffee = input("What would you like? (esp/lat/cap): ").lower()


def coffee_resources(coffee_type):
    # initialized values: "water": 300, "milk": 200, "coffee": 100,
    water = resources["water"]
    milk = resources["milk"]
    coffee_strength = resources["coffee"]

    if coffee_type == "esp":
        water -= 50
        coffee_strength -= 18
        return water, coffee_strength
    elif coffee_type == "lat":
        water -= 200
        milk -= 150
        coffee_strength -= 24
        return water, milk, coffee_strength
    elif coffee_type == "cap":
        water -= 250
        milk -= 100
        coffee_strength -= 24
        return water, milk, coffee_strength


def coins(coffee_type):
    if coffee_type == "esp":
        coffee_type = 'espresso'
    elif coffee_type == "lat":
        coffee_type = 'latte'
    elif coffee_type == "cap":
        coffee_type = 'cappuccino'
    coffee_cost = MENU[coffee_type]["cost"]

    print(f"Your total is {coffee_cost}.")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    change = round(total - coffee_cost, 2)

    if coffee_cost > total:
        print("Sorry, that's not enough money. Money refunded.")
        return
    elif coffee_cost < total:
        print(f"Here is your change: ${change:.2f}")
        return change


# drink = coffee_resources(coffee)
# print(drink)
print(coins(coffee))