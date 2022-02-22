import copy
# the registers class
# father class is 16-bit
class register:
    def __init__(self, num: list[16]):
        self.num = num

    def check(self, num):
        for nums in num:
            if nums != "1" and nums != "0":
                return False
        return True

    def set(self, num: list[16]):
        if self.check(num):
            self.num = copy.deepcopy(num)
        else:
            print(f"{num} is not binary in 16-bit")

class Gpr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)


class Ixr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)

class Mbr(register):
    def __init__(self, num: list[16]):
        super().__init__(num)


class Mar(register):
    def __init__(self, num: list[12]):
        self.num = num

    def set(self, num: list[12]):
        if self.check(num):
            self.num = num
        else:
            print(f"{num} is not binary in MAR")

class Pc(register):
    def __init__(self, num: list[12]):
        self.num = num

    def set(self, num: list[12]):
        if self.check(num):
            self.num = num
        else:
            print(f"{num} is not binary in PC")

class Ir(register):
    def __init__(self, num: list[16]):
        super().__init__(num)

