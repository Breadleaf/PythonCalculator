import tkinter
from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(0, 0)
root.configure(bg='black')
root.iconphoto(False, tkinter.PhotoImage(file='Icon.png'))

numberField = Entry(root, width=48, bg='black', fg='white')
numberField.grid(row=0, column=0, columnspan=3)

operator = ''
numOne = 0


def btnClick(num):
    tempNumField = numberField.get()
    numberField.delete(0, END)
    numberField.insert(0, str(tempNumField) + str(num))


def clear():
    numberField.delete(0, END)


def add():
    global numOne
    global operator
    numOne = float(numberField.get())
    operator = 'add'
    numberField.delete(0, END)


def sub():
    global numOne
    global operator
    numOne = float(numberField.get())
    operator = 'sub'
    numberField.delete(0, END)


def mult():
    global numOne
    global operator
    numOne = float(numberField.get())
    operator = 'mult'
    numberField.delete(0, END)


def div():
    global numOne
    global operator
    numOne = float(numberField.get())
    operator = 'div'
    numberField.delete(0, END)


def equals():
    global operator
    numTwo = float(numberField.get())
    numberField.delete(0, END)
    if operator == 'add':
        numberField.insert(0, str(numOne + numTwo))
    elif operator == 'sub':
        numberField.insert(0, str(numOne - numTwo))
    elif operator == 'mult':
        numberField.insert(0, str(numOne * numTwo))
    elif operator == 'div':
        if numOne == 0:
            numberField.insert(0, 'Divide by zero error, to continue press clear')
        elif numTwo == 0:
            numberField.insert(0, 'n/0 is undefined, to continue press clear')
        else:
            numberField.insert(0, str(numOne / numTwo))
    else:
        numberField.insert(0, 'Please enter a valid operator, to continue press clear')
    operator = ''


btnOne = Button(root, text="1", padx=43, pady=20, command=lambda: btnClick(1), bg='black', fg='white')
btnOne.grid(row=3, column=0)

btnTwo = Button(root, text="2", padx=43, pady=20, command=lambda: btnClick(2), bg='black', fg='white')
btnTwo.grid(row=3, column=1)

btnThree = Button(root, text="3", padx=40, pady=20, command=lambda: btnClick(3), bg='black', fg='white')
btnThree.grid(row=3, column=2)

btnFour = Button(root, text="4", padx=43, pady=20, command=lambda: btnClick(4), bg='black', fg='white')
btnFour.grid(row=2, column=0)

btnFive = Button(root, text="5", padx=43, pady=20, command=lambda: btnClick(5), bg='black', fg='white')
btnFive.grid(row=2, column=1)

btnSix = Button(root, text="6", padx=40, pady=20, command=lambda: btnClick(6), bg='black', fg='white')
btnSix.grid(row=2, column=2)

btnSeven = Button(root, text="7", padx=43, pady=20, command=lambda: btnClick(7), bg='black', fg='white')
btnSeven.grid(row=1, column=0)

btnEight = Button(root, text="8", padx=43, pady=20, command=lambda: btnClick(8), bg='black', fg='white')
btnEight.grid(row=1, column=1)

btnNine = Button(root, text="9", padx=40, pady=20, command=lambda: btnClick(9), bg='black', fg='white')
btnNine.grid(row=1, column=2)

btnZero = Button(root, text="0", padx=43, pady=20, command=lambda: btnClick(0), bg='black', fg='white')
btnZero.grid(row=4, column=0)

btnDecimal = Button(root, text='.', padx=42, pady=20, command=lambda: btnClick('.'), bg='black', fg='white')
btnDecimal.grid(row=6, column=2)

btnAdd = Button(root, text="+", padx=41, pady=20, command=add, bg='black', fg='white')
btnAdd.grid(row=4, column=1)

btnSub = Button(root, text="-", padx=41, pady=20, command=sub, bg='black', fg='white')
btnSub.grid(row=4, column=2)

btnMult = Button(root, text="x", padx=43, pady=20, command=mult, bg='black', fg='white')
btnMult.grid(row=5, column=1)

btnDiv = Button(root, text="/", padx=41, pady=20, command=div, bg='black', fg='white')
btnDiv.grid(row=5, column=2)

btnClr = Button(root, text="Clear", padx=32, pady=20, command=clear, bg='black', fg='white')
btnClr.grid(row=5, column=0)

btnEqu = Button(root, text="Equals", padx=80, pady=20, command=equals, bg='black', fg='white')
btnEqu.grid(row=6, column=0, columnspan=2)

root.mainloop()
