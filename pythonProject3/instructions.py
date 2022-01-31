from register import *
import time
#inital memory and registers
memory = [0] * 2048
for address in range(2048):
    memory[address] = [0] * 16

SIXTEENBIT = [0] * 16
TWELVEBIT = [0] * 12
gpr0 = Gpr(SIXTEENBIT)
gpr1 = Gpr(SIXTEENBIT)
gpr2 = Gpr(SIXTEENBIT)
gpr3 = Gpr(SIXTEENBIT)
ixr1 = Ixr(SIXTEENBIT)
ixr2 = Ixr(SIXTEENBIT)
ixr3 = Ixr(SIXTEENBIT)
mbr = Mbr(SIXTEENBIT)
mar = Mar(TWELVEBIT)
pc = Pc(TWELVEBIT)
ir = Ir(SIXTEENBIT)


def read_Mem_to_Mbr (mar:Mar, mbr:Mbr):
    address_bin = ''.join(str(i) for i in mar.num)
    address_dec = int(address_bin, 2)
    mbr.set(memory[address_dec])


def fetch(pcaddress):
    mar.set(pcaddress)
    print(f"mar is {mar.num}")#mar.showpanel
    time.sleep(1)

    read_Mem_to_Mbr(mar, mbr)
    print(f"mbr is {mbr.num}")#mbr.showpanel
    time.sleep(1)

    # 是否只有指令才能放到ir中，那fetch(EA)之类的是不需要ir？
    ir.set(mbr.num)
    print(f"ir is {ir.num}")#ir.showpanel
    time.sleep(1)


def cal_EA(instruction :list[16]):
    #EA is Effective Address not a const
    #EA应该是个12位数以放进MAR，但IXR是16位，最终得出EA也是16位
    if instruction[8] == 0 and instruction[9] == 0:
        EA = [0]*11+instruction[-5:]
    elif instruction[8] == 0 and instruction[9] == 1:
        EA = list()
        a = [0] * 11 + instruction[-5:]
        b = ixr1.num
        for i in range(16):
            EA[i] = a[i]+b[i]
    elif instruction[8] == 1 and instruction[9] == 0:
        EA = list()
        a = [0] * 11 + instruction[-5:]
        b = ixr2.num
        for i in range(16):
            EA[i] = a[i]+b[i]
    elif instruction[8] == 1 and instruction[9] == 1:
        EA = list()
        a = [0] * 11 + instruction[-5:]
        b = ixr3.num
        for i in range(16):
            EA[i] = a[i]+b[i]

    if instruction[10] == 1:
        EA=fetch(EA)

    return EA
    #print(EA)

def ldr001(instruction):
    EA = cal_EA(instruction)
    address = EA[-12:]  #to 12 bits for MAR
    mar.set(address)
    #show_panel
    read_Mem_to_Mbr(mar, mbr)
    #mbr.show_panel
    if instruction[6] == 0 and instruction[7] == 0:
        gpr0.set(mbr.num)
        print(gpr0.num) #gpr0.show_panel
    elif instruction[6] == 0 and instruction[7] == 1:
        gpr1.set(mbr.num)
        print(gpr1.num)  # gpr1.show_panel
    elif instruction[6] == 1 and instruction[7] == 0:
        gpr2.set(mbr.num)
        print(gpr2.num)  # gpr2.show_panel
    elif instruction[6] == 1 and instruction[7] == 1:
        gpr3.set(mbr.num)
        print(gpr3.num)  # gpr3.show_panel

def lda003(instruction):
    EA = cal_EA(instruction)
    if instruction[6] == 0 and instruction[7] == 0:
        gpr0.set(EA)
        print(gpr0.num)  # gpr0.show_panel
    elif instruction[6] == 0 and instruction[7] == 1:
        gpr1.set(EA)
        print(gpr1.num)  # gpr1.show_panel
    elif instruction[6] == 1 and instruction[7] == 0:
        gpr2.set(EA)
        print(gpr2.num)  # gpr2.show_panel
    elif instruction[6] == 1 and instruction[7] == 1:
        gpr3.set(EA)
        print(gpr3.num)  # gpr3.show_panel

def ldx041(instruction):
    EA = cal_EA(instruction)
    address = EA[-12:]  #to 12 bits for MAR
    mar.set(address)
    #show_panel
    read_Mem_to_Mbr(mar, mbr)
    #mbr.show_panel
    if instruction[8] == 0 and instruction[9] == 0:
        print("IXR is 0!")
    elif instruction[8] == 0 and instruction[9] == 1:
        ixr1.set(mbr.num)
        print(ixr1.num)  # ixr1.show_panel
    elif instruction[8] == 1 and instruction[9] == 0:
        ixr2.set(mbr.num)
        print(ixr2.num)  # ixr2.show_panel
    elif instruction[8] == 1 and instruction[9] == 1:
        ixr3.set(mbr.num)
        print(ixr3.num)  # ixr3.show_panel

#def str
instruction=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

cal_EA(instruction)