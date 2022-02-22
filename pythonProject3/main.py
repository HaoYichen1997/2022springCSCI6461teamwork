
""" 
 
Creater:Zack 
Date:01/21/2022 
 
"""
from tkinter import *
from tkinter import filedialog
from textwrap import wrap
import register as reg
import instructions as instr
import time
# from PIL import Image, ImageTk
# from tkinter.filedialog import askopenfile


#Basic interface made by Zihao Wen
root = Tk()
root.title("6461 Project1")
root.geometry("1130x450")
# Btn Frame made by Zihao Wen
frameBtn =  LabelFrame(root, text="Num Button")
frameBtn.grid(row=9,column=1,columnspan=5,padx=50, pady=10)
frameOpBtn =  LabelFrame(root, text="Op Button")
frameOpBtn.grid(row=8,column=6,columnspan=1,padx=50, pady=10)
frameSysBtn =  LabelFrame(root, text="Sys Button")
frameSysBtn.grid(row=9,column=6,columnspan=1,padx=50, pady=10)

#Label of the panel made by Zihao Wen
    #GPR Label
GPR0Label = Label(root, text="GPR 0(16bits)")
GPR1Label = Label(root, text="GPR 1(16bits)")
GPR2Label = Label(root, text="GPR 2(16bits)")
GPR3Label = Label(root, text="GPR 3(16bits)")
    #Space between GPR & IXR
SpaceGPRIXR = Label(root, text=" ")
    #IXR Label
IXR1Label = Label(root, text="IXR1(16bits)")
IXR2Label = Label(root, text="IXR2(16bits)")
IXR3Label = Label(root, text="IXR3(16bits)")
    #Space between IXR and Num Button & GPR & PC & etc
SpaceIXROperation = Label(root, text=" ")
SpaceGPRPC = Label(root, text=" ")
    #Panel right Label
PCLabel = Label(root, text="PC(12bits)")
MARLabel = Label(root, text="MAR(12bits)")
MBRLabel = Label(root, text="MBR(16bits)")
IRLabel = Label(root, text="IR(16bits)")
MFRLabel = Label(root, text="MFR(4bits)")
PrivailegedLabel = Label(root, text="Privileged(1bits)")
    #Sys Button
SpaceSSRUN = Label(frameSysBtn, text="          ")
HaltLabel =Label(frameSysBtn, text="Halt")
RunLabel =Label(frameSysBtn, text="Run")


#Textbox(light) made by Zihao Wen
GPR0 = Entry(root, width=60, borderwidth=5,)
GPR1 = Entry(root, width=60, borderwidth=5)
GPR2 = Entry(root, width=60, borderwidth=5)
GPR3 = Entry(root, width=60, borderwidth=5)

IXR1 = Entry(root, width=60, borderwidth=5)
IXR2 = Entry(root, width=60, borderwidth=5)
IXR3 = Entry(root, width=60, borderwidth=5)

PC = Entry(root, width=60, borderwidth=5)
MAR = Entry(root, width=60, borderwidth=5)
MBR = Entry(root, width=60, borderwidth=5)
IR = Entry(root, width=60, borderwidth=5)
MFR = Entry(root, width=60, borderwidth=5)
Privaileged = Entry(root, width=60, borderwidth=5)

RunLight = Entry(frameSysBtn, width=1, borderwidth=1)
HaltLight = Entry(frameSysBtn, width=1, borderwidth=1)

#define intial value made by Zihao Wen
num15: int =0
num14: int =0
num13: int =0
num12: int =0
num11: int =0
num10: int =0
num9: int =0
num8: int =0
num7: int =0
num6: int =0
num5: int =0
num4: int =0
num3: int =0
num2: int =0
num1: int =0
num0: int =0


GPR0.insert(0,"0000000000000000")
GPR1.insert(0,"0000000000000000")
GPR2.insert(0,"0000000000000000")
GPR3.insert(0,"0000000000000000")
IXR1.insert(0,"0000000000000000")
IXR2.insert(0,"0000000000000000")
IXR3.insert(0,"0000000000000000")

PC.insert(0,"000000000000")
MAR.insert(0,"000000000000")
MBR.insert(0,"0000000000000000")
IR.insert(0,"0000000000000000")
MFR.insert(0,"0000")
Privaileged.insert(0,"0")
RunLight.insert(0,"0")
HaltLight.insert(0,"0")

MAR_num = ''
MBR_num = ''




#Btn Status made by Zihao Wen
Status15 = Label(frameBtn, text="" + str(num15))
Status14 = Label(frameBtn, text="" + str(num14))
Status13 = Label(frameBtn, text="" + str(num13))
Status12 = Label(frameBtn, text="" + str(num12))
Status11 = Label(frameBtn, text="" + str(num11))
Status10 = Label(frameBtn, text="" + str(num10))
Status9 = Label(frameBtn, text="" + str(num9))
Status8 = Label(frameBtn, text="" + str(num8))
Status7 = Label(frameBtn, text="" + str(num7))
Status6 = Label(frameBtn, text="" + str(num6))
Status5 = Label(frameBtn, text="" + str(num5))
Status4 = Label(frameBtn, text="" + str(num4))
Status3 = Label(frameBtn, text="" + str(num3))
Status2 = Label(frameBtn, text="" + str(num2))
Status1 = Label(frameBtn, text="" + str(num1))
Status0 = Label(frameBtn, text="" + str(num0))

#Click number BTN modification made by Zihao Wen
#default button is Blue color and number 0, clicking it will change it to red and number 1. And Click again, it will be return to blue and number 0
def Click15(): #Named by corresponding number button, such as click15 is Num Button 15's function.
    global Status15
    global num15
    global Btn15
    if num15 != 1:
        num15 = 1
        Btn15.grid_forget()
        Btn15 = Button(frameBtn, text="15", padx=5, pady=15, bg="red", fg="yellow", command = Click15)
        Btn15.grid(row=14, column=0)
    else:
        num15 = 0
        Btn15.grid_forget()
        Btn15 = Button(frameBtn, text="15", padx=5, pady=16, bg="blue", fg="white", command = Click15)
        Btn15.grid(row=14, column=0)
    Status15 = Label(frameBtn, text="" + str(num15))
    Status15.grid(row=15, column=0)
    print(num15)
    return
def Click14():
    global Status14
    global num14
    global Btn14
    if num14 != 1:
        num14 = 1
        Btn14.grid_forget()
        Btn14 = Button(frameBtn, text="14", padx=5, pady=16, bg="red", fg="yellow", command = Click14)
        Btn14.grid(row=14, column=1)
    else:
        num14 = 0
        Btn14.grid_forget()
        Btn14 = Button(frameBtn, text="14", padx=5, pady=16, bg="blue", fg="white", command = Click14)
        Btn14.grid(row=14, column=1)
    Status14 = Label(frameBtn, text="" + str(num14))
    Status14.grid(row=15, column=1)
    print(num14)
    return
def Click13():
    global Status13
    global num13
    global Btn13
    if num13 != 1:
        num13 = 1
        Btn13.grid_forget()
        Btn13 = Button(frameBtn, text="13", padx=5, pady=16, bg="red", fg="yellow", command = Click13)
        Btn13.grid(row=14, column=2)
    else:
        num13 = 0
        Btn13.grid_forget()
        Btn13 = Button(frameBtn, text="13", padx=5, pady=16, bg="blue", fg="white", command = Click13)
        Btn13.grid(row=14, column=2)
    Status13 = Label(frameBtn, text="" + str(num13))
    Status13.grid(row=15, column=2)
    print(num13)
    return
def Click12():
    global Status12
    global num12
    global Btn12
    if num12 != 1:
        num12 = 1
        Btn12.grid_forget()
        Btn12 = Button(frameBtn, text="12", padx=5, pady=16, bg="red", fg="yellow", command = Click12)
        Btn12.grid(row=14, column=3)
    else:
        num12 = 0
        Btn12.grid_forget()
        Btn12 = Button(frameBtn, text="12", padx=5, pady=16, bg="blue", fg="white", command = Click12)
        Btn12.grid(row=14, column=3)
    Status12 = Label(frameBtn, text="" + str(num12))
    Status12.grid(row=15, column=3)
    print(num12)
    return
def Click11():
    global Status11
    global num11
    global Btn11
    if num11 != 1:
        num11 = 1
        Btn11.grid_forget()
        Btn11 = Button(frameBtn, text="11", padx=5, pady=16, bg="red", fg="yellow", command = Click11)
        Btn11.grid(row=14, column=4)
    else:
        num11 = 0
        Btn11.grid_forget()
        Btn11 = Button(frameBtn, text="11", padx=5, pady=16, bg="blue", fg="white", command = Click11)
        Btn11.grid(row=14, column=4)
    Status11 = Label(frameBtn, text="" + str(num11))
    Status11.grid(row=15, column=4)
    print(num11)
    return
def Click10():
    global Status10
    global num10
    global Btn10
    if num10 != 1:
        num10 = 1
        Btn10.grid_forget()
        Btn10 = Button(frameBtn, text="10", padx=5, pady=16, bg="red", fg="yellow", command = Click10)
        Btn10.grid(row=14, column=5)
    else:
        num10 = 0
        Btn10.grid_forget()
        Btn10 = Button(frameBtn, text="10", padx=5, pady=16, bg="blue", fg="white", command = Click10)
        Btn10.grid(row=14, column=5)
    Status10 = Label(frameBtn, text="" + str(num10))
    Status10.grid(row=15, column=5)
    print(num10)
    return
def Click9():
    global Status9
    global num9
    global Btn9
    if num9 != 1:
        num9 = 1
        Btn9.grid_forget()
        Btn9 = Button(frameBtn, text="9", padx=5, pady=16, bg="red", fg="yellow", command = Click9)
        Btn9.grid(row=14, column=6)
    else:
        num9 = 0
        Btn9.grid_forget()
        Btn9 = Button(frameBtn, text="9", padx=5, pady=16, bg="blue", fg="white", command = Click9)
        Btn9.grid(row=14, column=6)
    Status9 = Label(frameBtn, text="" + str(num9))
    Status9.grid(row=15, column=6)
    print(num9)
    return
def Click8():
    global Status8
    global num8
    global Btn8
    if num8 != 1:
        num8 = 1
        Btn8.grid_forget()
        Btn8 = Button(frameBtn, text="8", padx=5, pady=16, bg="red", fg="yellow", command = Click8)
        Btn8.grid(row=14, column=7)
    else:
        num8 = 0
        Btn8.grid_forget()
        Btn8 = Button(frameBtn, text="8", padx=5, pady=16, bg="blue", fg="white", command = Click8)
        Btn8.grid(row=14, column=7)
    Status8 = Label(frameBtn, text="" + str(num8))
    Status8.grid(row=15, column=7)
    print(num8)
    return
def Click7():
    global Status7
    global num7
    global Btn7
    if num7 != 1:
        num7 = 1
        Btn7.grid_forget()
        Btn7 = Button(frameBtn, text="7", padx=5, pady=16, bg="red", fg="yellow", command = Click7)
        Btn7.grid(row=14, column=8)
    else:
        num7 = 0
        Btn7.grid_forget()
        Btn7 = Button(frameBtn, text="7", padx=5, pady=16, bg="blue", fg="white", command = Click7)
        Btn7.grid(row=14, column=8)
    Status7 = Label(frameBtn, text="" + str(num7))
    Status7.grid(row=15, column=8)
    print(num7)
    return
def Click6():
    global Status6
    global num6
    global Btn6
    if num6 != 1:
        num6 = 1
        Btn6.grid_forget()
        Btn6 = Button(frameBtn, text="6", padx=5, pady=16, bg="red", fg="yellow", command = Click6)
        Btn6.grid(row=14, column=9)
    else:
        num6 = 0
        Btn6.grid_forget()
        Btn6 = Button(frameBtn, text="6", padx=5, pady=16, bg="blue", fg="white", command = Click6)
        Btn6.grid(row=14, column=9)
    Status6 = Label(frameBtn, text="" + str(num6))
    Status6.grid(row=15, column=9)
    print(num6)
    return
def Click5():
    global Status5
    global num5
    global Btn5
    if num5 != 1:
        num5 = 1
        Btn5.grid_forget()
        Btn5 = Button(frameBtn, text="5", padx=5, pady=16, bg="red", fg="yellow", command = Click5)
        Btn5.grid(row=14, column=10)
    else:
        num5 = 0
        Btn5.grid_forget()
        Btn5 = Button(frameBtn, text="5", padx=5, pady=16, bg="blue", fg="white", command = Click5)
        Btn5.grid(row=14, column=10)
    Status5 = Label(frameBtn, text="" + str(num5))
    Status5.grid(row=15, column=10)
    print(num5)
    return
def Click4():
    global Status4
    global num4
    global Btn4
    if num4 != 1:
        num4 = 1
        Btn4.grid_forget()
        Btn4 = Button(frameBtn, text="4", padx=5, pady=16, bg="red", fg="yellow", command = Click4)
        Btn4.grid(row=14, column=11)
    else:
        num4 = 0
        Btn4.grid_forget()
        Btn4 = Button(frameBtn, text="4", padx=5, pady=16, bg="blue", fg="white", command = Click4)
        Btn4.grid(row=14, column=11)
    Status4 = Label(frameBtn, text="" + str(num4))
    Status4.grid(row=15, column=11)
    print(num4)
    return
def Click3():
    global Status3
    global num3
    global Btn3
    if num3 != 1:
        num3 = 1
        Btn3.grid_forget()
        Btn3 = Button(frameBtn, text="3", padx=5, pady=16, bg="red", fg="yellow", command = Click3)
        Btn3.grid(row=14, column=12)
    else:
        num3 = 0
        Btn3.grid_forget()
        Btn3 = Button(frameBtn, text="3", padx=5, pady=16, bg="blue", fg="white", command = Click3)
        Btn3.grid(row=14, column=12)
    Status3 = Label(frameBtn, text="" + str(num3))
    Status3.grid(row=15, column=12)
    print(num3)
    return
def Click2():
    global Status2
    global num2
    global Btn2
    if num2 != 1:
        num2 = 1
        Btn2.grid_forget()
        Btn2 = Button(frameBtn, text="2", padx=5, pady=16, bg="red", fg="yellow", command = Click2)
        Btn2.grid(row=14, column=13)
    else:
        num2 = 0
        Btn2.grid_forget()
        Btn2 = Button(frameBtn, text="2", padx=5, pady=16, bg="blue", fg="white", command = Click2)
        Btn2.grid(row=14, column=13)
    Status2 = Label(frameBtn, text="" + str(num2))
    Status2.grid(row=15, column=13)
    print(num2)
    return
def Click1():
    global Status1
    global num1
    global Btn1
    if num1 != 1:
        num1 = 1
        Btn1.grid_forget()
        Btn1 = Button(frameBtn, text="1", padx=5, pady=16, bg="red", fg="yellow", command = Click1)
        Btn1.grid(row=14, column=14)
    else:
        num1 = 0
        Btn1.grid_forget()
        Btn1 = Button(frameBtn, text="1", padx=5, pady=16, bg="blue", fg="white", command = Click1)
        Btn1.grid(row=14, column=14)
    Status1 = Label(frameBtn, text="" + str(num1))
    Status1.grid(row=15, column=14)
    print(num1)
    return
def Click0():
    global Status0
    global num0
    global Btn0
    if num0 != 1:
        num0 = 1
        Btn0.grid_forget()
        Btn0 = Button(frameBtn, text="0", padx=5, pady=16, bg="red", fg="yellow", command = Click0)
        Btn0.grid(row=14, column=15)
    else:
        num0 = 0
        Btn0.grid_forget()
        Btn0 = Button(frameBtn, text="0", padx=5, pady=16, bg="blue", fg="white", command = Click0)
        Btn0.grid(row=14, column=15)
    Status0 = Label(frameBtn, text="" + str(num0))
    Status0.grid(row=15, column=15)
    print(num0)
    return

#Click LD BTN modification made by Zihao Wen
    #Clicking LD button will trigger these function, it will load number data from all the Num Button(at the bottom of the panel) to Textbox
        #For example, you click the LD button behind 'GPR0', GPR0 will be changed to the number of Num Button.
def LD_GPR0():
    GPR0.delete(0,END)
    GPR0.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    GPR0_num = GPR0.get()
    instr.gpr0.set(string_to_strlist(GPR0_num))
    return
def LD_GPR1():
    GPR1.delete(0,END)
    GPR1.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    GPR1_num = GPR1.get()
    instr.gpr1.set(string_to_strlist(GPR1_num))
    return
def LD_GPR2():
    GPR2.delete(0,END)
    GPR2.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    GPR2_num = GPR2.get()
    instr.gpr2.set(string_to_strlist(GPR2_num))
    return
def LD_GPR3():
    GPR3.delete(0,END)
    GPR3.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    GPR3_num = GPR3.get()
    instr.gpr3.set(string_to_strlist(GPR3_num))
    return
def LD_IXR1():
    IXR1.delete(0,END)
    IXR1.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    IXR1_num = IXR1.get()
    instr.ixr1.set(string_to_strlist(IXR1_num))
    return
def LD_IXR2():
    IXR2.delete(0,END)
    IXR2.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    IXR2_num = IXR2.get()
    instr.ixr2.set(string_to_strlist(IXR2_num))
    return
def LD_IXR3():
    IXR3.delete(0,END)
    IXR3.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    IXR3_num = IXR3.get()
    instr.ixr3.set(string_to_strlist(IXR3_num))
    return
def LD_PC():
    PC.delete(0,END)
    PC.insert(0,str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    PC_num = PC.get()
    instr.pc.set(string_to_strlist(PC_num))
    return
def LD_MAR():
    global MAR_num
    MAR.delete(0,END)
    MAR.insert(0,str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    MAR_num = MAR.get()
    instr.mar.set(string_to_strlist(MAR_num))
    print(MAR_num)
    return
def LD_MBR():
    global MBR_num
    MBR.delete(0,END)
    MBR.insert(0,str(num15)+str(num14)+str(num13)+str(num12)+str(num11)+str(num10)+str(num9)+str(num8)+str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1)+str(num0))
    MBR_num = MBR.get()
    instr.mbr.set(string_to_strlist(MBR_num))
    print(MBR_num)
    return


def string_to_strlist(str):
    return [num for num in str]

def show_Reg_to_Panel(a: str, num):    #test for uniform update
    if a == "mar":
        MAR.delete(0, END)
        MAR.insert(0, ''.join(i for i in num))
    elif a == "mbr":
        MBR.delete(0, END)
        MBR.insert(0, ''.join(i for i in num))
    elif a == "pc":
        PC.delete(0, END)
        PC.insert(0, ''.join(i for i in num))
    elif a == "ir":
        IR.delete(0, END)
        IR.insert(0, ''.join(i for i in num))
    elif a == "gpr0":
        GPR0.delete(0, END)
        GPR0.insert(0, ''.join(i for i in num))
    elif a == "gpr1":
        GPR1.delete(0, END)
        GPR1.insert(0, ''.join(i for i in num))
    elif a == "gpr2":
        GPR2.delete(0, END)
        GPR2.insert(0, ''.join(i for i in num))
    elif a == "gpr3":
        GPR3.delete(0, END)
        GPR3.insert(0, ''.join(i for i in num))
    elif a == "ixr1":
        IXR1.delete(0, END)
        IXR1.insert(0, ''.join(i for i in num))
    elif a == "ixr2":
        IXR2.delete(0, END)
        IXR2.insert(0, ''.join(i for i in num))
    elif a == "ixr3":
        IXR3.delete(0, END)
        IXR3.insert(0, ''.join(i for i in num))
    elif a == "halt":
        HaltLight.delete(0, END)
        HaltLight.insert(0, "1")
        RunLight.delete(0, END)
        RunLight.insert(0, "0")
    else: print("incorrect name of regs")
def show_Fetch(result):
    HaltLight.delete(0, END)
    HaltLight.insert(0, "0")
    RunLight.delete(0, END)
    RunLight.insert(0, "1")
    show_Reg_to_Panel('pc',instr.pc.num)
    for i in range(0, len(result), 2):
        show_Reg_to_Panel(result[i], result[i+1])

def show_Ldr001(result):
    for i in range(0, len(result), 2):
        show_Reg_to_Panel(result[i], result[i+1])

def show_general(result):
    for i in range(0, len(result), 2):
        show_Reg_to_Panel(result[i], result[i+1])




def run_Single_Step():
    opcode = int("".join(i for i in instr.ir.num[:6]), 2)
    if opcode == 1:
        ldr001_result = instr.ldr001(instr.ir.num)
        show_general(ldr001_result)
        print('opcode is 001')
    elif opcode == 2:
        str002_result = instr.str002(instr.ir.num)
        print('opcode is 002')
        show_general(str002_result)
    elif opcode == 3:
        lda003_result = instr.lda003(instr.ir.num)
        print('opcode is 003')
        show_general(lda003_result)
    elif opcode == 33:
        ldx041_result = instr.ldx041(instr.ir.num)
        print('opcode is 041')
        show_general(ldx041_result)
    elif opcode == 34:
        stx042_result = instr.stx042(instr.ir.num)
        print('opcode is 042')
        show_general(stx042_result)
    elif opcode == 0:
        halt000_result = instr.halt000()
        print('opcode is halt')
        show_general(halt000_result)
    else: print("incorrect opcode",opcode)

def SS():
    print("single step")
    fetch_result = instr.fetch(instr.pc.num)
    show_Fetch(fetch_result)
    run_Single_Step()

def run_instructions():
    print("run now")
    while True:
        fetch_result = instr.fetch(instr.pc.num)
        show_Fetch(fetch_result)
        #pc=pc+1:
        pc_bin = ''.join(i for i in instr.pc.num)
        pc_dec = int(pc_bin, 2)
        pc = pc_dec+1
        data = bin(pc)[2:].zfill(16)
        instr.pc.set(string_to_strlist(str(data)))
        run_Single_Step()
        print(instr.ir.num)
        if HaltLight.get() == '1':
            print("stop now")
            break
        root.update()
        time.sleep(4)


    #Binary translate to Decimal made by Zihao Wen
def BinaryTurnDec(Str) :
    sumTwo1 : int = 0
    sumTwo: int = 0
    global TurnString
    TurnString = Str
    if len(TurnString) == 16:
        for i in range(len(TurnString)):
            sumTwo1 = int(TurnString[i])*(2**(15-i))
            sumTwo = sumTwo+sumTwo1
    if len(TurnString) == 12:
        for i in range(len(TurnString)):
            sumTwo1 = int(TurnString[i])*(2**(11-i))
            sumTwo = sumTwo+sumTwo1
    return sumTwo

#Binary plus one, it can be used Binary number plus one,and return the results made by Zihao Wen
def BinaryPlusOne(S1) :
    Str = list(S1)
    j: int = 0
    for i in range(len(Str)):
        # print(int(len(Str))- i)
        if Str[int(len(Str)) - i - 1] == '0' and j == 0:
            Str[int(len(Str)) - i - 1] = '1'
            j = 0
            break
        elif Str[int(len(Str)) - i - 1] == '1':
            Str[int(len(Str)) - i - 1] = '0'
            j = 1
        elif Str[int(len(Str)) - i - 1] == '0' and j == 1:
            Str[int(len(Str)) - i - 1] = '1'
            j = 0
            break
    S1 = ''.join(Str)
    print('Binary Plus results:'+S1)
    return S1
#Store button's function, it will store data from MAR&MBR BOX to Memory made by Zihao Wen
def Store():
    Store_MARnum = MAR_num
    Store_MBRnum = MBR_num
    for i in range(len(MBR_num)):
         instr.memory[BinaryTurnDec(Store_MARnum)][i]=int(Store_MBRnum[i])
    # print('MBR Value'+''.join(instr.memory[BinaryTurnDec(Store_MARnum)]))
    return
#Store button's function, it will store data from MAR&MBR BOX to Memory, and MAR's binary number will plus one made by Zihao Wen
def StorePlus():
    global MAR_num
    Store_MARnum = MAR.get()
    Store_MBRnum = MBR.get()
    if MAR.get() !='111111111111':
        for i in range(len(MBR_num)):
            instr.memory[BinaryTurnDec(Store_MARnum)][i]=int(Store_MBRnum[i])
        MAR.delete(0, END)
        MAR.insert(0,BinaryPlusOne(Store_MARnum))
        MAR_num=BinaryPlusOne(MAR_num)
        print('MAR='+MAR_num)
    elif MAR.get() =='111111111111':
        for i in range(len(MBR_num)):
            instr.memory[BinaryTurnDec(Store_MARnum)][i]=int(Store_MBRnum[i])
        MAR.delete(0, END)
        MAR.insert(0, '000000000000')
        MAR_num = '000000000000'
        print('MAR=' + MAR_num+'is out of range')
    return
#Load number from Memory made by Zihao Wen
def Load():
    MBR.delete(0, END)
    temp1=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # print(range(len(instr.memory[BinaryTurnDec(MAR.get())])))
    for i in range(len(instr.memory[BinaryTurnDec(MAR.get())])):
        temp1[i] =  str(instr.memory[BinaryTurnDec(MAR.get())][i])
    MBR.insert(0, ''.join(temp1))
    # print('Load MBR='+''.join(instr.memory[BinaryTurnDec(MAR.get())]))
    return


# Init function
# open filedialog and allow user to select a file to load into memory
def ClickInit():
    try:
        initText = filedialog.askopenfilename(initialdir="/pythonProject3", title="Select a text file",
                                              filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        with open(initText, encoding="utf-8") as f:
            lines = f.readlines()
        count = 0
        for line in lines:
            count += 1
            line = line.strip('\n')
            address, data = line.split(" ")
            # transform hex to decimal or binary
            address = int(address, 16)
            data = bin(int(data, 16))[2:].zfill(16)
            # store data into memory
            for i in range(16):
                instr.memory[address][i] = data[i]
            print(instr.memory[address])
        print("Current contents in memory:")
        print("Address" + "\t data")
        for item in instr.memory:
            content = "".join([str(_) for _ in item])
            if content != "0000000000000000":
                print(instr.memory.index(item), content)
    except FileNotFoundError:
        print('No such file or directory!')



#Btn made by Zihao Wen
    #Num Button
Btn15 = Button(frameBtn, text="15", padx=5, pady=15, bg="blue", fg="white", command = Click15)
Btn14 = Button(frameBtn, text="14", padx=5, pady=15, bg="blue", fg="white", command = Click14)
Btn13 = Button(frameBtn, text="13", padx=5, pady=15, bg="blue", fg="white", command = Click13)
Btn12 = Button(frameBtn, text="12", padx=5, pady=15, bg="blue", fg="white", command = Click12)
Btn11 = Button(frameBtn, text="11", padx=5, pady=15, bg="blue", fg="white", command = Click11)
Btn10 = Button(frameBtn, text="10", padx=5, pady=15, bg="blue", fg="white", command = Click10)
Btn9 = Button(frameBtn, text="9", padx=5, pady=15, bg="blue", fg="white", command = Click9)
Btn8 = Button(frameBtn, text="8", padx=5, pady=15, bg="blue", fg="white", command = Click8)
Btn7 = Button(frameBtn, text="7", padx=5, pady=15, bg="blue", fg="white", command = Click7)
Btn6 = Button(frameBtn, text="6", padx=5, pady=15, bg="blue", fg="white", command = Click6)
Btn5 = Button(frameBtn, text="5", padx=5, pady=15, bg="blue", fg="white", command = Click5)
Btn4 = Button(frameBtn, text="4", padx=5, pady=15, bg="blue", fg="white", command = Click4)
Btn3 = Button(frameBtn, text="3", padx=5, pady=15, bg="blue", fg="white", command = Click3)
Btn2 = Button(frameBtn, text="2", padx=5, pady=15, bg="blue", fg="white", command = Click2)
Btn1 = Button(frameBtn, text="1", padx=5, pady=15, bg="blue", fg="white", command = Click1)
Btn0 = Button(frameBtn, text="0", padx=5, pady=15, bg="blue", fg="white", command = Click0)
    #GPR LD Button
GPR0_LD = Button(root,text="LD",padx=1, pady=1,command = LD_GPR0)
GPR1_LD = Button(root,text="LD",padx=1, pady=1,command = LD_GPR1)
GPR2_LD = Button(root,text="LD",padx=1, pady=1,command = LD_GPR2)
GPR3_LD = Button(root,text="LD",padx=1, pady=1,command = LD_GPR3)
    #IXR LD Button
IXR1_LD = Button(root,text="LD",padx=1, pady=1,command=LD_IXR1)
IXR2_LD = Button(root,text="LD",padx=1, pady=1,command=LD_IXR2)
IXR3_LD = Button(root,text="LD",padx=1, pady=1,command=LD_IXR3)
    #PC LD Button
PC_LD = Button(root,text="LD",padx=1, pady=1,command=LD_PC)
    #MAR LD Button
MAR_LD = Button(root,text="LD",padx=1, pady=1, command=LD_MAR)
    #MBR_LD Button
MBR_LD = Button(root,text="LD",padx=1, pady=1, command = LD_MBR)
    #System Button == Sys Button
Store  = Button(frameOpBtn,text="Store",padx=1, pady=1,command=Store)
StorePlus = Button(frameOpBtn,text="St+",padx=1, pady=1,command=StorePlus)
Load = Button(frameOpBtn,text="Load",padx=1, pady=1, command = Load)
Init = Button(frameOpBtn,text="Init",padx=1, pady=1, bg="red", fg="white", command=ClickInit)
SS = Button(frameSysBtn,text="SS",padx=10, pady=15, command=SS)
RunBtn = Button(frameSysBtn,text="Run",padx=10, pady=15,command=run_instructions)



#grid, it is the layout of the whole panel made by Zihao Wen

    #Label
GPR0Label.grid(row=0,column=0)
GPR1Label.grid(row=1,column=0)
GPR2Label.grid(row=2,column=0)
GPR3Label.grid(row=3,column=0)
SpaceGPRIXR.grid(row=4,column=0)
IXR1Label.grid(row=5,column=0)
IXR2Label.grid(row=6,column=0)
IXR3Label.grid(row=7,column=0)
SpaceIXROperation.grid(row=8,column=0)

SpaceGPRPC.grid(row=0,column=4)
PCLabel.grid(row=0,column=5)
MARLabel.grid(row=1,column=5)
MBRLabel.grid(row=2,column=5)
IRLabel.grid(row=3,column=5)
MFRLabel.grid(row=4,column=5)
PrivailegedLabel.grid(row=5,column=5)
    #Entry
GPR0.grid(row=0,column=1)
GPR1.grid(row=1,column=1)
GPR2.grid(row=2,column=1)
GPR3.grid(row=3,column=1)

IXR1.grid(row=5,column=1)
IXR2.grid(row=6,column=1)
IXR3.grid(row=7,column=1)

    #Right panel
PC.grid(row=0,column=6)
MAR.grid(row=1,column=6)
MBR.grid(row=2,column=6)
IR.grid(row=3,column=6)
MFR.grid(row=4,column=6)
Privaileged.grid(row=5,column=6)
HaltLabel.grid(row=1,column=4,rowspan=5)
RunLabel.grid(row=1,column=5,rowspan=5)
HaltLight.grid(row=2,column=4)
RunLight.grid(row=2,column=5)

    #Button
Btn15.grid(row=14,column=0)
Btn14.grid(row=14,column=1)
Btn13.grid(row=14,column=2)
Btn12.grid(row=14,column=3)
Btn11.grid(row=14,column=4)
Btn10.grid(row=14,column=5)
Btn9.grid(row=14,column=6)
Btn8.grid(row=14,column=7)
Btn7.grid(row=14,column=8)
Btn6.grid(row=14,column=9)
Btn5.grid(row=14,column=10)
Btn4.grid(row=14,column=11)
Btn3.grid(row=14,column=12)
Btn2.grid(row=14,column=13)
Btn1.grid(row=14,column=14)
Btn0.grid(row=14,column=15)
    # LD button
GPR0_LD.grid(row=0,column=3)
GPR1_LD.grid(row=1,column=3)
GPR2_LD.grid(row=2,column=3)
GPR3_LD.grid(row=3,column=3)
SpaceGPRIXR.grid(row=4,column=0)
IXR1_LD.grid(row=5,column=3)
IXR2_LD.grid(row=6,column=3)
IXR3_LD.grid(row=7,column=3)

PC_LD.grid(row=0,column=7)
MAR_LD.grid(row=1,column=7)
MBR_LD.grid(row=2,column=7)

    #system Button grid
Store.grid(row=7,column=7)
StorePlus.grid(row=7,column=8)
Load.grid(row=7,column=9)
Init.grid(row=7,column=10)
SS.grid(row=1,column=0)
SpaceSSRUN.grid(row=1,column=2)
RunBtn.grid(row=1,column=3)

    #Button status
Status15.grid(row=15,column=0)
Status14.grid(row=15,column=1)
Status13.grid(row=15,column=2)
Status12.grid(row=15,column=3)
Status11.grid(row=15,column=4)
Status10.grid(row=15,column=5)
Status9.grid(row=15,column=6)
Status8.grid(row=15,column=7)
Status7.grid(row=15,column=8)
Status6.grid(row=15,column=9)
Status5.grid(row=15,column=10)
Status4.grid(row=15,column=11)
Status3.grid(row=15,column=12)
Status2.grid(row=15,column=13)
Status1.grid(row=15,column=14)
Status0.grid(row=15,column=15)






root.mainloop()
