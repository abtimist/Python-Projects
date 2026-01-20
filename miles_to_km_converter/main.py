from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0,row=1)

miles_text = Label(text="Miles")
miles_text.grid(column=3,row=0)

km_text = Label(text="Km")
km_text.grid(column=3,row=1)

km_value = Label(text="0")
km_value.grid(column=1,row=1)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


def button_clicked():
    miles = int(miles_input.get())
    kilometer = round(miles*1.609,2)
    km_value.config(text=f"{kilometer}")

button = Button(text = "Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()