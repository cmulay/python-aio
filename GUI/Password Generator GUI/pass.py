from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_generator():
    pass_list = []
    for char in range(randint(8, 10)):
        pass_list.append(choice(alphabets))

    for char in range(randint(2, 4)):
        pass_list += choice(symbols)

    for char in range(randint(2, 4)):
        pass_list += choice(digits)

    shuffle(pass_list)

    password = ""
    for char in pass_list:
        password += char

    input_password.insert(0, password)
    print(f"Your password is: {password}")


def store_pass():
    get_website = input_website.get()
    get_email = input_email.get()
    get_pass = input_password.get()

    with open('password.txt', 'w') as data:
        if len(get_website) == 0 or len(get_email) <= 3 or len(get_pass) == 0:
            option = messagebox.showinfo(title="Uhh-ohh", message="Oops missed a field")
        else:
            option = messagebox.askokcancel(title="Confirm",
                                            message=f"Website: {get_website}\nEmail: {get_email}\nPassword: {get_pass}\nSave?")
            if option:
                data.write(f"{get_website} || {get_email} || {get_pass}\n")
                option = messagebox.showinfo(title="Success", message="Successfully Saved")
                input_password.delete(0, END)
                input_website.delete(0, END)
                data.close()


window = Tk()
window.title("Password Generator")
window.config(bg='white', padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)

website_label = Label(text="Website:")
website_label.config(bg="white")
website_label.grid(row=1, column=0)

input_website = Entry(width=50)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

email_label = Label(text="Email/Username:")
email_label.config(bg="white")
email_label.grid(row=2, column=0)

input_email = Entry(width=50)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "yourname@gmail.com")
password_label = Label(text="Password:")
password_label.config(bg="white")
password_label.grid(row=3, column=0)

input_password = Entry(width=25)
input_password.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=pass_generator)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=store_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
