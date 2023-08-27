from tkinter import *
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*']

def generate():
    password = ""

    password_field.delete(0, END)

    password_field.config(show='*')

    show_password_btn.config(text="Show Password")

    for i in range(0, length.get()):
        index = randint(0, len(letters) - 1)
        password += letters[index]

    password_field.insert(0, password)

def generateenter(event):
    generate()

def showpassword():
    if password_field.cget('show') == '*':
        password_field.config(show="")
        show_password_btn.config(text="Hide Password")
    else:
        password_field.config(show="*")
        show_password_btn.config(text="Show Password")

root = Tk()

root.geometry("350x200")
root.minsize(width=100, height=100)

root.title("Password Generator")
root.wm_iconbitmap("password.ico")

heading = Label(root, text="Password Generator", font="Helvetica 15 bold italic")
heading.pack(pady=10)

f1 = Frame(root)
f1.pack(pady=10)

prompt = Label(f1, text="Enter password length")
prompt.pack(side=LEFT, padx=10)

length = IntVar()

field = Entry(f1, textvariable=length)
field.pack(side=LEFT)
field.bind('<Return>', generateenter)

generate_btn = Button(root, fg="black", text="Generate", command=generate)
generate_btn.pack(pady=10)

f2 = Frame(root)
f2.pack(pady=10)

password_field = Entry(f2, show='*')
password_field.pack(side=LEFT, padx=10)

show_password_btn = Button(f2, fg='black', text="Show Password", command=showpassword)
show_password_btn.pack(side=LEFT, padx=10)


root.mainloop()
