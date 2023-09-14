import math
from data_creation import read_item


def cache_sim(read_item_list, mem_size, page_size, cache_size, k):

    block_num = mem_size/page_size
    line_num = cache_size/page_size
    set_size = line_num/k

    len_addr = math.log2(mem_size)
    len_offset = math.log2(page_size)
    len_page_num = len_addr - len(len_offset)
    len_tag = math.log2(k)

    cache = init_cache(k, set_size)

    for i in read_item_list:
        set = find_set(cache, i,len_page_num, len_tag)


def find_set(cache, item, len_page_num, len_tag):

    page_num = item.get_addr()[:len_page_num]
    tag = item.get_addr()[len_page_num-len_tag:len_page_num]
    offset = item.get_addr()[len_page_num:]

    sets = cache.getChildren()
    if len(sets) == 1:
        return sets[0]
    set = None

    for i in sets:
        if i.getName() == tag:
            set = i
            break
    
    return set

def binary(n, bit):
    return format(n, '0' + str(bit) + 'b')

def init_cache(k, set_size):
    cache = treeNode()
    if k == 1:
        new_set = treeNode("set")
        cache.addChild(new_set)
        for j in range(set_size):
            line = treeNode(None)
            new_set.addChild(line)
        return cache
    for i in range(k):
        new_set = treeNode(binary(i, k-1))
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
