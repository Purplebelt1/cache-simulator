import math
import random

read_list = []


class readItem:
    def __init__(self, addr, replace_loc=None, is_hit=False):
        self.is_hit = is_hit
        self.addr = int(addr)
        self.replace_loc = replace_loc

    def getIsHit(self):
        return self.is_hit

    def getAddr(self):
        return self.addr

    def getReplaceLoc(self):
        return self.replace_loc

    def setIsHit(self, boolean):
        self.is_hit = boolean
        return self.is_hit

    def setAddr(self, addr):
        self.addr = addr
        return self.addr

    def setReplaceLoc(self, location):
        self.replace_loc = location
        return self.replace_loc


def data_creation(mem_len, number_of_reads):
    counter = 0
    while counter < number_of_reads:
        new_addr = create_address(mem_len)
        read_object = readItem(new_addr)
        read_list.append(read_object)
    return read_list


def create_address(mem_len):
    addr = ""
    addr_len = math.log2(mem_len)
    for i in range(addr_len):
        temp = str(random.randint(0, 1))
        addr += temp
    final_addr = int(addr)
    return final_addr
