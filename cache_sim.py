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



def find_set(cache, item):
    pass


def init_cache(k, set_size):
    cache = treeNode()
    for i in range(k):
        new_set = treeNode("set")
        cache.addChild("set")
        for j in range(set_size):
            line = treeNode(None)
            new_set.addChild(line)
    return cache


class treeNode:
    def __init__(self, name = 'root', children = None):
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