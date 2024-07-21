import random
from tkinter import *
from tkinter import messagebox


def gen_password():
    # Define character sets
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!#$%&()*+"
    numbers = "0123456789"

    # Determine the number of each type of character
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    # Generate the password components
    password_list = (
            [random.choice(letters) for _ in range(num_letters)]
            + [random.choice(symbols) for _ in range(num_symbols)]
            + [random.choice(numbers) for _ in range(num_numbers)]
    )

    # Shuffle the components and form the password
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)

    return password

    # ---------------------------- Save Password ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return
    messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?",
    )

    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # Increased padding for the window for better spacing

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)  # Centered canvas

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")  # Align to the right for consistency

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
# website = website_entry.get()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")  # Align to the right for consistency

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jason@email.com")
# email = email_entry.get()

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)  # Align to the right for consistency

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)  # Added vertical padding

generate_button = Button(text="Generate Password", width=15, command=gen_password)
generate_button.grid(row=3, column=2)  # Adjusted width and added vertical padding

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(
    row=4, column=1, columnspan=2
)  # Increased vertical padding for separation

window.mainloop()
