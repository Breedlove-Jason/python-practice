from menu import resources


def check_resources():
    for resource in resources:
        if resources[resource] < 0:
            print(f"Sorry there is not enough {resource}")
            return False
        else:
            return True


class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee_beans = 100
        self.money = 0
        self.cost = 0
        self.machine_on = True
        self.user_input = input("What would you like? (esp/lat/cap): ").lower()
        check_resources()

    def make_coffee(self, user_input):
        if self.user_input == "esp":
            self.water -= 50
            self.coffee_beans -= 18
            print("Here is your espresso")
        elif user_input == "lat":
            self.water -= 200
            self.milk -= 150
            self.coffee_beans -= 24
            print("Here is your latte")
        elif user_input == "cap":
            self.water -= 250
            self.milk -= 100
            self.coffee_beans -= 24
            print("Here is your cappuccino")

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

        if self.money < self.cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = self.money - self.cost
            print(f"Here is ${change} in change.")
            self.money = 0
            return True

    def machine_off(self, user_input):
        if user_input == "off":
            print("Machine is off")
            self.machine_on = False

    def report(self, user_input):
        if user_input == "report":
            print(f"Water: {self.water}ml")
            print(f"Milk: {self.milk}ml")
            print(f"Coffee Beans: {self.coffee_beans}g")

        while self.machine_on:
            self.user_input = input("What would you like? (esp/lat/cap): ").lower()
            # self.report(self.user_input)
            # check_resources()
            self.make_coffee(self.user_input)
            self.process_coins(self.user_input)
            # self.machine_off(self.user_input)


coffee_machine = CoffeeMachine()
