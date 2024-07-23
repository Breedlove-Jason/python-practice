import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


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

    pyperclip.copy(password)

    return password

    # ---------------------------- Save Password ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )

    try:
        with open("data.json", "r") as file:
            # json.dump(new_data, file, indent=4)
            try:
                # reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(new_data)
                # data = json.load(file)
                # print(data)
            except json.decoder.JSONDecodeError:
                data = {}
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    except FileNotFoundError:
        data = {}

    # UI cleanup moved outside the try-except block.
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jason@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", width=15, command=gen_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
