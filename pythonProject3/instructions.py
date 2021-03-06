import struct

import register as reg
import copy
import time
from tkinter import *
import Program1 as pg1
import Cache
from struct import *

'''
this module about the 16-bit instructions 
and other instructions about memory
'''

# inital memory and registers
memory = [0] * 2048
for address in range(2048):
    memory[address] = ['0'] * 16
# ZERO_16 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"].
'''
buffers of IN instruction
'''
console_keyboard_buffer = list()

# [[0],[1]]
# e.p. memory=list[2048]
#  mem[0]= ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']    list[16].
SIXTEENBIT = ['0'] * 16
TWELVEBIT = ['0'] * 12
FOURBIT = ['0'] * 4
gpr0 = reg.Gpr(SIXTEENBIT, "gpr0")
gpr1 = reg.Gpr(SIXTEENBIT, "gpr1")
gpr2 = reg.Gpr(SIXTEENBIT, "gpr2")
gpr3 = reg.Gpr(SIXTEENBIT, "gpr3")
ixr1 = reg.Ixr(SIXTEENBIT, "ixr1")
ixr2 = reg.Ixr(SIXTEENBIT, "ixr2")
ixr3 = reg.Ixr(SIXTEENBIT, "ixr3")
mbr = reg.Mbr(SIXTEENBIT, "mbr")
mar = reg.Mar(TWELVEBIT)
pc = reg.Pc(TWELVEBIT)
ir = reg.Ir(SIXTEENBIT, "ir")
cc = reg.Cc(FOURBIT)
fr0 = reg.fr(SIXTEENBIT, "fr0")
fr1 = reg.fr(SIXTEENBIT, "fr1")


def read_Mem_to_Mbr(mar: reg.Mar, mbr: reg.Mbr):  # use mar mbr read mem
    address_bin = ''.join(i for i in mar.num)
    address_dec = int(address_bin, 2)
    mbr.set(Cache.read_cache(address_dec))
    # Cache.add_to_cache(address_dec)
    mbr.set(memory[address_dec])


def str_Mbr_to_Mem(mar: reg.Mar, mbr: reg.Mbr):  # put mbr to mem address
    address_bin = ''.join(i for i in mar.num)
    address_dec = int(address_bin, 2)
    Cache.write_reg_to_c_m(address_dec, mbr.num)
    # Cache.add_to_cache(address_dec)
    memory[address_dec] = mbr.num


def fetch(pcaddress):  # take instruction from mem to ir
    fetch_result = list()

    mar.set(pcaddress)
    fetch_result.append("mar")
    fetch_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    fetch_result.append("mbr")
    fetch_result.append(mbr.num)

    ir.set(mbr.num)
    fetch_result.append("ir")
    fetch_result.append(ir.num)
    return fetch_result


def cal_ldx_EA(instruction: []):
    # in ldx EA do not count number already in ixr
    EA_result = list()  # for return if needed
    EA = ['0'] * 11 + instruction[-5:]

    if instruction[10] == "1":
        result = fetch(EA)
        EA_result = copy.deepcopy(result)
        EA = copy.deepcopy(mbr.num)
    EA_result.append(EA)
    return EA_result


def cal_EA(instruction: []):  # calculate EA
    # EA is Effective Address not a const
    # EA should be a 12 digit number to fit in MAR, but IXR is 16 bits, So EA is 16 bits
    # if EA is indirect, we need update mar,mbr once time, I return these num as a list
    EA_result = list()  # for return if needed
    if instruction[8] == "0" and instruction[9] == '0':  # find the ixr number
        EA = ['0'] * 11 + instruction[-5:]
    elif instruction[8] == '0' and instruction[9] == '1':
        a = ['0'] * 11 + instruction[-5:]
        b = ixr1.num
        # binary plus for ixr and address
        a_bin = ''.join(i for i in a)
        a_dec = int(a_bin, 2)
        b_bin = ''.join(i for i in b)
        b_dec = int(b_bin, 2)
        c = a_dec + b_dec
        data = bin(c)[2:].zfill(16)
        EA = [num for num in str(data)]
        print("CAL_EA,01EA:", EA)
    elif instruction[8] == '1' and instruction[9] == '0':
        EA = ['0'] * 16
        a = ['0'] * 11 + instruction[-5:]
        b = ixr2.num
        a_bin = ''.join(i for i in a)
        a_dec = int(a_bin, 2)
        b_bin = ''.join(i for i in b)
        b_dec = int(b_bin, 2)
        c = a_dec + b_dec
        data = bin(c)[2:].zfill(16)
        EA = [num for num in str(data)]
    elif instruction[8] == "1" and instruction[9] == "1":
        EA = ["0"] * 16
        a = ["0"] * 11 + instruction[-5:]
        b = ixr3.num
        a_bin = ''.join(i for i in a)
        a_dec = int(a_bin, 2)
        b_bin = ''.join(i for i in b)
        b_dec = int(b_bin, 2)
        c = a_dec + b_dec
        data = bin(c)[2:].zfill(16)
        EA = [num for num in str(data)]

    if instruction[10] == "1":
        result = fetch(EA)
        EA_result = copy.deepcopy(result)
        EA = copy.deepcopy(mbr.num)
    EA_result.append(EA)
    return EA_result


def ldr001(instruction):  # load from mem to gpr
    # result is the list of regs num to panel
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result
    ldr001_result = copy.deepcopy(EA_result)

    address = EA[-12:]  # to 12 bits for MAR
    mar.set(address)
    ldr001_result.append("mar")
    ldr001_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    ldr001_result.append("mbr")
    ldr001_result.append(mbr.num)

    if instruction[6] == "0" and instruction[7] == "0":
        gpr0.set(mbr.num)
        ldr001_result.append("gpr0")
        ldr001_result.append(gpr0.num)
    elif instruction[6] == "0" and instruction[7] == "1":
        gpr1.set(mbr.num)
        ldr001_result.append("gpr1")
        ldr001_result.append(gpr1.num)
    elif instruction[6] == "1" and instruction[7] == "0":
        gpr2.set(mbr.num)
        ldr001_result.append("gpr2")
        ldr001_result.append(gpr2.num)
    elif instruction[6] == "1" and instruction[7] == "1":
        gpr3.set(mbr.num)
        ldr001_result.append("gpr3")
        ldr001_result.append(gpr3.num)
    return ldr001_result


def lda003(instruction):  # load address to gpr
    EA = ['0'] * 11 + instruction[-5:]
    lda003_result = list()
    if instruction[6] == "0" and instruction[7] == "0":
        gpr0.set(EA)
        lda003_result.append("gpr0")
        lda003_result.append(gpr0.num)
    elif instruction[6] == "0" and instruction[7] == "1":
        gpr1.set(EA)
        lda003_result.append("gpr1")
        lda003_result.append(gpr1.num)
    elif instruction[6] == "1" and instruction[7] == "0":
        gpr2.set(EA)
        lda003_result.append("gpr2")
        lda003_result.append(gpr2.num)
    elif instruction[6] == "1" and instruction[7] == "1":
        gpr3.set(EA)
        lda003_result.append("gpr3")
        lda003_result.append(gpr3.num)
    return lda003_result


def ldx041(instruction):  # load from mem to ixr
    EA_result = cal_ldx_EA(instruction)
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

    if instruction[8] == "0" and instruction[9] == "0":
        print("IXR is 0!")

    elif instruction[8] == "0" and instruction[9] == "1":
        ixr1.set(mbr.num)
        ldx041_result.append("ixr1")
        ldx041_result.append(ixr1.num)

    elif instruction[8] == "1" and instruction[9] == "0":
        ixr2.set(mbr.num)
        ldx041_result.append("ixr2")
        ldx041_result.append(ixr2.num)

    elif instruction[8] == "1" and instruction[9] == "1":
        ixr3.set(mbr.num)
        ldx041_result.append("ixr3")
        ldx041_result.append(ixr3.num)

    return ldx041_result


def str002(instruction):  # store from gpr to mem
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:
        del EA_result[-2:]
    str002_result = copy.deepcopy(EA_result)

    address = EA[-12:]
    mar.set(address)
    str002_result.append("mar")
    str002_result.append(mar.num)

    if instruction[6] == "0" and instruction[7] == "0":
        mbr.set(gpr0.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == "0" and instruction[7] == "1":
        mbr.set(gpr1.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == "1" and instruction[7] == "0":
        mbr.set(gpr2.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == "1" and instruction[7] == "1":
        mbr.set(gpr3.num)
        str002_result.append("mbr")
        str002_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    return str002_result


def stx042(instruction):  # store from ixr to mem
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

    if instruction[8] == "0" and instruction[9] == "0":
        print("IXR is 0!")

    elif instruction[8] == "0" and instruction[9] == "1":
        mbr.set(ixr1.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    elif instruction[8] == "1" and instruction[9] == "0":
        mbr.set(ixr2.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    elif instruction[8] == "1" and instruction[9] == "1":
        mbr.set(ixr3.num)
        stx042_result.append("mbr")
        stx042_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)

    return stx042_result


def halt000():  # halt
    halt000_result = list()
    halt000_result.append("halt")
    halt000_result.append(["0"] * 16)
    return halt000_result


'''
'''


def mlt020(instruction):
    mlt020_result = list()
    rx, ry = -1, -1
    operand1 = list()
    operand2 = list()
    if instruction[6] == "0" and instruction[7] == "0":
        rx = 0
        operand1.append(gpr0.num)
    if instruction[6] == "1" and instruction[7] == "0":
        rx = 2
        operand1.append(gpr2.num)
    if instruction[8] == "0" and instruction[9] == "0":
        ry = 0
        operand2.append(gpr0.num)
    if instruction[8] == "1" and instruction[9] == "0":
        ry = 2
        operand2.append(gpr2.num)
    if rx == -1 or ry == -1:
        print("wrong reg in mlt")
    else:
        a_bin = ''.join(i for i in operand1[0])
        a_dec = int(a_bin, 2)
        b_bin = ''.join(i for i in operand2[0])
        b_dec = int(b_bin, 2)
        c_dec = a_dec * b_dec
        result = bin(c_dec)[2:].zfill(32)
        high_bits = [num for num in str(result[:16])]
        low_bits = [num for num in str(result[16:])]
        if instruction[6] == "0" and instruction[7] == "0":
            gpr0.set(high_bits)
            mlt020_result.append("gpr0")
            mlt020_result.append(gpr0.num)
            gpr1.set(low_bits)
            mlt020_result.append("gpr1")
            mlt020_result.append(gpr1.num)

        if instruction[6] == "1" and instruction[7] == "0":
            gpr2.set(high_bits)
            mlt020_result.append("gpr0")
            mlt020_result.append(gpr0.num)
            gpr3.set(low_bits)
            mlt020_result.append("gpr1")
            mlt020_result.append(gpr1.num)

        if check_mul_overflew(c_dec):
            cc.set_overflow("1")
            mlt020_result.append('cc')
            mlt020_result.append('overflow_1')
            print("over flow in mlt020")

        return mlt020_result


def check_mul_overflew(num: int):  # dec multiple overflow is 2 **32
    # overflew underflew return true
    flag = False
    if num > 2 ** 32:
        print("overflew")
        flag = True
    elif num < -2 ** 32 - 1:
        print("underflew")
        flag = True
    return flag


def dvd021(instruction):
    dvd021_result = list()
    rx, ry = -1, -1
    operand1 = list()
    operand2 = list()
    if instruction[6] == "0" and instruction[7] == "0":
        rx = 0
        operand1.append(gpr0.num)
    if instruction[6] == "1" and instruction[7] == "0":
        rx = 2
        operand1.append(gpr2.num)
    if instruction[8] == "0" and instruction[9] == "0":
        ry = 0
        operand2.append(gpr0.num)
    if instruction[8] == "1" and instruction[9] == "0":
        ry = 2
        operand2.append(gpr2.num)
        print(gpr2.num)
    if rx == -1 or ry == -1:
        print("wrong reg in dvd021")
    else:
        a_bin = ''.join(i for i in operand1[0])
        a_dec = int(a_bin, 2)
        b_bin = ''.join(i for i in operand2[0])
        b_dec = int(b_bin, 2)
        print("a_dec:", a_dec, "b_dec", b_dec)
        c_dec = a_dec // b_dec
        d_dec = a_dec % b_dec
        quotient = bin(c_dec)[2:].zfill(16)
        remainder = bin(d_dec)[2:].zfill(16)

        quotient_list = list()
        remainder_list = list()
        for i in quotient:
            quotient_list.append(i)
        for i in remainder:
            remainder_list.append(i)
        print("quotientl:", quotient_list, "remaninl", remainder_list)
        if instruction[6] == "0" and instruction[7] == "0":
            gpr0.set(quotient_list)
            dvd021_result.append("gpr0")
            dvd021_result.append(gpr0.num)
            gpr1.set(remainder_list)
            dvd021_result.append("gpr1")
            dvd021_result.append(gpr1.num)

        if instruction[6] == "1" and instruction[7] == "0":
            gpr2.set(quotient_list)
            dvd021_result.append("gpr0")
            dvd021_result.append(gpr0.num)
            gpr3.set(remainder_list)
            dvd021_result.append("gpr1")
            dvd021_result.append(gpr1.num)

        if b_dec == 0:
            cc.set_div_zero("1")
            dvd021_result.append('cc')
            dvd021_result.append('div_zero_1')
            print("over flow in dvd021")

        return dvd021_result


def get_gpr_in_instr(instruction, num1: int, num2: int):  # num1,2 is digit like 6 7
    # use to find which gpr in instr's gpr area, 2 bits
    if instruction[num1] == "0" and instruction[num2] == "0":
        return gpr0
    elif instruction[num1] == "0" and instruction[num2] == "1":
        return gpr1
    elif instruction[num1] == "1" and instruction[num2] == "0":
        return gpr2
    elif instruction[num1] == "1" and instruction[num2] == "1":
        return gpr3


def trr022(instruction):
    trr022_result = list()
    rx = get_gpr_in_instr(instruction, 6, 7)
    ry = get_gpr_in_instr(instruction, 8, 9)

    equal = True
    for i in range(16):
        if rx.num[i] != ry.num[i]:
            equal = False

    if equal:
        cc.set_equal_or_not("1")
        trr022_result.append('cc')
        trr022_result.append('equal_or_not_1')
    else:
        cc.set_equal_or_not("0")
        trr022_result.append('cc')
        trr022_result.append('equal_or_not_0')

    return trr022_result


def and023(instruction):
    and023_result = list()
    rx = get_gpr_in_instr(instruction, 6, 7)
    ry = get_gpr_in_instr(instruction, 8, 9)

    for i in range(16):
        if rx.num[i] == "1" and ry.num == '1':
            rx.num[i] = "1"
        else:
            rx.num[i] = "0"

    and023_result.append(rx.name)
    and023_result.append(rx.num)
    return and023_result


def orr024(instruction):
    orr024_result = list()
    rx = get_gpr_in_instr(instruction, 6, 7)
    ry = get_gpr_in_instr(instruction, 8, 9)

    for i in range(16):
        if rx.num[i] == "1" or ry.num == '1':
            rx.num[i] = "1"
        else:
            rx.num[i] = "0"

    orr024_result.append(rx.name)
    orr024_result.append(rx.num)
    return orr024_result


def not025(instruction):
    not025_result = list()
    rx = get_gpr_in_instr(instruction, 6, 7)
    for i in range(16):
        if rx.num[i] == "1":
            rx.num[i] = "0"
        else:
            rx.num[i] = "1"
    not025_result.append(rx.name)
    not025_result.append(rx.num)
    return not025_result


def in061(instruction):
    global Consolekey  # ["100","w",] ["w","o","r","d"]
    # 90["w"ascii],91["o"ascii]  "1aw7"
    # assume is a list of char
    # number ascii from 48- 57
    # A-Z :65 -90  a-z:97-122  + -: 43 45
    r = get_gpr_in_instr(instruction, 6, 7)
    devid = instruction[-5:]
    a_bin = ''.join(i for i in devid)
    devid_dec = int(a_bin, 2)
    if devid_dec == 0:
        chr = Consolekey.pop(0)
        if chr.isdigit():
            num = chr
            result = bin(int(num))[2:].zfill(16)
            data = [num for num in str(result)]
            r.set(data)
            print("num", num)
        else:
            asc = ord(chr)
            result = bin(int(asc))[2:].zfill(16)
            data = [num for num in str(result)]
            r.set(data)
            print("asc:", asc, "data:", data)
    in061_result = list()
    in061_result.append(f"{r.name}")
    r_data = ''.join(i for i in r.num)
    in061_result.append(r_data)
    return in061_result


def chk063(instruction):
    global Consolekey
    r = get_gpr_in_instr(instruction, 6, 7)
    devid = instruction[-5:]
    a_bin = ''.join(i for i in devid)
    devid_dec = int(a_bin, 2)
    if devid_dec == 0:
        if Consolekey:
            r.set(['0'] * 15 + ["1"])
        else:
            r.set(['0'] * 16)
    chk063_result = list()
    chk063_result.append(f"{r.name}")
    r_data = ''.join(i for i in r.num)
    chk063_result.append(r_data)
    return chk063_result


'''
'''


def to_one_str(data: list):
    i = ''.join(data)
    return i


def float2bin32(num):
    ''' python float to 32bit bin
    :param num: a float num int is ok
    :return: a 32bit str like 0 01111111 10000000000000000000000
    '''
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)


def bin2float32(binary):
    '''  python 32bit bin to float
    :param binary: a 32 bit str
    :return: float
    '''
    return struct.unpack('!f', struct.pack('!I', int(binary, 2)))[0]


def turndecint(content: []):
    # if value is negative
    if content[0] == '1':
        return -int("".join(content[1:]), 2)
    int_cont = int("".join(content), 2)
    return int_cont


def int_to7bit(number: int):
    if number < 0:
        return '1' + str(bin(number)[3:].zfill(6))
    if number >= 0:
        return str(bin(number)[2:].zfill(7))


def convertfloat2bin16(value):
    '''
    :param value: float
    :return: str 16bit
    '''
    print("float2b16v:", value)
    bin32 = float2bin32(value)
    sign = bin32[0]
    expo32 = bin32[1:9]
    manti32 = bin32[9:]
    # print("sign:",sign,"exp32:",expo32,"ma32:",manti32)
    manti16 = manti32[0:8]
    expo_dec = int(expo32, 2) - 127
    if expo_dec < -63 or expo_dec > 64:
        print("float overflow or underflow in convertf2bin")
        # return
    expo16 = int_to7bit(expo_dec)
    float16 = sign + expo16 + manti16
    return float16


def convertbin16_tofloat(bin16):
    '''
    :param bin16: str
    :return: float
    '''
    sign = bin16[0]
    expo16 = to_one_str(bin16[1:8])
    manti16 = to_one_str(bin16[8:])

    # print("sign:", sign, "exp16:", expo16, "ma16:", manti16)
    manti32 = manti16 + "000000000000000"
    expo_dec = turndecint(expo16) + 127
    # print("expdec:", expo_dec)
    expo32 = bin(expo_dec)[2:].zfill(8)
    bin32 = sign + expo32 + manti32
    # print("sign:", sign, "exp32:", expo32, "ma32:", manti32)
    print("cb2float bin32:", bin32)
    fnum = bin2float32(bin32)
    print(fnum)
    return fnum


def convertbin16_tofixed(bin16):
    '''
    :param bin16: str
    :return: fixed point
    '''
    sign = bin16[0]
    manti16 = bin16[1:]
    fixed = 0
    times = 0.1  # config times set in here e.p. 0.01, 0.001
    # must same as the times in convertfixed2bin16
    if sign == '0':
        a_bin = ''.join(i for i in manti16)
        a_dec = int(a_bin, 2)
        fixed = a_dec * times
    elif sign == "1":
        a_bin = ''.join(i for i in manti16)
        a_dec = int(a_bin, 2)
        fixed = - a_dec * times
    else:
        print("conver fixed wrong")
    return fixed


def convertfixed2bin16(value):
    '''
    :param fixed
    :return: bin16
    '''
    times = 0.1
    if value >= 0:
        sign = "0"
    else:
        sign = "1"
    a = int(value / times)
    manti_bin = bin(a)[2:].zfill(15)
    fix16 = sign + manti_bin
    return fix16


# print(float2bin32(-14.888))  # 0 01111111 10000000000000000000000
# print(type(bin2float32("11000001011011100011010100111111")))
# print(covertfloat2bin16(-0.5))
# print("test")
# print(convertbin16_tofloat("0100001010011001"))
'''
'''


def cnvrt037(instruction):
    cnvrt037_result = list()
    r = get_gpr_in_instr(instruction, 6, 7)
    a_bin = ''.join(i for i in r.num)
    a_dec = int(a_bin, 2)
    if a_dec == 0:
        EA_result = cal_EA(instruction)
        EA = EA_result.pop()
        if len(EA_result) != 0:
            del EA_result[-2:]
        cnvrt037_result = copy.deepcopy(EA_result)
        print("cnvertEA", EA)
        num = convertbin16_tofloat(EA)
        fix16 = convertfixed2bin16(num)
        fix16_list = [num for num in fix16]
        print("fix16list:", fix16_list)
        r.set(fix16_list)
        cnvrt037_result.append(r.name)
        cnvrt037_result.append(r.num)
    elif a_dec == 1:
        EA_result = cal_EA(instruction)
        EA = EA_result.pop()
        if len(EA_result) != 0:
            del EA_result[-2:]
        cnvrt037_result = copy.deepcopy(EA_result)
        print("cnvert1EA", EA)
        num = convertbin16_tofixed(EA)
        print("cnvert1num", num)
        float16 = convertfloat2bin16(num)
        float16_list = [num for num in float16]
        print("float16_list:", float16_list)
        fr0.set(float16_list)
        cnvrt037_result.append("fr0")
        cnvrt037_result.append(fr0.num)
    else:
        print("F invalid")
    return cnvrt037_result


def ldfr050(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result
    ldfr050_result = copy.deepcopy(EA_result)

    address = EA[-12:]  # to 12 bits for MAR
    mar.set(address)
    ldfr050_result.append("mar")
    ldfr050_result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    ldfr050_result.append("mbr")
    ldfr050_result.append(mbr.num)
    print("050:", mbr.num)
    if instruction[6] == "0" and instruction[7] == "0":
        fr0.set(mbr.num)
        ldfr050_result.append("fr0")
        ldfr050_result.append(fr0.num)
    elif instruction[6] == "0" and instruction[7] == "1":
        fr1.set(mbr.num)
        ldfr050_result.append("fr1")
        ldfr050_result.append(fr1.num)
    else:
        print("ldfr wrong")
    return ldfr050_result


def stfr051(instruction):
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:
        del EA_result[-2:]
    stfr051_result = copy.deepcopy(EA_result)

    address = EA[-12:]
    mar.set(address)
    stfr051_result.append("mar")
    stfr051_result.append(mar.num)

    if instruction[6] == "0" and instruction[7] == "0":
        mbr.set(fr0.num)
        print("051fr0", fr0.num)
        stfr051_result.append("mbr")
        stfr051_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    elif instruction[6] == "0" and instruction[7] == "1":
        mbr.set(fr1.num)
        print("051fr1", fr1.num)
        stfr051_result.append("mbr")
        stfr051_result.append(mbr.num)
        str_Mbr_to_Mem(mar, mbr)
    else:
        print("stfr wrong")
    return stfr051_result


def jz010(instruction):  # Jump If Zero
    # result is the list of regs num to panel
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result   1
    JZ10_result = copy.deepcopy(EA_result)

    if (instruction[6] == "0" and instruction[7] == "0" and "".join(gpr0.num) == "0000000000000000") \
            or (instruction[6] == "0" and instruction[7] == "1" and "".join(gpr1.num) == "0000000000000000") \
            or (instruction[6] == "1" and instruction[7] == "0" and "".join(gpr2.num) == "0000000000000000") \
            or (instruction[6] == "1" and instruction[7] == "1" and "".join(gpr3.num) == "0000000000000000"):
        # main.PC.delete(0, END)
        # main.PC.insert(0,str(JZ10_result[0]))
        EA_PC_dec = int(to_one_str(EA), 2)
        EA_PC_bin = bin(EA_PC_dec)
        pc.set(EA_PC_bin[2:].zfill(12))
        JZ10_result.append("pc")
        JZ10_result.append(pc.num)
        print("JZ!PC:", EA_PC_dec)
    else:
        pc.set(pc.num)
        JZ10_result.append("pc")
        JZ10_result.append(pc.num)
        # main.PC.delete(0, END)
        # main.PC.insert(main.BinaryPlusOne(main.PC.get()))
    return JZ10_result


# This function add memory to register,opcode04
def amr(instruction):
    amr_result = get_data_from_memory(instruction)
    dest_reg = get_register(instruction)
    cont_reg = string_to_int(dest_reg.num)
    cont_EA = string_to_int(mbr.num)
    add_result = cont_EA + cont_reg
    if check_overflow_or_underflow(add_result):
        return []
    # add c(EA) AND C(r) to r
    dest_reg.set(int_to_string(add_result))
    print("cont_EA:", cont_EA, "cont_reg:", cont_reg, "reg_num:", dest_reg.num)
    amr_result.append(dest_reg.name)
    amr_result.append(dest_reg.num)
    return amr_result


def string_to_int(content: []):
    # if value is negative
    if content[0] == '1':
        return -int("".join(content[1:]), 2)
    int_cont = int("".join(content), 2)
    return int_cont


def int_to_string(number: int):
    if number < 0:
        return ['1'] + list(str(bin(number)[3:].zfill(15)))
    if number >= 0:
        return list(str(bin(number)[2:].zfill(16)))


# Return the register according to instruction
def get_register(instruction):
    if instruction[6] == "0" and instruction[7] == "0":
        return gpr0
    elif instruction[6] == "0" and instruction[7] == "1":
        return gpr1
    elif instruction[6] == "1" and instruction[7] == "0":
        return gpr2
    elif instruction[6] == "1" and instruction[7] == "1":
        return gpr3


def get_data_from_memory(instruction):
    # result is the list of regs num to panel
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result
    result = copy.deepcopy(EA_result)

    address = EA[-12:]
    mar.set(address)
    result.append("mar")
    result.append(mar.num)

    read_Mem_to_Mbr(mar, mbr)
    result.append("mbr")
    result.append(mbr.num)

    return result


# 05 Subtract Memory From Register
def smr(instruction):
    smr_result = get_data_from_memory(instruction)
    dest_reg = get_register(instruction)
    cont_reg = string_to_int(dest_reg.num)
    cont_EA = string_to_int(mbr.num)
    sub_result = cont_reg - cont_EA
    if check_overflow_or_underflow(sub_result):
        return []
    print("subre:", sub_result, "cont_reg:", cont_reg, "cont_EA", cont_EA)
    dest_reg.set(int_to_string(sub_result))

    smr_result.append(dest_reg.name)
    smr_result.append(dest_reg.num)
    return smr_result


# 06 Add  Immediate to Register
def air(instruction):
    immediate = int("".join(instruction[-5:]), 2)
    # if Immed = 0, does nothing
    if immediate == 0:
        return []
    dest_reg = get_register(instruction)
    cont_reg = string_to_int(dest_reg.num)

    # if c(r) = 0, loads r with Immed
    if cont_reg == 0:
        dest_reg.set(['0'] * 11 + instruction[-5:])

    else:
        add_result = cont_reg + immediate
        if check_overflow_or_underflow(add_result):
            return []
        dest_reg.set(int_to_string(add_result))
    air_result = [dest_reg.name, dest_reg.num]
    return air_result


def check_overflow_or_underflow(number):
    if number < -32767:
        print("Underflow!")
        return True
    if number > 32767:
        print("Overflow!")
        return True
    return False


# 07 Subtract  Immediate  from Register
def sir(instruction):
    immediate = int("".join(instruction[-5:]), 2)
    if immediate == 0:
        return []
    dest_reg = get_register(instruction)
    cont_reg = string_to_int(dest_reg.num)
    if cont_reg == 0:
        dest_reg.set(int_to_string(-immediate))
    else:
        sub_result = cont_reg - immediate
        if check_overflow_or_underflow(sub_result):
            return []
        dest_reg.num = int_to_string(sub_result)

    sir_result = [dest_reg.name, dest_reg.num]
    return sir_result


# ZERO_16 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
def jne011(instruction):  # Jump If not equal
    # result is the list of regs num to panel
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]  # delete the "ir" and ir.num in fetch_result
    JZ11_result = copy.deepcopy(EA_result)

    if (instruction[6] == "0" and instruction[7] == "0" and "".join(gpr0.num) != "0000000000000000") \
            or (instruction[6] == "0" and instruction[7] == "1" and "".join(gpr1.num) != "0000000000000000") \
            or (instruction[6] == "1" and instruction[7] == "0" and "".join(gpr2.num) != "0000000000000000") \
            or (instruction[6] == "1" and instruction[7] == "1" and "".join(gpr3.num) != "0000000000000000"):
        EA_PC_dec = int(to_one_str(EA), 2)
        EA_PC_bin = bin(EA_PC_dec)
        pc.set(EA_PC_bin[2:].zfill(12))
        print("JNE!PC:", EA_PC_dec)
        JZ11_result.append("pc")
        JZ11_result.append(pc.num)
    else:
        pc.set(pc.num)
        JZ11_result.append("pc")
        JZ11_result.append(pc.num)
    return JZ11_result


def jcc012(instruction):  # Jump if condition code
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    jcc012_result = copy.deepcopy(EA_result)

    if (instruction[6] == "0" and instruction[7] == "0" and cc[0] == '1') or \
            (instruction[6] == "0" and instruction[7] == "1" and cc[1] == '1') or \
            (instruction[6] == "1" and instruction[7] == "1" and cc[3] == '1') or \
            (instruction[6] == "1" and instruction[7] == "0" and cc[2] == '1'):
        EA_PC_dec = int(to_one_str(EA), 2)
        EA_PC_bin = bin(EA_PC_dec)
        pc.set(EA_PC_bin[2:].zfill(12))
        jcc012_result.append("pc")
        jcc012_result.append(pc.num)
    else:
        pc.set(pc.num)
        jcc012_result.append("pc")
        jcc012_result.append(pc.num)
    return jcc012_result


def jma013(instruction):  # Unconditional Jump To Address
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    jma013_result = copy.deepcopy(EA_result)
    EA_PC_dec = int(to_one_str(EA), 2)
    EA_PC_bin = bin(EA_PC_dec)
    pc.set(EA_PC_bin[2:].zfill(12))
    print("EA_PC_dec", EA_PC_dec)
    jma013_result.append("pc")
    jma013_result.append(pc.num)
    return jma013_result


def jsr014(instruction):  # Jump if condition code
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    jsr014_result = copy.deepcopy(EA_result)
    PC1_bin = bin(int(pc.num, 10) + 1)
    gpr3.set(PC1_bin.zfill(16))
    jsr014_result.append("gpr3")
    jsr014_result.append(gpr3.num)

    EA_PC_dec = int(to_one_str(EA), 2)
    EA_PC_bin = bin(EA_PC_dec)
    pc.set(EA_PC_bin[2:].zfill(12))
    jsr014_result.append("pc")
    jsr014_result.append(pc.num)
    return jsr014_result


def rfs015(instruction):  # Jump if condition code
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    rfs015_result = copy.deepcopy(EA_result)
    GPR3_dec = int(to_one_str(gpr3.num), 2)
    GPR3_bin = bin(GPR3_dec)
    pc.set(GPR3_bin[2:].zfill(12))
    rfs015_result.append("pc")
    rfs015_result.append(pc.num)
    immed = "".join(instruction[-5:])
    gpr0.set(immed.zfill(12))
    rfs015_result.append("gpr0")
    rfs015_result.append(gpr0.num)
    return rfs015_result


#
#
#
def sob016(instruction):  # Subtract One and Branch. R = 0..3 update
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    sob016_result = copy.deepcopy(EA_result)
    if instruction[6] == "0" and instruction[7] == "0":
        s0 = "".join(gpr0.num)
        s1 = int(to_one_str(s0), 2) - 1
        s0 = bin(s1)
        gpr0.set(s0[2:].zfill(16))
        sob016_result.append("gpr0")
        sob016_result.append(gpr0.num)
    elif instruction[6] == "0" and instruction[7] == "1":
        s0 = "".join(gpr1.num)
        s0 = int(to_one_str(s0), 2) - 1
        s0 = bin(s0)
        gpr1.set(s0[2:].zfill(16))
        sob016_result.append("gpr1")
        sob016_result.append(gpr1.num)
    elif instruction[6] == "1" and instruction[7] == "0":
        s0 = "".join(gpr2.num)
        s0 = int(to_one_str(s0), 2) - 1
        s0 = bin(s0)
        gpr2.set(s0[2:].zfill(16))
        sob016_result.append("gpr2")
        sob016_result.append(gpr2.num)
    elif instruction[6] == "1" and instruction[7] == "1":
        s0 = "".join(gpr3.num)
        s0 = int(to_one_str(s0), 2) - 1
        s0 = bin(s0)
        gpr3.set(s0[2:].zfill(16))
        sob016_result.append("gpr3")
        sob016_result.append(gpr3.num)
    if (instruction[6] == "0" and instruction[7] == "0" and int(to_one_str(gpr0.num), 2) - 1 > 0) \
            or (instruction[6] == "0" and instruction[7] == "1" and int(to_one_str(gpr1.num), 2) - 1 > 0) \
            or (instruction[6] == "1" and instruction[7] == "0" and int(to_one_str(gpr2.num), 2) - 1 > 0) \
            or (instruction[6] == "1" and instruction[7] == "1" and int(to_one_str(gpr3.num), 2) - 1 > 0):
        EA_PC_dec = int(to_one_str(EA), 2)
        EA_PC_bin = bin(EA_PC_dec)
        pc.set(EA_PC_bin[2:].zfill(12))
        sob016_result.append("pc")
        sob016_result.append(pc.num)
    else:
        pc.set(pc.num)
        sob016_result.append("pc")
        sob016_result.append(pc.num)
    print("gpr3sob:", int(to_one_str(gpr3.num), 2))
    return sob016_result


def jge017(instruction):  # Jump Greater Than or Equal To
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  # indirect EA use fetch
        del EA_result[-2:]
    jge017_result = copy.deepcopy(EA_result)
    if (instruction[6] == "0" and instruction[7] == "0" and string_to_int(to_one_str(gpr0.num)) >= 0) \
            or (instruction[6] == "0" and instruction[7] == "1" and string_to_int(to_one_str(gpr1.num)) >= 0) \
            or (instruction[6] == "1" and instruction[7] == "0" and string_to_int(to_one_str(gpr2.num)) >= 0) \
            or (instruction[6] == "1" and instruction[7] == "1" and string_to_int(to_one_str(gpr3.num)) >= 0):
        EA_PC_dec = int(to_one_str(EA), 2)
        EA_PC_bin = bin(EA_PC_dec)
        pc.set(EA_PC_bin[2:].zfill(12))
        jge017_result.append("pc")
        jge017_result.append(pc.num)
        print("jge pcnum>0:", pc.num)
    else:
        pc.set(pc.num)
        jge017_result.append("pc")
        jge017_result.append(pc.num)
        print("jge pcnum<0:", pc.num)
    return jge017_result


# Shift Register by Count
def src(instruction):
    count_bin = ''.join(i for i in instruction[12:])
    count = int(count_bin, 2)
    register = get_register(instruction)
    value = register.num
    if is_left(instruction):
        result = shiftLeft(value, count, instruction)
    else:
        result = shiftRight(value, count, instruction)
    register.num = result
    print(register.num)
    return [register.name, register.num]


def is_arithmetic(instruction):
    if instruction[8] == '0':
        return True
    else:
        return False


def is_left(instruction):
    if instruction[9] == '1':
        return True
    else:
        return False


def shiftLeft(value, count, instruction):
    # count = 0..15
    if count == 0:
        return value
    if is_arithmetic(instruction):
        value = [value[0]] + value[count + 1:] + ['0'] * count
    else:
        value = value[count:] + ['0'] * count
    return value


def shiftRight(value, count, instruction):
    if count == 0:
        return value
    if is_arithmetic(instruction):
        result = ([value[0]] + [value[0]] * count + value[1:16 - count])
    else:
        result = ['0'] * count + value[:16 - count]
    return result


# Rotate Register by Count
def rrc(instruction):
    count_bin = ''.join(i for i in instruction[12:])
    count = int(count_bin, 2)
    register = get_register(instruction)
    value = register.num
    if is_left(instruction):
        # Put the head to tail
        result = value[count:] + value[:count]
    # Else rotate right
    else:
        # Put the tail to head
        result = value[-count:] + value[:-count]
    register.num = result
    return [register.name, register.num]


def out(instruction):
    deviceId_bin = ''.join(i for i in instruction[11:])
    deviceId = int(deviceId_bin, 2)
    value = get_register(instruction).num
    # Get the ASCII code for the character
    value_int = string_to_int(value)
    print("value_int:", value_int)
    output = chr(value_int)
    print("out:", output)
    return ['out', output]


def trap(instruction):
    pc_bin = ''.join(i for i in pc.num)
    pc_int = int(pc_bin, 2)
    pc_int = pc_int + 1
    pc_adr = list(str(bin(pc_int)[2:].zfill(12)))
    Cache.write_reg_to_c_m(2, pc_adr)
    memory[2] = pc_adr
    trapcode = int(''.join(i for i in instruction[12:]), 2)
    table_adr = int(''.join(i for i in memory[0]), 2)
    routine_adr = table_adr + trapcode
    pc.num = list(str(bin(routine_adr)[2:].zfill(12)))
    fetch(pc.num)
    show_result = process_instr()
    pc.num = memory[2]
    return show_result


def fadd033(instruction):  # Floating Add Memory To Register
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  #
        del EA_result[-2:]
    fadd033_result = copy.deepcopy(EA_result)
    print("faddEA", EA)
    if (instruction[6] == "0" and instruction[7] == "0" and instruction[10] == "0"):
        fetch(EA[-12:])
        EA_dec = int(to_one_str(mbr.num), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr0.num))
        fr_result_dec = fr_dec + EA_dec
        print("00+", "frdec:", fr_dec, "EAdec", EA_dec)
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr0.set(a)
        fadd033_result.append("fr0")
        fadd033_result.append(fr0.num)
        print("fr = 0, I = 0")
    elif (instruction[6] == "0" and instruction[7] == "1" and instruction[10] == "0"):
        fetch(EA[-12:])
        EA_dec = int(to_one_str(mbr.num), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr1.num))
        fr_result_dec = fr_dec + EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr1.set(a)
        fadd033_result.append("fr1")
        fadd033_result.append(fr1.num)
        print("fr = 1, I = 0")
    elif (instruction[6] == "0" and instruction[7] == "0" and instruction[10] == "1"):
        EA_result = cal_EA(list(EA))
        EA = EA_result.pop()
        if len(EA_result) != 0:  #
            del EA_result[-2:]
        EA_dec = int(to_one_str(EA), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr0.num))
        fr_result_dec = fr_dec + EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr0.set(a)
        fadd033_result.append("fr0")
        fadd033_result.append(fr0.num)
        print("fr = 0, I = 0")
    elif (instruction[6] == "0" and instruction[7] == "1" and instruction[10] == "1"):
        EA_result = cal_EA(list(EA))
        EA = EA_result.pop()
        if len(EA_result) != 0:  #
            del EA_result[-2:]
        EA_dec = int(to_one_str(EA), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr1.num))
        fr_result_dec = fr_dec + EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr1.set(a)
        fadd033_result.append("fr1")
        fadd033_result.append(fr1.num)
        print("fr = 1, I = 0")
    if check_mul_overflew(fr_result_dec):
        cc.set_overflow("1")
        fadd033_result.append('cc')
        fadd033_result.append('overflow_1')
        print("over flow in fadd033")
    return fadd033_result


def fsub034(instruction):  # Floating Subtract Memory From Register
    EA_result = cal_EA(instruction)
    EA = EA_result.pop()
    if len(EA_result) != 0:  #
        del EA_result[-2:]
    fsub034_result = copy.deepcopy(EA_result)
    if (instruction[6] == "0" and instruction[7] == "0" and instruction[10] == "0"):
        fetch(EA[-12:])
        EA_dec = int(to_one_str(mbr.num), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr0.num))
        fr_result_dec = fr_dec - EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr0.set(a)
        fsub034_result.append("fr0")
        fsub034_result.append(fr0.num)
        print("fr = 0, I = 0")
    elif (instruction[6] == "0" and instruction[7] == "1" and instruction[10] == "0"):
        fetch(EA[-12:])
        EA_dec = int(to_one_str(mbr.num), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr1.num))
        fr_result_dec = fr_dec - EA_dec
        print("frdec:", fr_dec, "EAdec", EA_dec)
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr1.set(a)
        fsub034_result.append("fr1")
        fsub034_result.append(fr1.num)
        print("fr = 1, I = 0")
    elif (instruction[6] == "0" and instruction[7] == "0" and instruction[10] == "1"):
        EA_result = cal_EA(list(EA))
        EA = EA_result.pop()
        if len(EA_result) != 0:  #
            del EA_result[-2:]
        EA_dec = int(to_one_str(EA), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr0.num))
        fr_result_dec = fr_dec - EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr0.set(a)
        fsub034_result.append("fr0")
        fsub034_result.append(fr1.num)
        print("fr = 0, I = 1")
    elif (instruction[6] == "0" and instruction[7] == "1" and instruction[10] == "1"):
        EA_result = cal_EA(list(EA))
        EA = EA_result.pop()
        if len(EA_result) != 0:  #
            del EA_result[-2:]
        EA_dec = int(to_one_str(EA), 2)
        fr_dec = convertbin16_tofloat(to_one_str(fr1.num))
        fr_result_dec = fr_dec - EA_dec
        fr_result = convertfloat2bin16(fr_result_dec)
        a = [num for num in fr_result]
        fr1.set(a)
        fsub034_result.append("fr1")
        fsub034_result.append(fr1.num)
        print("fr = 1, I = 1")
    if check_mul_overflew(fr_result_dec):
        cc.set_underflow("1")
        fsub034_result.append('cc')
        fsub034_result.append('underflow_1')
        print("underflow in fsub034")
    return fsub034_result


def vector_add(instruction):
    if instruction[6] == "0" and instruction[7] == "0":
        fr = fr0
    elif instruction[6] == "0" and instruction[7] == "1":
        fr = fr1
    fr_dec_value = int("".join(fr.num), 2)
    EA = int("".join(instruction[-5:]), 2)
    EA_second = list(str(bin(EA + 1)[2:].zfill(5)))
    instruction2 = instruction[:11] + EA_second
    first_adr = get_data_from_memory(instruction)[3]
    adr1 = int("".join(first_adr), 2)
    sec_adr = get_data_from_memory(instruction2)[3]
    adr2 = int("".join(sec_adr), 2)
    result = ""
    for i in range(fr_dec_value):
        adr_vector1 = adr1 + i
        vector_sum = int(''.join(n for n in Cache.read_cache(adr_vector1)), 2) + int(
            ''.join(n for n in Cache.read_cache(adr2 + i)), 2)
        result = result + str(vector_sum) + ","
    print("The result is " + result)
    Cache.write_reg_to_c_m(adr_vector1, int_to_string(vector_sum))
    return result


def vector_sub(instruction):
    if instruction[6] == "0" and instruction[7] == "0":
        fr = fr0
    elif instruction[6] == "0" and instruction[7] == "1":
        fr = fr1
    fr_dec_value = int("".join(fr.num), 2)
    EA = int("".join(instruction[-5:]), 2)
    EA_second = list(str(bin(EA + 1)[2:].zfill(5)))
    instruction2 = instruction[:11] + EA_second
    first_adr = get_data_from_memory(instruction)[3]
    adr1 = int("".join(first_adr), 2)
    sec_adr = get_data_from_memory(instruction2)[3]
    adr2 = int("".join(sec_adr), 2)
    result = ""
    for i in range(fr_dec_value):
        adr_vector1 = adr1 + i
        sub = int(''.join(n for n in Cache.read_cache(adr_vector1)), 2) - int(
            ''.join(n for n in Cache.read_cache(adr2 + i)), 2)
        result = result + str(sub) + ","
    print("The result is " + result)
    Cache.write_reg_to_c_m(adr_vector1, int_to_string(sub))
    return result


def run_vector(v1_1, v1_2, v1_3, v2_1, v2_2, v2_3, select):
    # memory 0 store the address of vector1
    instruction = ['1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    """""
    print("Please input the 1st value for vector1:")
    v1_1 = input()
    print("Please input the 2nd value for vector1:")
    v1_2 = input()
    print("Please input the 3rd value for vector1:")
    v1_3 = input()
    print("Please input the 1st value for vector2:")
    v2_1 = input()
    print("Please input the 2nd value for vector2:")
    v2_2 = input()
    print("Please input the 3rd value for vector1:")
    v2_3 = input()
    """
    fr0.num = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1']
    # address 2
    memory[0] = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0']
    # address 5
    memory[1] = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1']
    memory[2] = int_to_string(int(v1_1))
    memory[3] = int_to_string(int(v1_2))
    memory[4] = int_to_string(int(v1_3))
    memory[5] = int_to_string(int(v2_1))
    memory[6] = int_to_string(int(v2_2))
    memory[7] = int_to_string(int(v2_3))


    # print("Please enter the number for: 1:vector add,2: vector sub:")
    # select = int(input())
    if int(select) == 1:
        return vector_add(instruction)
    elif int(select) == 2:
        return vector_sub(instruction)
    else:
        print("Invalid Number")
        return "Invalid"


def process_instr():
    opcode = int("".join(i for i in ir.num[:6]), 2)
    if opcode == 1:
        return ldr001(ir.num)
    elif opcode == 2:
        return str002(ir.num)
    elif opcode == 3:
        return lda003(ir.num)
    elif opcode == 4:
        return amr(ir.num)
    elif opcode == 5:
        return smr(ir.num)
    elif opcode == 6:
        return air(ir.num)
    elif opcode == 7:
        return sir(ir.num)
    elif opcode == 25:
        return src(ir.num)
    elif opcode == 26:
        return rrc(ir.num)

    elif opcode == 50:
        return out(ir.num)

    elif opcode == 33:
        return ldx041(ir.num)
    elif opcode == 34:
        return stx042(ir.num)

    elif opcode == 8:  # Jump if Zero
        return jz010(ir.num)

    elif opcode == 9:  # Jump if Zero
        return jne011(ir.num)

    elif opcode == 10:
        return jcc012(ir.num)

    elif opcode == 11:
        return jma013(ir.num)

    elif opcode == 12:
        return jsr014(ir.num)

    elif opcode == 13:
        return rfs015(ir.num)

    elif opcode == 14:
        return sob016(ir.num)

    elif opcode == 15:
        return jge017(ir.num)

    elif opcode == 0:
        return halt000()

    elif opcode == 16:
        return mlt020(ir.num)

    elif opcode == 17:
        return dvd021(ir.num)

    elif opcode == 18:
        return trr022(ir.num)

    elif opcode == 19:
        return and023(ir.num)

    elif opcode == 20:
        return orr024(ir.num)

    elif opcode == 21:
        return not025(ir.num)
    elif opcode == 49:
        return in061(ir.num)
    elif opcode == 25:
        return fadd033(ir.num)
    elif opcode == 26:
        return fsub034(ir.num)
    else:
        print("incorrect opcode", opcode)


# program 1.

global Consolekey
Consolekey = ["0"] * 30
Consolekey_out = list()
# beiju
