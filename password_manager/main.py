from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_url.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n Email: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as datafile:
                datafile.write(f"{website} | {email} | {password}\n")
                password_entry.delete(0, END)
                website_url.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady= 50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1, row=0)

#Labels
website_text = Label(text = "Website:")
website_text.grid(column=0,row=1)
email_text = Label(text="Email/Username:")
email_text.grid(column=0,row=2)
password_text = Label(text="Password:")
password_text.grid(column=0,row=3)

#Entry
website_url = Entry(width=35)
website_url.grid(column=1,row=1,columnspan=2,sticky="EW")
website_url.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "abcd@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


#Buttons
generate_password = Button(text="Generate Password", command = password_generator)
generate_password.grid(column=2,row=3,sticky="EW")
add_button = Button(text="Add", width= 36, command=save_details)
add_button.grid(column=1,row=4, columnspan=2,sticky="EW")



window.mainloop()