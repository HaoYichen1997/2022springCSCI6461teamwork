from tkinter import *
import Cache

#Cache windows panel design


def open():
    #define cache basic background
    cacheW = Toplevel()
    cacheW.title('Cache Display')
    cacheW.geometry("1400x600")

    #define Label
    IdxLabel = Label(cacheW, text="Index")
    ValLabel = Label(cacheW, text="Valid")
    BlkNLabel = Label(cacheW, text="Block#")
    Ewordslabel = Label(cacheW, text="8 Words")

    #define Idx textbox number 0-16
    for i, j in zip(range(1, 17), range(16)):
        exec("Idx" + str(j) + '=' + "Entry(cacheW, width=4, borderwidth=4)")
    # define Block Number textbox number 0-16
    for i, j in zip(range(1, 17), range(16)):
        exec("Blk_Num" + str(j) + '=' + "Entry(cacheW, width=8, borderwidth=4)")
    # define Valid textbox number 0-16
    for i, j in zip(range(1, 17), range(16)):
        exec("Valid" + str(j) + '=' + "Entry(cacheW, width=2, borderwidth=4)")
    # define 8 words textbox number
    # defination rule :  Ewords + row number + column number , such as Ewords061 == row No.7 & column No.2 because of number starting from 0;
    for i in range(16):
        for j in range(8):
            if i < 10:
                exec("Ewords" + '0' + str(i) +str(j) + '=' + "Entry(cacheW, width=20, borderwidth=4)")
            else :
                exec("Ewords" + str(i) + str(j) + '=' + "Entry(cacheW, width=20, borderwidth=4)")


    #refresh cache windows
    def refresh():
        cacheW.destroy()
        open()
    def clearCache():
        Cache.cache=["0"]*16
        for elements in range(16):
            Cache.cache[elements] = ["0"] * 10
        for i in range(16):
            exec()


    #define Button
    RefreshBtn =Button(cacheW,text="Refresh",padx=10, pady=15, command=refresh)
    ClearBtn = Button(cacheW,text="Clear",padx=10, pady=15, command=clearCache)


    #grid
    IdxLabel.grid(row=0, column=0)
    ValLabel.grid(row=0, column=1)
    BlkNLabel.grid(row=0, column=2)
    Ewordslabel.grid(row=0, column=3)
    # Idx location at row 1-17
    for i, j in zip(range(1, 17), range(16)):
        exec("Idx" + str(j) + '.' + "grid(row=" + str(i) + ",column=0" + ')')
    # valid location at row 1-17
    for i, j in zip(range(1, 17), range(16)):
        exec("Valid" + str(j) + '.' + "grid(row=" + str(i) + ",column=1" + ')')
    # Block location at row 1-17
    for i, j in zip(range(1, 17), range(16)):
        exec("Blk_Num" + str(j) + '.' + "grid(row=" + str(i) + ",column=2" + ')')
    # 8 words location at row 1-17
    for i in range(1, 17):
        for j in range(3, 11):
            if i-1 < 10:
                exec("Ewords" + '0' + str(i-1) + str(j-3) + '.' + "grid(row=" + str(i) + ",column=" + str(j) + ')')
            else:
                exec("Ewords" + str(i-1) + str(j-3) + '.' + "grid(row=" + str(i) + ",column=" + str(j) + ')')

    RefreshBtn.grid(row=20, column=10)





