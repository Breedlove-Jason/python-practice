from menu import resources


def check_resources():
    for resource in resources:
        if resources[resource] < 0:
            print(f"Sorry there is not enough {resource}")
            return False

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
        if self.user_input == "esp" and check_resources():
            self.water -= 50
            self.coffee_beans -= 18
            self.process_coins(self.user_input)
            if self.money < self.cost:
                print("Sorry that's not enough money. Money refunded.")
                return
            print("Here is your espresso. Enjoy!")
        elif user_input == "lat" and check_resources():
            self.water -= 200
            self.milk -= 150
            self.coffee_beans -= 24
            self.process_coins(self.user_input)
            if self.money < self.cost:
                print("Sorry that's not enough money. Money refunded.")
                return
            print("Here is your latte. Enjoy!")
        elif user_input == "cap" and check_resources():
            self.water -= 250
            self.milk -= 100
            self.coffee_beans -= 24
            self.process_coins(self.user_input)
            if self.money < self.cost:
                print("Sorry that's not enough money. Money refunded.")
                return
            print("Here is your cappuccino. Enjoy!")

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

        if self.money >= self.cost:
            self.calculate_change()

        return True

    def calculate_change(self):
        change = round(self.money - self.cost)
        print(f"Here is ${change} in change.")
        self.money = 0

    def machine_off(self, user_input):
        if user_input == "off":
            print("Machine is off")
            self.machine_on = False

    def report(self, user_input):
        if user_input == "report":
            print(f"Water: {self.water}ml")
            print(f"Milk: {self.milk}ml")
            print(f"Coffee Beans: {self.coffee_beans}g")


coffee_machine = CoffeeMachine()
while coffee_machine.machine_on:
    check_resources()
    coffee_machine.report(coffee_machine.user_input)
    if coffee_machine.machine_on is False:
        break
    coffee_machine.machine_off(coffee_machine.user_input)
    coffee_machine.make_coffee(coffee_machine.user_input)
    coffee_machine.user_input = input("What would you like? (esp/lat/cap): ").lower()
