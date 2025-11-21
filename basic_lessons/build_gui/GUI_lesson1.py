import tkinter as tk

def change_text():
    label.config(text="Hello, student!")

# Create the main window
window = tk.Tk()
window.title("Lesson 1: Tkinter")
window.geometry("300x200")

# Initial label
label = tk.Label(window, text="Press the button", font=("Segoe UI", 12))
label.pack(pady=20)

# Button to change the text
button = tk.Button(window, text="Click me!", command=change_text)
button.pack(pady=10)

window.mainloop()
