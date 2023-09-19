# File written by Cody Zahn

import math
import random


class readItem:
    def __init__(self, addr, replace_loc=None, is_hit=False):
        self.is_hit = is_hit
        self.addr = addr
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
    # Create an empty list to store the generated binary strings.
    read_list = []

    # Calculate the number of bits required to represent 'mem_len' in binary.
    num_bits = str(int(math.log2(mem_len)))

    # Create a format string to ensure the generated binary strings have leading zeros
    # to match the required number of bits.
    bits_format = "0" + num_bits + "b"

    # Initialize a counter to keep track of the number of generated binary strings.
    counter = 0

    # Start a loop that continues until 'counter' reaches 'number_of_reads'.
    while counter < number_of_reads:
        # Generate a random integer between 0 and 'mem_len - 1'.
        new_addr = random.randint(0, mem_len - 1)

        # Convert the random integer to a binary string using the specified format.
        new_addr = format(new_addr, bits_format)

        # Create a 'readItem' object using the generated binary string as address.
        read_object = readItem(new_addr)

        # Append the 'read_object' to the 'read_list'.
        read_list.append(read_object)

        # Increment the counter by 1.
        counter += 1

    # Return the list of generated 'readItem' objects.
    return read_list


