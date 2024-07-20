from tkinter import *
import math

# Define color constants for UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# Time constants in minutes
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # Track number of repetitions
timer = None  # Reference for the timer


def reset_timer():
    """Resets the timer to its initial state."""
    window.after_cancel(timer)  # Stops the current countdown
    canvas.itemconfig(timer_text, text="00:00")  # Resets timer display
    title_label.config(text="Timer")  # Resets the title label
    check_marks.config(text="")  # Clears check marks
    global reps
    reps = 0  # Resets repetition counter


def start_timer():
    """Starts the timer for work or break based on the session count."""
    global reps
    reps += 1

    # Calculate seconds for each session type
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine session type and start countdown
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    """Performs the countdown and updates the UI accordingly."""
    count_min = math.floor(count / 60)  # Minutes remaining
    count_sec = count % 60  # Seconds remaining
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Format seconds with leading zero

    # Update timer display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Schedule next second
    else:
        start_timer()  # Restart timer for next session
        marks = ""  # String to hold check marks
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)  # Update check marks display


# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas for tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Load tomato image
canvas.create_image(100, 112, image=tomato_img)  # Display tomato image
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)  # Timer display
canvas.grid(column=1, row=1)

# Start and reset buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label for check marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()  # Start the GUI event loop
