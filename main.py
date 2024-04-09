import tkinter as tk
import fibonacci
import prime
from tkinter import messagebox  # Import messagebox for displaying results

# Create the main window
root = tk.Tk()


def clear_gui():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()


def prime_checker_gui():
    # Create a label widget
    label = tk.Label(root, text="Enter a number to check if it's prime:")

    # Create a text entry widget
    num_entry = tk.Entry(root)

    # Create a button to check if the number is prime
    check_button = tk.Button(root, text="Check Prime", command=lambda: prime_checker(num_entry))

    # Pack the widgets into the window
    label.pack()
    num_entry.pack()
    check_button.pack()


def prime_checker(num):
    number = num.get()
    answer = prime.prime_checker(number)
    if answer is False:
        clear_gui()
        label_wrong = tk.Label(root, text="Please enter a positive integer.")
        label_wrong.pack()
        prime_checker_gui()
    else:
        clear_gui()
        label_answer = tk.Label(root, text=answer)
        label_okay = tk.Button(root, text="Okay", command=run_home)
        label_answer.pack()
        label_okay.pack()


def fib_gui():
    # Create a label widget
    label = tk.Label(root, text="How many terms of the Fibonacci sequence would you like to list?")

    # Create a text entry widget
    num_entry = tk.Entry(root)

    # Create a button to check if the number is prime
    check_button = tk.Button(root, text="List", command=lambda: fib(num_entry))

    # Pack the widgets into the window
    label.pack()
    num_entry.pack()
    check_button.pack()


def fib(num):
    number = num.get()
    answer = fibonacci.fibonacci_sequence(number)
    if answer is False:
        clear_gui()
        label_wrong = tk.Label(root, text="Please enter a positive integer.")
        label_wrong.pack()
        fib_gui()
    else:
        clear_gui()
        label_answer = tk.Label(root, text=answer)
        label_okay = tk.Button(root, text="Okay", command=run_home)
        label_answer.pack()
        label_okay.pack()


# Create button commands
def run_prime():
    clear_gui()
    prime_checker_gui()


def run_fibonacci():
    clear_gui()
    fib_gui()


def home():
    # Create a label widget
    label = tk.Label(root, text="Please select an app")

    # Create button widgets
    button1 = tk.Button(root, text="Prime Checker", command=run_prime)
    button2 = tk.Button(root, text="Fibonacci Sequence", command=run_fibonacci)
    button3 = tk.Button(root, text="Quit", command=lambda: root.quit())

    # Pack the widgets into the window
    label.pack()
    button1.pack()
    button2.pack()
    button3.pack()


def run_home():
    clear_gui()
    home()


run_home()

# Start the event loop
root.mainloop()
