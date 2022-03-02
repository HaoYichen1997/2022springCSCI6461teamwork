"""

Creater:Zack
Date:02/27/2022

"""
from tkinter import *

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
    Initial00 = Entry(Program1W, width=20, borderwidth=4)
    Initial01 = Entry(Program1W, width=20, borderwidth=4)
    Initial02 = Entry(Program1W, width=20, borderwidth=4)
    Initial03 = Entry(Program1W, width=20, borderwidth=4)
    Initial04 = Entry(Program1W, width=20, borderwidth=4)
    Initial05 = Entry(Program1W, width=20, borderwidth=4)
    Initial06 = Entry(Program1W, width=20, borderwidth=4)
    Initial07 = Entry(Program1W, width=20, borderwidth=4)
    Initial08 = Entry(Program1W, width=20, borderwidth=4)
    Initial09 = Entry(Program1W, width=20, borderwidth=4)
    Initial10 = Entry(Program1W, width=20, borderwidth=4)
    Initial11 = Entry(Program1W, width=20, borderwidth=4)
    Initial12 = Entry(Program1W, width=20, borderwidth=4)
    Initial13 = Entry(Program1W, width=20, borderwidth=4)
    Initial14 = Entry(Program1W, width=20, borderwidth=4)
    Initial15 = Entry(Program1W, width=20, borderwidth=4)
    Initial16 = Entry(Program1W, width=20, borderwidth=4)
    Initial17 = Entry(Program1W, width=20, borderwidth=4)
    Initial18 = Entry(Program1W, width=20, borderwidth=4)
    Initial19 = Entry(Program1W, width=20, borderwidth=4)

    TestNumber = Entry(Program1W, width=20, borderwidth=4)
    ResultNumber = Entry(Program1W, width=20, borderwidth=4)



    # for i in range(20):
    #     if i < 10 :
    #         exec("Initial" + '0' + str(i) + ".insert(0,"+ str(i) + ')')
    #     else:
    #         exec("Initial" + str(i) + ".insert(0,"+ str(i) + ')')

    #define Button function
    def Program1():
        NInitial00 = Initial00.get()
        NInitial01 = Initial01.get()
        NInitial02 = Initial02.get()
        NInitial03 = Initial03.get()
        NInitial04 = Initial04.get()
        NInitial05 = Initial05.get()
        NInitial06 = Initial06.get()
        NInitial07 = Initial07.get()
        NInitial08 = Initial08.get()
        NInitial09 = Initial09.get()
        NInitial10 = Initial10.get()
        NInitial11 = Initial11.get()
        NInitial12 = Initial12.get()
        NInitial13 = Initial13.get()
        NInitial14 = Initial14.get()
        NInitial15 = Initial15.get()
        NInitial16 = Initial16.get()
        NInitial17 = Initial17.get()
        NInitial18 = Initial18.get()
        NInitial19 = Initial19.get()
        Program1Cache = []
        # for i in range(20):
        #     if i < 10:
        #         exec("Program1Cache" + '[' + str(i) + ']' + '=' + "NInitial" + '0' + str(i))
        #     else:
        #         exec("Program1Cache" + '[' + str(i) + ']' + '=' + "NInitial" + str(i))
        print(Program1Cache)

    # define Button
    CalBtn = Button(Program1W, text="Calculate!", padx=1, pady=1, command=Program1)


    #define location of elements
    InitialLabel.grid(row=0, column=0)
    idxnumber = 0
    for i in range(1, 6):
        for j in range(4):
            if idxnumber < 10:
                exec("Initial" + '0' + str(idxnumber) + '.' + "grid(row=" + str(i) + ",column=" + str(j) + ')')
                idxnumber += 1
            else :
                exec("Initial" + str(idxnumber) + '.' + "grid(row=" + str(i) + ",column=" + str(j) + ')')
                idxnumber += 1
    TestNumberLabel.grid(row=6, column=0)
    TestNumber.grid(row=7, column=0)
    CalBtn.grid(row=7, column=1)
    Space.grid(row=8, column=0)
    Space.grid(row=9, column=0)
    ResultLabel.grid(row=10, column=0)
    ResultNumber.grid(row=11, column=0)


