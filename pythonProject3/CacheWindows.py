from tkinter import *
import Cache
import Program1

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
    # Idx0 = Entry(cacheW, width=4, borderwidth=4)
    # Idx1 = Entry(cacheW, width=4, borderwidth=4)
    # Idx2 = Entry(cacheW, width=4, borderwidth=4)
    # Idx3 = Entry(cacheW, width=4, borderwidth=4)
    # Idx4 = Entry(cacheW, width=4, borderwidth=4)
    # Idx5 = Entry(cacheW, width=4, borderwidth=4)
    # Idx6 = Entry(cacheW, width=4, borderwidth=4)
    # Idx7 = Entry(cacheW, width=4, borderwidth=4)
    # Idx8 = Entry(cacheW, width=4, borderwidth=4)
    # Idx9 = Entry(cacheW, width=4, borderwidth=4)
    # Idx10 = Entry(cacheW, width=4, borderwidth=4)
    # Idx11 = Entry(cacheW, width=4, borderwidth=4)
    # Idx12 = Entry(cacheW, width=4, borderwidth=4)
    # Idx13 = Entry(cacheW, width=4, borderwidth=4)
    # Idx14 = Entry(cacheW, width=4, borderwidth=4)
    # Idx15 = Entry(cacheW, width=4, borderwidth=4)
    Idx0 = Label(cacheW, text="0")
    Idx1 = Label(cacheW, text="1")
    Idx2 = Label(cacheW, text="2")
    Idx3 = Label(cacheW, text="3")
    Idx4 = Label(cacheW, text="4")
    Idx5 = Label(cacheW, text="5")
    Idx6 = Label(cacheW, text="6")
    Idx7 = Label(cacheW, text="7")
    Idx8 = Label(cacheW, text="8")
    Idx9 = Label(cacheW, text="9")
    Idx10 = Label(cacheW, text="10")
    Idx11 = Label(cacheW, text="11")
    Idx12 = Label(cacheW, text="12")
    Idx13 = Label(cacheW, text="13")
    Idx14 = Label(cacheW, text="14")
    Idx15 = Label(cacheW, text="15")
    # for i, j in zip(range(1, 17), range(16)):
    #     exec("Idx" + str(j) + '=' + "Entry(cacheW, width=4, borderwidth=4)")
    #     print("Idx"+ str(j))
    # define Block Number textbox number 0-16
    Blk_Num0 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num1 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num2 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num3 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num4 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num5 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num6 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num7 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num8 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num9 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num10 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num11 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num12 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num13 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num14 = Entry(cacheW, width=4, borderwidth=4)
    Blk_Num15 = Entry(cacheW, width=4, borderwidth=4)

    # for i, j in zip(range(1, 17), range(16)):
    #     exec("Blk_Num" + str(j) + '=' + "Entry(cacheW, width=8, borderwidth=4)")
    # define Valid textbox number 0-16
    Valid0 = Entry(cacheW, width=4, borderwidth=4)
    Valid1 = Entry(cacheW, width=4, borderwidth=4)
    Valid2 = Entry(cacheW, width=4, borderwidth=4)
    Valid3 = Entry(cacheW, width=4, borderwidth=4)
    Valid4 = Entry(cacheW, width=4, borderwidth=4)
    Valid5 = Entry(cacheW, width=4, borderwidth=4)
    Valid6 = Entry(cacheW, width=4, borderwidth=4)
    Valid7 = Entry(cacheW, width=4, borderwidth=4)
    Valid8 = Entry(cacheW, width=4, borderwidth=4)
    Valid9 = Entry(cacheW, width=4, borderwidth=4)
    Valid10 = Entry(cacheW, width=4, borderwidth=4)
    Valid11 = Entry(cacheW, width=4, borderwidth=4)
    Valid12 = Entry(cacheW, width=4, borderwidth=4)
    Valid13 = Entry(cacheW, width=4, borderwidth=4)
    Valid14 = Entry(cacheW, width=4, borderwidth=4)
    Valid15 = Entry(cacheW, width=4, borderwidth=4)
    # for i, j in zip(range(1, 17), range(16)):
    #     exec("Valid" + str(j) + '=' + "Entry(cacheW, width=2, borderwidth=4)")
    # define 8 words textbox number
    # defination rule :  Ewords + row number + column number , such as Ewords061 == row No.7 & column No.2 because of number starting from 0;
    Ewords000 = Entry(cacheW, width=20, borderwidth=4)
    Ewords001 = Entry(cacheW, width=20, borderwidth=4)
    Ewords002 = Entry(cacheW, width=20, borderwidth=4)
    Ewords003 = Entry(cacheW, width=20, borderwidth=4)
    Ewords004 = Entry(cacheW, width=20, borderwidth=4)
    Ewords005 = Entry(cacheW, width=20, borderwidth=4)
    Ewords006 = Entry(cacheW, width=20, borderwidth=4)
    Ewords007 = Entry(cacheW, width=20, borderwidth=4)
    Ewords010 = Entry(cacheW, width=20, borderwidth=4)
    Ewords011 = Entry(cacheW, width=20, borderwidth=4)
    Ewords012 = Entry(cacheW, width=20, borderwidth=4)
    Ewords013 = Entry(cacheW, width=20, borderwidth=4)
    Ewords014 = Entry(cacheW, width=20, borderwidth=4)
    Ewords015 = Entry(cacheW, width=20, borderwidth=4)
    Ewords016 = Entry(cacheW, width=20, borderwidth=4)
    Ewords017 = Entry(cacheW, width=20, borderwidth=4)
    Ewords020 = Entry(cacheW, width=20, borderwidth=4)
    Ewords021 = Entry(cacheW, width=20, borderwidth=4)
    Ewords022 = Entry(cacheW, width=20, borderwidth=4)
    Ewords023 = Entry(cacheW, width=20, borderwidth=4)
    Ewords024 = Entry(cacheW, width=20, borderwidth=4)
    Ewords025 = Entry(cacheW, width=20, borderwidth=4)
    Ewords026 = Entry(cacheW, width=20, borderwidth=4)
    Ewords027 = Entry(cacheW, width=20, borderwidth=4)
    Ewords030 = Entry(cacheW, width=20, borderwidth=4)
    Ewords031 = Entry(cacheW, width=20, borderwidth=4)
    Ewords032 = Entry(cacheW, width=20, borderwidth=4)
    Ewords033 = Entry(cacheW, width=20, borderwidth=4)
    Ewords034 = Entry(cacheW, width=20, borderwidth=4)
    Ewords035 = Entry(cacheW, width=20, borderwidth=4)
    Ewords036 = Entry(cacheW, width=20, borderwidth=4)
    Ewords037 = Entry(cacheW, width=20, borderwidth=4)
    Ewords040 = Entry(cacheW, width=20, borderwidth=4)
    Ewords041 = Entry(cacheW, width=20, borderwidth=4)
    Ewords042 = Entry(cacheW, width=20, borderwidth=4)
    Ewords043 = Entry(cacheW, width=20, borderwidth=4)
    Ewords044 = Entry(cacheW, width=20, borderwidth=4)
    Ewords045 = Entry(cacheW, width=20, borderwidth=4)
    Ewords046 = Entry(cacheW, width=20, borderwidth=4)
    Ewords047 = Entry(cacheW, width=20, borderwidth=4)
    Ewords050 = Entry(cacheW, width=20, borderwidth=4)
    Ewords051 = Entry(cacheW, width=20, borderwidth=4)
    Ewords052 = Entry(cacheW, width=20, borderwidth=4)
    Ewords053 = Entry(cacheW, width=20, borderwidth=4)
    Ewords054 = Entry(cacheW, width=20, borderwidth=4)
    Ewords055 = Entry(cacheW, width=20, borderwidth=4)
    Ewords056 = Entry(cacheW, width=20, borderwidth=4)
    Ewords057 = Entry(cacheW, width=20, borderwidth=4)
    Ewords060 = Entry(cacheW, width=20, borderwidth=4)
    Ewords061 = Entry(cacheW, width=20, borderwidth=4)
    Ewords062 = Entry(cacheW, width=20, borderwidth=4)
    Ewords063 = Entry(cacheW, width=20, borderwidth=4)
    Ewords064 = Entry(cacheW, width=20, borderwidth=4)
    Ewords065 = Entry(cacheW, width=20, borderwidth=4)
    Ewords066 = Entry(cacheW, width=20, borderwidth=4)
    Ewords067 = Entry(cacheW, width=20, borderwidth=4)
    Ewords070 = Entry(cacheW, width=20, borderwidth=4)
    Ewords071 = Entry(cacheW, width=20, borderwidth=4)
    Ewords072 = Entry(cacheW, width=20, borderwidth=4)
    Ewords073 = Entry(cacheW, width=20, borderwidth=4)
    Ewords074 = Entry(cacheW, width=20, borderwidth=4)
    Ewords075 = Entry(cacheW, width=20, borderwidth=4)
    Ewords076 = Entry(cacheW, width=20, borderwidth=4)
    Ewords077 = Entry(cacheW, width=20, borderwidth=4)
    Ewords080 = Entry(cacheW, width=20, borderwidth=4)
    Ewords081 = Entry(cacheW, width=20, borderwidth=4)
    Ewords082 = Entry(cacheW, width=20, borderwidth=4)
    Ewords083 = Entry(cacheW, width=20, borderwidth=4)
    Ewords084 = Entry(cacheW, width=20, borderwidth=4)
    Ewords085 = Entry(cacheW, width=20, borderwidth=4)
    Ewords086 = Entry(cacheW, width=20, borderwidth=4)
    Ewords087 = Entry(cacheW, width=20, borderwidth=4)
    Ewords090 = Entry(cacheW, width=20, borderwidth=4)
    Ewords091 = Entry(cacheW, width=20, borderwidth=4)
    Ewords092 = Entry(cacheW, width=20, borderwidth=4)
    Ewords093 = Entry(cacheW, width=20, borderwidth=4)
    Ewords094 = Entry(cacheW, width=20, borderwidth=4)
    Ewords095 = Entry(cacheW, width=20, borderwidth=4)
    Ewords096 = Entry(cacheW, width=20, borderwidth=4)
    Ewords097 = Entry(cacheW, width=20, borderwidth=4)
    Ewords100 = Entry(cacheW, width=20, borderwidth=4)
    Ewords101 = Entry(cacheW, width=20, borderwidth=4)
    Ewords102 = Entry(cacheW, width=20, borderwidth=4)
    Ewords103 = Entry(cacheW, width=20, borderwidth=4)
    Ewords104 = Entry(cacheW, width=20, borderwidth=4)
    Ewords105 = Entry(cacheW, width=20, borderwidth=4)
    Ewords106 = Entry(cacheW, width=20, borderwidth=4)
    Ewords107 = Entry(cacheW, width=20, borderwidth=4)
    Ewords110 = Entry(cacheW, width=20, borderwidth=4)
    Ewords111 = Entry(cacheW, width=20, borderwidth=4)
    Ewords112 = Entry(cacheW, width=20, borderwidth=4)
    Ewords113 = Entry(cacheW, width=20, borderwidth=4)
    Ewords114 = Entry(cacheW, width=20, borderwidth=4)
    Ewords115 = Entry(cacheW, width=20, borderwidth=4)
    Ewords116 = Entry(cacheW, width=20, borderwidth=4)
    Ewords117 = Entry(cacheW, width=20, borderwidth=4)
    Ewords120 = Entry(cacheW, width=20, borderwidth=4)
    Ewords121 = Entry(cacheW, width=20, borderwidth=4)
    Ewords122 = Entry(cacheW, width=20, borderwidth=4)
    Ewords123 = Entry(cacheW, width=20, borderwidth=4)
    Ewords124 = Entry(cacheW, width=20, borderwidth=4)
    Ewords125 = Entry(cacheW, width=20, borderwidth=4)
    Ewords126 = Entry(cacheW, width=20, borderwidth=4)
    Ewords127 = Entry(cacheW, width=20, borderwidth=4)
    Ewords130 = Entry(cacheW, width=20, borderwidth=4)
    Ewords131 = Entry(cacheW, width=20, borderwidth=4)
    Ewords132 = Entry(cacheW, width=20, borderwidth=4)
    Ewords133 = Entry(cacheW, width=20, borderwidth=4)
    Ewords134 = Entry(cacheW, width=20, borderwidth=4)
    Ewords135 = Entry(cacheW, width=20, borderwidth=4)
    Ewords136 = Entry(cacheW, width=20, borderwidth=4)
    Ewords137 = Entry(cacheW, width=20, borderwidth=4)
    Ewords140 = Entry(cacheW, width=20, borderwidth=4)
    Ewords141 = Entry(cacheW, width=20, borderwidth=4)
    Ewords142 = Entry(cacheW, width=20, borderwidth=4)
    Ewords143 = Entry(cacheW, width=20, borderwidth=4)
    Ewords144 = Entry(cacheW, width=20, borderwidth=4)
    Ewords145 = Entry(cacheW, width=20, borderwidth=4)
    Ewords146 = Entry(cacheW, width=20, borderwidth=4)
    Ewords147 = Entry(cacheW, width=20, borderwidth=4)
    Ewords150 = Entry(cacheW, width=20, borderwidth=4)
    Ewords151 = Entry(cacheW, width=20, borderwidth=4)
    Ewords152 = Entry(cacheW, width=20, borderwidth=4)
    Ewords153 = Entry(cacheW, width=20, borderwidth=4)
    Ewords154 = Entry(cacheW, width=20, borderwidth=4)
    Ewords155 = Entry(cacheW, width=20, borderwidth=4)
    Ewords156 = Entry(cacheW, width=20, borderwidth=4)
    Ewords157 = Entry(cacheW, width=20, borderwidth=4)
    # for i in range(16):
    #     for j in range(8):
    #         if i < 10:
    #             exec("Ewords" + '0' + str(i) +str(j) + '=' + "Entry(cacheW, width=20, borderwidth=4)")
    #         else :
    #             exec("Ewords" + str(i) + str(j) + '=' + "Entry(cacheW, width=20, borderwidth=4)")
    # Cache.cache[1][8] = "123"
    # insert Cache data into textbox
    for i in range(16): # insert valid value
        if Cache.cache[i][0] != "0":
            exec("Valid" + str(i) + ".insert(0," + str(Cache.cache[i][0]) + ')')
    for i in range(16): # insert Block Number
        if Cache.cache[i][1] != "0":
            exec("Blk_Num" + str(i) + ".insert(0," + str(Cache.cache[i][1]) + ')')
    for i in range(16):  # insert Block Number
        for j in range(2, 10):
            if Cache.cache[i][j] != "0":
                if i >= 10:
                    exec("Ewords" + str(i) + str(j-2) + ".insert(0," + str(Cache.cache[i][j]) + ')')
                else:
                    exec("Ewords" + '0' + str(i) + str(j-2) + ".insert(0," + str(Cache.cache[i][j]) + ')')


    #refresh cache windows
    def refresh():
        cacheW.destroy()
        open()

    def clearCache():
        Cache.cache=["0"]*16
        for elements in range(16):
            Cache.cache[elements] = ["0"] * 10
        # Idx0.delete(0, END)
        # Idx1.delete(0, END)
        # Idx2.delete(0, END)
        # Idx3.delete(0, END)
        # Idx4.delete(0, END)
        # Idx5.delete(0, END)
        # Idx6.delete(0, END)
        # Idx7.delete(0, END)
        # Idx8.delete(0, END)
        # Idx9.delete(0, END)
        # Idx10.delete(0, END)
        # Idx11.delete(0, END)
        # Idx12.delete(0, END)
        # Idx13.delete(0, END)
        # Idx14.delete(0, END)
        # Idx15.delete(0, END)
        Blk_Num0.delete(0, END)
        Blk_Num1.delete(0, END)
        Blk_Num2.delete(0, END)
        Blk_Num3.delete(0, END)
        Blk_Num4.delete(0, END)
        Blk_Num5.delete(0, END)
        Blk_Num6.delete(0, END)
        Blk_Num7.delete(0, END)
        Blk_Num8.delete(0, END)
        Blk_Num9.delete(0, END)
        Blk_Num10.delete(0, END)
        Blk_Num11.delete(0, END)
        Blk_Num12.delete(0, END)
        Blk_Num13.delete(0, END)
        Blk_Num14.delete(0, END)
        Blk_Num15.delete(0, END)
        Valid0.delete(0, END)
        Valid1.delete(0, END)
        Valid2.delete(0, END)
        Valid3.delete(0, END)
        Valid4.delete(0, END)
        Valid5.delete(0, END)
        Valid6.delete(0, END)
        Valid7.delete(0, END)
        Valid8.delete(0, END)
        Valid9.delete(0, END)
        Valid10.delete(0, END)
        Valid11.delete(0, END)
        Valid12.delete(0, END)
        Valid13.delete(0, END)
        Valid14.delete(0, END)
        Valid15.delete(0, END)
        Ewords000.delete(0, END)
        Ewords001.delete(0, END)
        Ewords002.delete(0, END)
        Ewords003.delete(0, END)
        Ewords004.delete(0, END)
        Ewords005.delete(0, END)
        Ewords006.delete(0, END)
        Ewords007.delete(0, END)
        Ewords010.delete(0, END)
        Ewords011.delete(0, END)
        Ewords012.delete(0, END)
        Ewords013.delete(0, END)
        Ewords014.delete(0, END)
        Ewords015.delete(0, END)
        Ewords016.delete(0, END)
        Ewords017.delete(0, END)
        Ewords020.delete(0, END)
        Ewords021.delete(0, END)
        Ewords022.delete(0, END)
        Ewords023.delete(0, END)
        Ewords024.delete(0, END)
        Ewords025.delete(0, END)
        Ewords026.delete(0, END)
        Ewords027.delete(0, END)
        Ewords030.delete(0, END)
        Ewords031.delete(0, END)
        Ewords032.delete(0, END)
        Ewords033.delete(0, END)
        Ewords034.delete(0, END)
        Ewords035.delete(0, END)
        Ewords036.delete(0, END)
        Ewords037.delete(0, END)
        Ewords040.delete(0, END)
        Ewords041.delete(0, END)
        Ewords042.delete(0, END)
        Ewords043.delete(0, END)
        Ewords044.delete(0, END)
        Ewords045.delete(0, END)
        Ewords046.delete(0, END)
        Ewords047.delete(0, END)
        Ewords050.delete(0, END)
        Ewords051.delete(0, END)
        Ewords052.delete(0, END)
        Ewords053.delete(0, END)
        Ewords054.delete(0, END)
        Ewords055.delete(0, END)
        Ewords056.delete(0, END)
        Ewords057.delete(0, END)
        Ewords060.delete(0, END)
        Ewords061.delete(0, END)
        Ewords062.delete(0, END)
        Ewords063.delete(0, END)
        Ewords064.delete(0, END)
        Ewords065.delete(0, END)
        Ewords066.delete(0, END)
        Ewords067.delete(0, END)
        Ewords070.delete(0, END)
        Ewords071.delete(0, END)
        Ewords072.delete(0, END)
        Ewords073.delete(0, END)
        Ewords074.delete(0, END)
        Ewords075.delete(0, END)
        Ewords076.delete(0, END)
        Ewords077.delete(0, END)
        Ewords080.delete(0, END)
        Ewords081.delete(0, END)
        Ewords082.delete(0, END)
        Ewords083.delete(0, END)
        Ewords084.delete(0, END)
        Ewords085.delete(0, END)
        Ewords086.delete(0, END)
        Ewords087.delete(0, END)
        Ewords090.delete(0, END)
        Ewords091.delete(0, END)
        Ewords092.delete(0, END)
        Ewords093.delete(0, END)
        Ewords094.delete(0, END)
        Ewords095.delete(0, END)
        Ewords096.delete(0, END)
        Ewords097.delete(0, END)
        Ewords100.delete(0, END)
        Ewords101.delete(0, END)
        Ewords102.delete(0, END)
        Ewords103.delete(0, END)
        Ewords104.delete(0, END)
        Ewords105.delete(0, END)
        Ewords106.delete(0, END)
        Ewords107.delete(0, END)
        Ewords110.delete(0, END)
        Ewords111.delete(0, END)
        Ewords112.delete(0, END)
        Ewords113.delete(0, END)
        Ewords114.delete(0, END)
        Ewords115.delete(0, END)
        Ewords116.delete(0, END)
        Ewords117.delete(0, END)
        Ewords120.delete(0, END)
        Ewords121.delete(0, END)
        Ewords122.delete(0, END)
        Ewords123.delete(0, END)
        Ewords124.delete(0, END)
        Ewords125.delete(0, END)
        Ewords126.delete(0, END)
        Ewords127.delete(0, END)
        Ewords130.delete(0, END)
        Ewords131.delete(0, END)
        Ewords132.delete(0, END)
        Ewords133.delete(0, END)
        Ewords134.delete(0, END)
        Ewords135.delete(0, END)
        Ewords136.delete(0, END)
        Ewords137.delete(0, END)
        Ewords140.delete(0, END)
        Ewords141.delete(0, END)
        Ewords142.delete(0, END)
        Ewords143.delete(0, END)
        Ewords144.delete(0, END)
        Ewords145.delete(0, END)
        Ewords146.delete(0, END)
        Ewords147.delete(0, END)
        Ewords150.delete(0, END)
        Ewords151.delete(0, END)
        Ewords152.delete(0, END)
        Ewords153.delete(0, END)
        Ewords154.delete(0, END)
        Ewords155.delete(0, END)
        Ewords156.delete(0, END)
        Ewords157.delete(0, END)
        #     exec("Idx" + str(i) + ".delete(0,END)")
        #     exec("Blk_Num" + str(i) + ".delete(0,END)")
        #     exec("Valid" + str(i) + ".delete(0,END)")
        # for i in range(16):
        #     for j in range(8):
        #         if i < 10:
        #             exec("Ewords" + '0' + str(i) + str(j) + ".delete(0,END)")
        #         else:
        #             exec("Ewords" + str(i) + str(j) + ".delete(0,END)")


    #define Button
    RefreshBtn =Button(cacheW,text="Refresh",padx=10, pady=15, command=refresh)
    ClearBtn = Button(cacheW,text="Clear",padx=10, pady=15, command=clearCache)
    Pro1Btn = Button(cacheW, text="Program 1", padx=10, pady=15, command=Program1.pro1)

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
    ClearBtn.grid(row=20, column=9)
    Pro1Btn.grid(row=20, column=8)





