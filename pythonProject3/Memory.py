from collections import OrderedDict


def main():
    print("Load the program")
    loadfile()


def loadfile():
    lines = []
    with open('IPL.txt') as f:
        lines = f.readlines()

    count = 0
    memory_dict: OrderedDict[str, str] = OrderedDict()
    for line in lines:
        count += 1
        print(f'line {count}: {line}')
        # delete the \n in the string
        line = line.strip('\n')
        address, data = line.split(" ")
        # transform hex to binary
        address = bin(int(address, 16))
        data = bin(int(data, 16))
        memory_dict[address] = data

    print(memory_dict)

#memory[i] = i.value LDR 1 0 010
if __name__ == "__main__":
    main()


class Memory(object):
    MEMORY_SIZE = 2048
    TRAP_INSTRUCTION = 0
    MACHINE_FAULT = 1
    PC_FOR_TRAP = 2
    PC_FOR_MACHINE_FAULT = 4

    memory_dict = OrderedDict()

    def __init__(self, mem_bytes: bytes):
        self.mem_bytes = mem_bytes

    def get_byte(self, pos: int) -> bytes:
        """
        get byte at the position
        """
        # return self.mem_bytes[pos: pos]
        pass
