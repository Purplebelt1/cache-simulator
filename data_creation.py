import math
import random


class readItem:
    def __init__(self, addr, replace_loc=None, is_hit=False):
        self.is_hit = is_hit
        self.addr = int(addr)
        self.replace_loc = replace_loc
        self.last_read = 0
        self.time_added = 0

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
    
    def getLastRead(self):
        return self.last_read
    
    def setLastRead(self, value):
        self.last_read = value

    def getTimeAdded(self):
        return self.time_added
    
    def setTimeAdded(self, value):
        self.time_added = value


def data_creation(mem_len, number_of_reads):
    read_list = []
    counter = 0
    while counter < number_of_reads:
        new_addr = random.randint(0,mem_len -1)
        new_addr = format(new_addr, '0' + str(int(math.log2(mem_len)) + 'b'))
        read_object = readItem(new_addr)
        read_list.append(read_object)
    return read_list

