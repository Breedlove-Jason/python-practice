from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # Increased padding for the window for better spacing

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, padx=20, pady=20)  # Centered canvas

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")  # Align to the right for consistency

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=2)  # Added vertical padding

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")  # Align to the right for consistency

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)  # Added vertical padding

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)  # Align to the right for consistency

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=2)  # Added vertical padding

generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2)  # Adjusted width and added vertical padding

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=10)  # Increased vertical padding for separation

window.mainloop()