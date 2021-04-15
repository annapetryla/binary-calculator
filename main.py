from tkinter import *
import sys
import math

admin = Tk()
admin.title("Kalkulator binarny")
admin.geometry('480x220')


def dec_to_bin(x):
    return int(bin(x)[2:])


def binary_addition(first_dig, second_dig):
    while first_dig != 0:
        c = second_dig & first_dig
        second_dig = second_dig ^ first_dig
        first_dig = c << 1
    return second_dig


def binary_substraction(first_dig, second_dig):
    while second_dig != 0:
        what_is_borrowed = (~first_dig) & second_dig
        first_dig = first_dig ^ second_dig
        second_dig = what_is_borrowed << 1
    return first_dig


def binary_multiplication(first_dig, second_dig):
    result = 0
    while second_dig != 0:
        if second_dig & 1:
            result = result | first_dig
        first_dig = first_dig << 1
        second_dig = second_dig >> 1
    return result


def binary_division(first_dig, second_dig):
    result = 0
    while first_dig >= second_dig:
        temp_val = second_dig
        counter = 1
        while temp_val <= first_dig:
            temp_val = temp_val << 1
            counter = counter << 1
        result = result | counter >> 1
        temp_val = temp_val >> 1
        first_dig = binary_substraction(first_dig, second_dig)
    return result


aLabel = Label(admin, text="War I ::", font='Cambria 8')
aLabel.place(x=20, y=20, width=60, height=40)

aEntry = Entry(admin, bd=1)
aEntry.place(x=70, y=20, width=90, height=40)

bLabel = Label(admin, text="War II ::", font='Cambria 8')
bLabel.place(x=160, y=20, width=60, height=40)

bEntry = Entry(admin, bd=1)
bEntry.place(x=210, y=20, width=90, height=40)

cLabel = Label(admin, text="Znak ::\n+ - * /", font='Cambria 8')
cLabel.place(x=300, y=20, width=60, height=40)

cEntry = Entry(admin, bd=1)
cEntry.place(x=350, y=20, width=90, height=40)

resultLabel = Label(admin, text="Wynik :: ", font='Cambria 8')
resultLabel.place(x=60, y=140, width=60, height=40)

resultEntry = Entry(admin, bd=1)
resultEntry.place(x=110, y=140, width=110, height=40)

binresultLabel = Label(admin, text="Bin :: ", font='Cambria 8')
binresultLabel.place(x=200, y=140, width=60, height=40)

binresultEntry = Entry(admin, bd=1)
binresultEntry.place(x=250, y=140, width=110, height=40)



def account():


    resultEntry.delete(0, END)
    a = int(aEntry.get())
    b = int(bEntry.get())
    if cEntry.get() == '+':
        result = binary_addition(int(aEntry.get()), int(bEntry.get()))
        resultEntry.insert(0, result)
        binresultEntry.insert(0, dec_to_bin(result))
    if cEntry.get() == '-':
        result = binary_substraction(int(aEntry.get()), int(bEntry.get()))
        resultEntry.insert(0, result)
        binresultEntry.insert(0,dec_to_bin(result))
    if cEntry.get() == '*':
        result = binary_multiplication(int(aEntry.get()), int(bEntry.get()))
        resultEntry.insert(0, result)
        binresultEntry.insert(0, dec_to_bin(result))
    if cEntry.get() == '/':
        if int(bEntry.get()) == 0:
            resultEntry.insert(0, "Niedozwolone")
            return
        result = binary_division(int(aEntry.get()), int(bEntry.get()))
        resultEntry.insert(0, result)
        binresultEntry.insert(0, dec_to_bin(result))
    aEntry.delete(0, END)
    aEntry.insert(0, dec_to_bin(a))

    bEntry.delete(0, END)
    bEntry.insert(0, dec_to_bin(b))


button = Button(text="Oblicz", command=account, font='Cambria 8')
button.place(x=180, y=80, width=140, height=40)



admin.mainloop()