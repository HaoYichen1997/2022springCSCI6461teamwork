"""

Creater:Zack
Date:01/21/2022

"""
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = Tk()
root.title("6461 Project1")
root.geometry("1130x450")
#Btn Frame

frameBtn =  LabelFrame(root, text="Num Button")
frameBtn.grid(row=9,column=1,columnspan=5,padx=50, pady=10)

frameOpBtn =  LabelFrame(root, text="Op Button")
frameOpBtn.grid(row=8,column=6,columnspan=1,padx=50, pady=10)

frameSysBtn =  LabelFrame(root, text="Sys Button")
frameSysBtn.grid(row=9,column=6,columnspan=1,padx=50, pady=10)


#Label of the panel
GPR0Label = Label(root, text="GRP 0(16bits)")
GPR1Label = Label(root, text="GRP 1(16bits)")
GPR2Label = Label(root, text="GRP 2(16bits)")
GPR3Label = Label(root, text="GRP 3(16bits)")

SpaceGPRIXR = Label(root, text=" ")

IXR1Label = Label(root, text="IXR1(16bits)")
IXR2Label = Label(root, text="IXR2(16bits)")
IXR3Label = Label(root, text="IXR3(16bits)")

SpaceIXROperation = Label(root, text=" ")
SpaceGPRPC = Label(root, text=" ")

PCLabel = Label(root, text="PC(12bits)")
MARLabel = Label(root, text="MAR(12bits)")
MBRLabel = Label(root, text="MBR(16bits)")
IRLabel = Label(root, text="IR(16bits)")
MFRLabel = Label(root, text="MFR(4bits)")
PrivailegedLabel = Label(root, text="Privaileged(1bits)")

SpaceSSRUN = Label(frameSysBtn, text="          ")
HaltLabel =Label(frameSysBtn, text="Halt")
RunLabel =Label(frameSysBtn, text="Run")
#Textbox(light)

# GPR0 = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# GPR0Value=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# for i in range(len(GPR0)) :
#     GPR0[i] = Entry(root, width=1, borderwidth=3)
#     GPR0[i].insert(0, "" + str(GPR0Value[i]))
#     GPR0[i].grid(row=0, column=i+1)

GPR0 = Entry(root, width=60, borderwidth=5,)
GPR1 = Entry(root, width=60, borderwidth=5)
GPR2 = Entry(root, width=60, borderwidth=5)
GPR3 = Entry(root, width=60, borderwidth=5)
IXR3 = Entry(root, width=60, borderwidth=5)
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

# GPR1 = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# GPR1Value=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# for i in range(len(GPR1)) :
#     GPR1[i] = Entry(root, width=1, borderwidth=3)
#     GPR1[i].insert(0, "" + str(GPR1Value[i]))
#     GPR1[i].grid(row=1, column=i+1)
#
# GPR2 = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# GPR2Value=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
# for i in range(len(GPR2)) :
#     GPR2[i] = Entry(root, width=1, borderwidth=3)
#     GPR2[i].insert(0, "" + str(GPR2Value[i]))
#     GPR2[i].grid(row=2, column=i+1)




# GPR01 =Entry(root, width=3, borderwidth=3)
# GPR01.insert(0,"0")

# GPR11 =Entry(root, width=3, borderwidth=3)
# GPR11.insert(0,"0")
#
# GPR21 =Entry(root, width=3, borderwidth=3)
# GPR21.insert(0,"0")
#
# GPR31 =Entry(root, width=3, borderwidth=3)
# GPR31.insert(0,"0")

# IXR11 = Entry(root, width=3, borderwidth=3)
# IXR11.insert(0,"0")
#
# IXR21 = Entry(root, width=3, borderwidth=3)
# IXR21.insert(0,"0")
#
# IXR31 = Entry(root, width=3, borderwidth=3)
# IXR31.insert(0,"0")


#Btn Click Function
# def Click15():
#     Label15 = Label(root, text="15 has been clicked", bg="yellow")
#     Label15.grid(row=15,column=0)
#define intial value
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




# frameOperation =  LabelFrame(root, text="Operation")
# frameOperation.grid(row=14,column=0,columnspan=1,padx=50, pady=10)
# frameGPR =  LabelFrame(root, text="GPR")
# frameGPR.grid(row=14,column=1,columnspan=1,padx=50, pady=10)
# frameIXR =  LabelFrame(root, text="IXR")
# frameIXR.grid(row=14,column=2,columnspan=1,padx=50, pady=10)
# frameI =  LabelFrame(root, text="I")
# frameI.grid(row=14,column=3,columnspan=1,padx=50, pady=10)
# frameAddress =  LabelFrame(root, text="Address")
# frameAddress.grid(row=14,column=4,columnspan=1,padx=50, pady=10)

#Btn Status
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
#Click number BTN modification
def Click15():
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

#Click LD BTN modification
def LD_GPR0():
    return
def LD_GPR1():
    return
def LD_GPR2():
    return
def LD_GPR3():
    return
def LD_IXR1():
    return
def LD_IXR2():
    return
def LD_IXR3():
    return
def LD_PC():
    return
def LD_MAR():
    return
def LD_MBR():
    return


#Btn
    #Button
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
    #GPR Loading
GPR0_LD = Button(root,text="LD",padx=1, pady=1)
GPR1_LD = Button(root,text="LD",padx=1, pady=1)
GPR2_LD = Button(root,text="LD",padx=1, pady=1)
GPR3_LD = Button(root,text="LD",padx=1, pady=1)
    #IXR Loading
IXR1_LD = Button(root,text="LD",padx=1, pady=1)
IXR2_LD = Button(root,text="LD",padx=1, pady=1)
IXR3_LD = Button(root,text="LD",padx=1, pady=1)
    #PC Loading
PC_LD = Button(root,text="LD",padx=1, pady=1)
    #MAR Loading
MAR_LD = Button(root,text="LD",padx=1, pady=1)
    #MBR_Loading
MBR_LD = Button(root,text="LD",padx=1, pady=1)
    #System Button
Store  = Button(frameOpBtn,text="Store",padx=1, pady=1)
StorePlus = Button(frameOpBtn,text="St+",padx=1, pady=1)
Load = Button(frameOpBtn,text="Load",padx=1, pady=1)
Init = Button(frameOpBtn,text="Init",padx=1, pady=1, bg="red", fg="white")
SS = Button(frameSysBtn,text="SS",padx=10, pady=15)
RunBtn = Button(frameSysBtn,text="Run",padx=10, pady=15)

# #canvas size
# canvas = tk.Canvas(root, width=600, height=300, bg="#20bebe")
# canvas.grid(columnspan=3)

# #logo
# logo = Image.open('touxiang.jpg')
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1,row=0)
#
# #instructions
# instructions = tk.Label(root, text="Select a PDF file", font="Raleway")
# instructions.grid(columnspan=3, column=0, row=1)
#
# def open_file():
#     browse_text.set("loading")
#     file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf File","*.pdf")])
#     if file:
#         read_pdf = PyPDF2.PdfFileReader(file)
#         page = read_pdf.getPage(0)
#         page_content = page.extractText()
#         #text_box
#         text_box = tk.Text(root, height=10, width=50, pady=15)
#         text_box.insert(1.0,page_content)
#         text_box.tag_configure("center", justify="center")
#         text_box.tag_add("center", 1.0, "end")
#         text_box.grid(column=1, row=3)
#
# #browse_button
# browse_text = tk.StringVar()
# browse_btn= tk.Button(root, textvariable=browse_text, command=lambda:open_file(),font="Raleway",bg="#20bebe", fg="white", height=2, width=15)
# browse_text.set("Browse")
# browse_btn.grid(column=1,row=2)
#
# canvas = tk.Canvas(root, width=600, height=300, bg="#20bebe")
# canvas.grid(columnspan=3)
#
# root.wm_title("6461 Team Project")


#grid

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
# GPR01.grid(row=0,column=1)
# GPR11.grid(row=1,column=1)
# GPR21.grid(row=2,column=1)
# GPR31.grid(row=3,column=1)
# IXR11.grid(row=5,column=1)
# IXR21.grid(row=6,column=1)
# IXR31.grid(row=7,column=1)
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
    # loading button
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

# Btn10.grid(row=14,column=5)
# Btn9.grid(row=14,column=6)
# Btn8.grid(row=14,column=7)
# Btn7.grid(row=14,column=8)
# Btn6.grid(row=14,column=9)
# Btn5.grid(row=14,column=10)
# Btn4.grid(row=14,column=11)
# Btn3.grid(row=14,column=12)
# Btn2.grid(row=14,column=13)
# Btn1.grid(row=14,column=14)
# Btn0.grid(row=14,column=15)


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
