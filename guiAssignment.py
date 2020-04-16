from tkinter import *


def button_execute():
    value_gram.set(float(value_kilogram.get())*1000)
    value_pound.set(float(value_kilogram.get())*2.20462)
    value_ounce.set(float(value_kilogram.get())*35.274)

window = Tk()

value_kilogram = StringVar()
value_gram = StringVar()
value_pound = StringVar()
value_ounce = StringVar()

t1 = Label(window,text="Enter Kg")
t1.grid(row=0,column=0)

e1 = Entry(window,width=5, textvariable = value_kilogram)
e1.grid(row=0,column=1)

b1 = Button(window,text="Execute",command=button_execute)
b1.grid(row=0,column=2)

gram = Entry(window,textvariable=value_gram)
pound = Entry(window,textvariable=value_pound)
ounce = Entry(window,textvariable=value_ounce)

gram.grid(row=1,column=0)
pound.grid(row=1,column=1)
ounce.grid(row=1,column=2)

window.mainloop()