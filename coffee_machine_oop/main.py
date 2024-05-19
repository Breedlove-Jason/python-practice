from menu import MENU, resources


class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee_beans = 100
        self.money = 0
        self.machine_on = True
        self.user_input = input("What would you like? (esp/lat/cap): ").lower()
        self.report()

    def make_coffee(self, user_input):
        if user_input == "esp":
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

    def machine_off(self, user_input):
        if user_input == "off":
            print("Machine is off")
            self.machine_on = False

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
