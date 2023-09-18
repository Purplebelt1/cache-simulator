import math
from data_creation import readItem
from replacement_algorithms import first_in_first_out, least_recently_used

def cache_sim(mem_size, cache_size, page_size, mapping_type, k, algorithm, read_item_list):
#def cache_sim(read_item_list, mem_size, page_size, cache_size, k, algorithm):

    block_num = mem_size/page_size
    line_num = cache_size/page_size
    set_size = k

    set_num_tot = line_num/k

    len_addr = math.log2(mem_size)
    len_offset = math.log2(page_size)
    len_page_num = len_addr - len(len_offset)
    len_set_num = math.log2(set_num_tot)


    cache = init_cache(set_num_tot, set_size)

    increment = 0
    for i in read_item_list:
        set_num = i.getAddr()[len_page_num-len_set_num:len_page_num]
        set = find_set(cache, set_num)
        line = find_line(set, i)

        # On hit
        if line:
            i.setIsHit(True)
            was_hit = line.getName()
            was_hit.setLastRead(increment)

        # On miss
        else:
            match algorithm:
                case "fifo":
                    index = first_in_first_out(set)
                case "lru":
                    index = least_recently_used(set)
            old = set.getChildren()[index]
            if old.getName != None:
                i.setReplaceLoc(old.getName)
            old.setName(i)
            i.setTimeAdded(increment)
            i.setLastRead(increment)
        increment += 1
    return read_item_list







def find_set(cache,set_num):


    sets = cache.getChildren()
    if len(sets) == 1:
        return sets[0]

    for i in sets:
        if i.getName() == set_num:
            set = i
            break
    
    return set

def find_line(set, item):
    line = None
    for i in set.getChildren():
        if isinstance(i, item):
            if i.getAddr() == item.getAddr():
                line = i
    return line

def binary(n, bit):
    return format(n, '0' + str(bit) + 'b')

def init_cache(set_num_tot, set_size):
    cache = treeNode()
    if set_num_tot == 1:
        new_set = treeNode("set")
        cache.addChild(new_set)
        for j in range(set_size):
            line = treeNode(None)
            new_set.addChild(line)
        return cache
    for i in range(set_num_tot):
        new_set = treeNode(binary(i, set_num_tot-1))
        cache.addChild(new_set)
        for j in range(set_size):
            line = treeNode(None)
            new_set.addChild(line)
    return cache


class treeNode:
    def __init__(self, name='root', children=None):
        self.__name = name
        self.__children = None
        if children:
            for i in children:
                self.__addChild(i)

    def addChild(self, child):
        if isinstance(child, treeNode):
            self.__children.append(child)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getChildren(self):
        return self.__children
