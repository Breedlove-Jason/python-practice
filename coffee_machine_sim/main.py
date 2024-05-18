from menu import MENU, resources

machine_on = True


print(f"water: ${water} milk: ${milk} coffee ${coffee}")
coffee_machine = input("What would you like? (esp/lat/cap): ").lower()
while machine_on:
    if coffee_machine == "off":
        print("Machine is off")
        machine_on = False

    elif coffee_machine == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")


def coffee_resources(coffee_type):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if coffee_type == "esp":
        water -= 50
        coffee -= 18
        return water, coffee
    elif coffee_type == "lat":
        water -= 200
        milk -= 150
        coffee -= 24
        return water, milk, coffee
    elif coffee_type == "cap":
        water -= 250
        milk -= 100
        coffee -= 24
        return water, milk, coffee


def choose_coffee(coffee):
    if coffee == "esp":
        print("espresso")
    elif coffee == "lat":
        print("latte")
    elif coffee == "cap":
        print("cappuccino")


def resource_values(water_ml, milk_ml, coffee_grams):
    print(f"Water: {water_ml}ml")
    print(f"Milk: {milk_ml}ml")
    print(f"Coffee: {coffee_grams}g")


choose_coffee(coffee_choice)
