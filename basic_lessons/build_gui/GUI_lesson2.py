import tkinter as tk
from tkinter import messagebox
import random

def change_text():
    """Change the text of the label when the button is clicked."""
    label.config(text="Hello, student!")

def update_random_data():
    """Update the label with a random number every 3 seconds."""
    random_value = random.randint(1, 100)  # Generate a random number between 1 and 100
    random_label.config(text=f"Random Value: {random_value}")  # Update the label with the random number
    window.after(1000, update_random_data)  # Call this function again after 1000ms (1 seconds)

def reset_greeting():
    """Ask for confirmation before resetting the greeting label."""
    response = messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset the greeting?")
    if response:  # If the user clicks 'Yes'
        label.config(text="Press the button")  # Reset the greeting label to the initial text

# Create the main window
window = tk.Tk()
window.title("Lesson 2: Tkinter")
window.geometry("300x250")

# Initial greeting label
label = tk.Label(window, text="Press the button", font=("Segoe UI", 12))
label.pack(pady=20)

# Button to change the greeting text
button = tk.Button(window, text="Click me!", command=change_text)
button.pack(pady=10)

# Reset button to reset the greeting label
reset_button = tk.Button(window, text="Reset", command=reset_greeting)
reset_button.pack(pady=10)

# Label to display random value
random_label = tk.Label(window, text="Random Value: 0", font=("Segoe UI", 12))
random_label.pack(pady=20)

# Start the random data update loop
update_random_data()

# Start the main event loop
window.mainloop()
