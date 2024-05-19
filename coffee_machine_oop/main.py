from menu import resources


class CoffeeMachine:
    def __init__(self):
        self.water = resources['water']
        self.milk = resources['milk']
        self.coffee = resources['coffee']
        self.money = 0
        self.machine_on = True
        self.user_input = input("What would you like? (esp/lat/cap): ").lower()

    def check_resources(self, user_input):
        if user_input == "esp":
            required_milk = 0
            required_water = 50
            required_coffee = 18
        elif user_input == "lat":
            required_milk = 150
            required_water = 200
            required_coffee = 24
        elif user_input == "cap":
            required_milk = 100
            required_water = 250
            required_coffee = 24
        else:
            print("Invalid input")
            return False

        # Check if resources are sufficient
        if (self.water < required_water or self.milk < required_milk or self.coffee < required_coffee):
            print(f"Sorry there is not enough resources to make {user_input}")
            return False

        # Deduct the resources
        self.water -= required_water
        self.milk -= required_milk
        self.coffee -= required_coffee
        return True

    def check_money(self, money, cost):
        if money < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        return True

    def make_coffee(self, user_input):
        if self.check_resources(user_input):
            self.process_coins(user_input)
            if self.check_money(self.money, self.cost):
                self.calculate_change()
                print(f"Here is your {user_input}. Enjoy!")
            else:
                self.money = 0  # Reset the money if not enough
        else:
            self.money = 0  # Reset the money if resources are not enough

    def process_coins(self, user_input):
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        self.money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        if user_input == "esp":
            self.cost = 1.5
        elif user_input == "lat":
            self.cost = 2.5
        elif user_input == "cap":
            self.cost = 3.0
        else:
            self.cost = 0

    def calculate_change(self):
        change = round(self.money - self.cost, 2)
        print(f"Here is ${change} in change.")
        self.money = 0  # Reset money after giving change

    def machine_off(self, user_input):
        if user_input == "off":
            print("Machine is off")
            self.machine_on = False

    def report(self, user_input):
        if user_input == "report":
            print(f"Water: {self.water}ml")
            print(f"Milk: {self.milk}ml")
            print(f"Coffee Beans: {self.coffee}g")
            print(f"Money: ${self.money}")


# Initialize the coffee machine
coffee_machine = CoffeeMachine()
while coffee_machine.machine_on:
    coffee_machine.report(coffee_machine.user_input)
    coffee_machine.machine_off(coffee_machine.user_input)
    if coffee_machine.machine_on:
        coffee_machine.make_coffee(coffee_machine.user_input)
        coffee_machine.user_input = input("What would you like? (esp/lat/cap): ").lower()
