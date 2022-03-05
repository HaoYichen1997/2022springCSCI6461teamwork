"""

Creater:Zack
Date:02/27/2022

"""
from tkinter import *
from tkinter import messagebox

def pro1():
    # define program1 background
    Program1W = Toplevel()
    Program1W.title('Program1')
    Program1W.geometry("650x600")

    InitialLabel = Label(Program1W, text="Initial Number(20)")
    TestNumberLabel = Label(Program1W, text="Input Test Number")
    ResultLabel = Label(Program1W, text="Closest Number(Result)")
    Space = Label(Program1W, text=" ")
    # define intial number textbox
    InitialNumber = Entry(Program1W, width=40, borderwidth=4)
    TestNumber = Entry(Program1W, width=40, borderwidth=4)
    ResultNumber = Entry(Program1W, width=40, borderwidth=4)


    global step
    step = 0
    global Consolekey
    Consolekey = ["0"] * 30
    #define Button function
    def Program1(event):
        global step
        global Consolekey
        if InitialNumber.get().isdigit():
            if step < 20:
                Consolekey[0] = InitialNumber.get()
                print(InitialNumber.get())
                print(Consolekey)
                InitialNumber.delete(0, END)
                # instruct in and store to memory
                # halt
            else:
                InitialNumber.delete(0, END)
                InitialNumber.insert(0, "number has been enough, start calculateing!")
                # run
                # halt的灯 更新成为run
        else:
            messagebox.showerror("Error", "Your input is not a number")
            step -= 1
        step += 1



    Program1W.bind('<Return>', Program1)
    # define Button
    CalBtn = Button(Program1W, text="Calculate!", padx=1, pady=1, command=Program1)


    #define location of elements
    InitialLabel.grid(row=0, column=0)
    InitialNumber.grid(row=1, column=0)

    TestNumberLabel.grid(row=6, column=0)
    TestNumber.grid(row=7, column=0)
    CalBtn.grid(row=7, column=1)
    Space.grid(row=8, column=0)
    Space.grid(row=9, column=0)
    ResultLabel.grid(row=10, column=0)
    ResultNumber.grid(row=11, column=0)




