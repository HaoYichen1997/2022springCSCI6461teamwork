import instructions
import copy
# define cache
cache = [0] * 16
for elements in range(16):  # elements 0 == val, elements 1 == Block Num, elements 2-9 == 8 words
    cache[elements] = ["0"] * 10

cache_length = 16
line_words = 8
add_counter = 0

# define cache variable
# define idx number
# for i in range(16):
#     exec("Idx")
for i in range(8):
    instructions.memory[i] = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0"]

'''
'''

def write_reg_to_c_m(address:int, contents:list): # address dec 0-2047, content:16bits
    # write to cache
    if check_cache_line(address):  # if already in cache, change
        cache_line = get_cache_line(address)
        offset = get_address_offset(address)
        cache_line[offset+2] = copy.deepcopy(contents)
    else:  # not in cache, add to the cache
        cache_line = add_to_cache(address)
        offset = get_address_offset(address)
        cache_line[offset + 2] = copy.deepcopy(contents)
    add_counter += 1
    # write to mem
    instructions.memory[address] = contents


def check_cache_line(address:int):   # only check the block num
    cache_line = get_cache_line(address)
    if cache_line is None:
        return False
    else:
        return True
'''
'''


def add_to_cache(address):  # add content in cache
    global add_counter
    if add_counter < cache_length:
        cache_line = cache[add_counter]
        load_from_memory(address, cache_line)
        print(cache[add_counter])

    else:
        cache_line = cache[add_counter % 16]
        load_from_memory(address, cache_line)
        print(cache[add_counter])

    add_counter += 1
    return cache_line


def read_cache(address: int):  # try find content in cache
    cache_line = get_cache_line(address)
    offset = get_address_offset(address)
    if cache_line is None:  # not in cache
        cache_line = add_to_cache(address)
    return get_words(offset, cache_line)


def get_cache_line(address):
    for cache_line in cache:
        if is_valid(cache_line):
            if check_tag(cache_line, address):
                return cache_line
    return None


def is_valid(cache_line):
    if cache_line[0] == 1:
        return True
    else:
        return False


def load_from_memory(address, cache_line):  # mem to cache
    # set valid
    cache_line[0] = 1
    # set tag
    cache_line[1] = get_address_tag(address)
    # get words from memory and load to cache
    for index in range(8):
        cache_line[index + 2] = instructions.memory[address + index]


def check_tag(cache_line, address):
    if get_line_tag(cache_line) == get_address_tag(address):
        return True
    return False


def get_address_tag(address: int):  # second element
    tag = address // line_words
    return tag


def get_address_offset(address: int):
    offset = address % line_words
    return offset


def get_line_tag(line):
    return line[1]


def get_words(offset: int, cache_line):
    word = cache_line[offset+2]
    return word


read_cache(0)
