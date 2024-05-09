import random
import string
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low(exclude_chars):
    entry.delete(0, END)

    # Get the length of password
    length = var1.get()

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?~"

    password = ""

    # if strength selected is low
    if var.get() == 1:
        char_set = lower
    # if strength selected is medium
    elif var.get() == 0:
        char_set = lower + upper
    # if strength selected is strong
    elif var.get() == 3:
        char_set = lower + upper + digits + special_chars

    for i in range(length):
        char = random.choice(char_set)
        while char in exclude_chars:
            char = random.choice(char_set)
        password += char
    return password




def generate():
    exclude_chars = exclude_entry.get().strip()
    password1 = low(exclude_chars)
    entry.insert(10, password1)



def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


root = Tk()
var = IntVar()
var1 = IntVar()


root.title("Random Password Generator")

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)


c_label = Label(root, text="Length")
c_label.grid(row=1)

exclude_label = Label(root, text="Exclude Characters")
exclude_label.grid(row=2)


exclude_entry = Entry(root)
exclude_entry.grid(row=2, column=1)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)


radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)


combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()
