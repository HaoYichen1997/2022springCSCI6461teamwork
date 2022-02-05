import register as reg
import copy

#from main import *

import time
#inital memory and registers
memory = [0] * 2048
for address in range(2048):
    memory[address] = [0] * 16

#list[2048]
#  mem[0]= [0,0,0,0,0,0,0,0,0,0,0]    list[16]
SIXTEENBIT = [0] * 16
TWELVEBIT = [0] * 12
gpr0 = reg.Gpr(SIXTEENBIT)
gpr1 = reg.Gpr(SIXTEENBIT)
gpr2 = reg.Gpr(SIXTEENBIT)
gpr3 = reg.Gpr(SIXTEENBIT)
ixr1 = reg.Ixr(SIXTEENBIT)
ixr2 = reg.Ixr(SIXTEENBIT)
ixr3 = reg.Ixr(SIXTEENBIT)
mbr = reg.Mbr(SIXTEENBIT)
mar = reg.Mar(TWELVEBIT)
pc = reg.Pc(TWELVEBIT)
ir = reg.Ir(SIXTEENBIT)
#import main
'''
def show_Panel(register: reg.register, panel_textbox):
    panel_textbox.insert(str(register.num))
'''
def read_Mem_to_Mbr (mar:reg.Mar, mbr:reg.Mbr): #use mar mbr read mem
    address_bin = ''.join(str(i) for i in mar.num)
    address_dec = int(address_bin, 2)
    mbr.set(memory[address_dec])

def str_Mbr_to_Mem (ar:reg.Mar, mbr:reg.Mbr): #put mbr to mem address
    address_bin = ''.join(str(i) for i in mar.num)
    address_dec = int(address_bin, 2)
    memory[address_dec] = mbr.num

def fetch(pcaddress): #take instruction from mem to ir
    fetch_result = list()

    mar.set(pcaddress)
    fetch_result.append("mar")
    fetch_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    fetch_result.append("mbr")
    fetch_result.append(mbr.num)

    # 是否只有指令才能放到ir中，那fetch(EA)之类的是不需要ir？
    ir.set(mbr.num)
    fetch_result.append("ir")
    fetch_result.append(ir.num)
    return fetch_result

def cal_EA(instruction :list[16]):  #calculate EA
    #EA is Effective Address not a const
    #EA应该是个12位数以放进MAR，但IXR是16位，最终得出EA也是16位
    EA_result = list()
    if instruction[8] == 0 and instruction[9] == 0:
        EA = [0]*11 + instruction[-5:]
    elif instruction[8] == 0 and instruction[9] == 1:
        EA = [0]*16
        a = [0] * 11 + instruction[-5:]
        b = ixr1.num
        for i in range(16):
            EA[i] = a[i]+b[i]
    elif instruction[8] == 1 and instruction[9] == 0:
        EA = [0]*16
        a = [0] * 11 + instruction[-5:]
        b = ixr2.num
        for i in range(16):
            EA[i] = a[i]+b[i]
    elif instruction[8] == 1 and instruction[9] == 1:
        EA = [0]*16
        a = [0] * 11 + instruction[-5:]
        b = ixr3.num
        for i in range(16):
            EA[i] = a[i]+b[i]

    if instruction[10] == 1:
        result = fetch(EA)
        EA_result = copy.deepcopy(result)
        EA = copy.deepcopy(mbr.num)
    EA_result.append(EA)
    return EA_result

def ldr001(instruction):  #result is the list of regs num to panel
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0: #indirect EA use fetch
        del EA_result[-2:]  #delete the "ir" and ir.num in fetch_result
    ldr001_result = copy.deepcopy(EA_result)

    address = EA[-12:]  #to 12 bits for MAR
    mar.set(address)
    ldr001_result.append("mar")
    ldr001_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    ldr001_result.append("mbr")
    ldr001_result.append(mbr.num)

    if instruction[6] == 0 and instruction[7] == 0:
        gpr0.set(mbr.num)
        ldr001_result.append("gpr0")
        ldr001_result.append(gpr0.num)
    elif instruction[6] == 0 and instruction[7] == 1:
        gpr1.set(mbr.num)
        ldr001_result.append("gpr1")
        ldr001_result.append(gpr1.num)
    elif instruction[6] == 1 and instruction[7] == 0:
        gpr2.set(mbr.num)
        ldr001_result.append("gpr2")
        ldr001_result.append(gpr2.num)
    elif instruction[6] == 1 and instruction[7] == 1:
        gpr3.set(mbr.num)
        ldr001_result.append("gpr3")
        ldr001_result.append(gpr3.num)
    return  ldr001_result

def lda003(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0: #indirect EA use fetch
        del EA_result[-2:]  #delete the "ir" and ir.num in fetch_result
    lda003_result = copy.deepcopy(EA_result)
    if instruction[6] == 0 and instruction[7] == 0:
        gpr0.set(EA)
        lda003_result.append("gpr0")
        lda003_result.append(gpr0.num)
    elif instruction[6] == 0 and instruction[7] == 1:
        gpr1.set(EA)
        lda003_result.append("gpr1")
        lda003_result.append(gpr1.num)
    elif instruction[6] == 1 and instruction[7] == 0:
        gpr2.set(EA)
        lda003_result.append("gpr2")
        lda003_result.append(gpr2.num)
    elif instruction[6] == 1 and instruction[7] == 1:
        gpr3.set(EA)
        lda003_result.append("gpr3")
        lda003_result.append(gpr3.num)

    return lda003_result

def ldx041(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:
        del EA_result[-2:]
    ldx041_result = copy.deepcopy(EA_result)

    address = EA[-12:]
    mar.set(address)
    ldx041_result.append("mar")
    ldx041_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    ldx041_result.append("mbr")
    ldx041_result.append(mbr.num)

    if instruction[8] == 0 and instruction[9] == 0:
        print("IXR is 0!")

    elif instruction[8] == 0 and instruction[9] == 1:
        ixr1.set(mbr.num)
        ldx041_result.append("ixr1")
        ldx041_result.append(ixr1.num)

    elif instruction[8] == 1 and instruction[9] == 0:
        ixr2.set(mbr.num)
        ldx041_result.append("ixr2")
        ldx041_result.append(ixr2.num)

    elif instruction[8] == 1 and instruction[9] == 1:
        ixr3.set(mbr.num)
        ldx041_result.append("ixr3")
        ldx041_result.append(ixr3.num)

    return ldx041_result

def str002(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result
    str002_result = copy.deepcopy(EA_result)

    address = EA[-12:]  # to 12 bits for MAR
    mar.set(address)
    str002_result.append("mar")
    str002_result.append(mar.num)



    if instruction[6] == 0 and instruction[7] == 0:
        mbr.set(gpr0.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == 0 and instruction[7] == 1:
        mbr.set(gpr1.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == 1 and instruction[7] == 0:
        mbr.set(gpr2.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == 1 and instruction[7] == 1:
        mbr.set(gpr3.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    return str002_result

def stx042(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:
        del EA_result[-2:]
    stx042_result = copy.deepcopy(EA_result)

    address = EA[-12:]
    mar.set(address)
    print(address)
    stx042_result.append("mar")
    stx042_result.append(mar.num)


    if instruction[8] == 0 and instruction[9] == 0:
        print("IXR is 0!")

    elif instruction[8] == 0 and instruction[9] == 1:
        mbr.set(ixr1.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    elif instruction[8] == 1 and instruction[9] == 0:
        mbr.set(ixr2.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    elif instruction[8] == 1 and instruction[9] == 1:
        mbr.set(ixr3.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    return stx042_result

def halt000():
    halt000_result = list()
    halt000_result.append("halt")
    halt000_result.append([0]*16)
    return halt000_result


