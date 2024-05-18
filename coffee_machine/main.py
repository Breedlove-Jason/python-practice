from menu import MENU, resources

coffee_choice = input("What would you like? (esp/lat/cap): ").lower()

water = MENU[coffee]["ingredients"]["water"]
milk = MENU[coffee]["ingredients"]["milk"]
coffee = MENU[coffee]["ingredients"]["coffee"]


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
