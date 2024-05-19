# Coffee Machine

## Description

The Coffee Machine project simulates a simple coffee machine that can make espresso, latte, and cappuccino. The machine checks for sufficient resources, processes coins for payment, calculates change, and updates the resources after making a coffee. It also includes functionality to turn off the machine and report the current resources.

## How to Use

1. Run the `main.py` script.
2. The machine will prompt you to select a type of coffee (espresso, latte, or cappuccino) or to turn off the machine.
3. If a coffee type is selected, the machine will check if there are enough resources to make the coffee.
4. If resources are sufficient, the machine will prompt you to insert coins.
5. The machine will then calculate if enough money has been inserted and dispense the coffee if the payment is sufficient.
6. The machine will provide change if necessary and update the resource levels.

## Files

- `main.py`: The main script for the coffee machine simulation.
- `menu.py`: Contains the resources used by the coffee machine.

## Running the Project

To run the project, navigate to the `coffee-machine` directory and execute the `main.py` script using Python:

```bash
cd coffee-machine
python main.py
```
coffee-machine/
├── main.py
├── menu.py
└── README.md

```python
What would you like? (esp/lat/cap): lat
Water: 200ml
Milk: 150ml
Coffee Beans: 24g
Money: $0
Please insert coins
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your lat. Enjoy!
```
