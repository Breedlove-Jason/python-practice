import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# Generates a strong password combining letters, symbols, and numbers
def gen_password():
    # Define character sets
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!#$%&()*+"
    numbers = "0123456789"

    # Generate the password components
    password_list = (
        [random.choice(letters) for _ in range(randint(8, 10))]
        + [random.choice(symbols) for _ in range(randint(2, 4))]
        + [random.choice(numbers) for _ in range(randint(2, 4))]
    )

    # Shuffle the components and form the password
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)

    return password


# Saves the password for the given website and email
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    # Check if website or password fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    # Attempt to read existing data; handle file not found or empty file
    try:
        with open("data.json", "r") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        data = {}

    # Update data with new entry and write back to file
    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    # Clear the website and password fields after saving
    website_entry.delete(0, END)
    # email_entry.delete(0, END)  # This line is commented out; decide if it should clear the email field
    password_entry.delete(0, END)


# UI setup for the password manager application
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo display
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website entry setup
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search_button = Button(text="Search", width=12)
search_button.grid(row=1, column=2)

# Email/Username entry setup
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jason@email.com")

# Password entry setup
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Generate password button
generate_button = Button(text="Generate Password", width=15, command=gen_password)
generate_button.grid(row=3, column=2)

# Add button to save the password
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Start the GUI event loop
window.mainloop()
