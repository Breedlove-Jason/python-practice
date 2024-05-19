from menu import resources


class Drink:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class CoinProcessor:
    def __init__(self):
        self.money = 0.0

    def process_coins(self):
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        self.money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return self.money

    def calculate_change(self, cost):
        change = round(self.money - cost, 2)
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            return False
        print(f"Here is ${change} in change.")
        self.money = 0  # Reset money after giving change
        return True


class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.money = 0
        self.machine_on = True
        self.coin_processor = CoinProcessor()
        self.drinks = {
            "esp": Drink("espresso", 50, 0, 18, 1.5),
            "lat": Drink("latte", 200, 150, 24, 2.5),
            "cap": Drink("cappuccino", 250, 100, 24, 3.0)
        }

    def check_resources(self, drink):
        if self.resources['water'] < drink.water:
            print("Sorry there is not enough water.")
            return False
        if self.resources['milk'] < drink.milk:
            print("Sorry there is not enough milk.")
            return False
        if self.resources['coffee'] < drink.coffee:
            print("Sorry there is not enough coffee.")
            return False
        return True

    def deduct_resources(self, drink):
        self.resources['water'] -= drink.water
        self.resources['milk'] -= drink.milk
        self.resources['coffee'] -= drink.coffee

    def make_coffee(self, user_input):
        if user_input in self.drinks:
            drink = self.drinks[user_input]
            if self.check_resources(drink):
                self.money = self.coin_processor.process_coins()
                if self.coin_processor.calculate_change(drink.cost):
                    self.deduct_resources(drink)
                    print(f"Here is your {drink.name}. Enjoy!")
        else:
            print("Invalid selection")

    def machine_off(self, user_input):
        if user_input == "off":
            print("Machine is off")
            self.machine_on = False

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee Beans: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")


# Initialize the coffee machine
coffee_machine = CoffeeMachine()

while coffee_machine.machine_on:
    user_input = input("What would you like? (esp/lat/cap): ").lower()
    coffee_machine.report()
    coffee_machine.machine_off(user_input)
    if coffee_machine.machine_on:
        coffee_machine.make_coffee(user_input)
