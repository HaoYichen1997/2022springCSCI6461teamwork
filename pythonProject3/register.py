import copy
class register:
    def __init__(self, num: list[16]):
        self.num = num

    def check(self, num):
        for nums in num:
            if nums != 1 and nums != 0:
                return False
        return True

    def set(self, num: list[16]):
        if self.check(num):
            self.num = copy.deepcopy(num)
        else:
            print(f"{num} is not binary")

class Gpr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)

    '''
    def show_Panel(self,a: int):
        if a == 0:
            GPR0.insert(0, str(self.num))
        elif a == 1:
            GPR1.insert(0, str(self.num))
        elif a == 2:
            GPR2.insert(0, str(self.num))
        elif a == 3:
            GPR3.insert(0, str(self.num))
        else: print("mistake in show_panel")
    '''

class Ixr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)
'''
    def show_Panel(self,a: int):
        if a == 1:
            IXR1.insert(0, str(self.num))
        elif a == 2:
            IXR2.insert(0, str(self.num))
        elif a == 3:
            IXR3.insert(0, str(self.num))
        else: print("mistake in show_panel")
'''
class Mbr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)

    '''
    def show_Panel(self):
        MBR.insert(0,str(self.num))
    '''

class Mar(register):
    def __init__(self, num: list[12]):
        self.num = num

    def set(self, num: list[12]):
        if self.check(num):
            self.num = num
        else:
            print(f"{num} is not binary in MAR")

    '''
    def show_Panel(self):
        MAR.insert(0,str(self.num))
    '''
class Pc(register):
    def __init__(self, num: list[12]):
        self.num = num

    '''
    def show_Panel(self):
        PC.insert(0,str(self.num))
    '''

    def set(self, num: list[12]):
        if self.check(num):
            self.num = num
        else:
            print(f"{num} is not binary in PC")

class Ir(register):
    def __init__(self, num: list[16]):
        super().__init__(num)

    '''
    def show_Panel(self):
        IR.insert(0,str(self.num))
    '''
