# File written by William DeBlieck

import math
from data_creation import readItem
from replacement_algorithms import first_in_first_out, least_recently_used

def cache_sim(mem_size, page_size, cache_size, mapping_type, k, algorithm, read_item_list):
    # Calculate the number of blocks in memory based on memory size and page size
    block_num = mem_size / page_size

    # Calculate the number of lines in the cache based on cache size and page size,
    # and round up to the nearest integer
    line_num = math.ceil(cache_size / page_size)

    # Calculate the number of bits needed to represent the memory address
    len_addr = math.ceil(math.log2(mem_size))

    # Calculate the number of bits needed to represent the offset within a page
    len_offset = math.ceil(math.log2(page_size))

    # Calculate the number of bits needed to represent the page number
    len_page_num = len_addr - len_offset

    # Calculate the number of bits needed to represent the line number in the cache
    len_line_num = math.ceil(math.log2(line_num))

    # Check the cache mapping type and call the corresponding cache mapping function
    if mapping_type == "direct":
        post_read_list = direct_map_cache(line_num, read_item_list, len_page_num, len_line_num)
    elif mapping_type == "associative":
        post_read_list = associative_map_cache(read_item_list, line_num, len_page_num, algorithm)
    elif mapping_type == "set-associative":
        post_read_list = set_associative_map_cache(read_item_list, k, line_num, cache_size, len_page_num, algorithm)

    # Return the list of post-read items
    return post_read_list


    
def binary(n, bit):
    return format(n, '0' + str(bit) + 'b')


def set_associative_map_cache(read_item_list, k, line_num, cache_size, len_page_num, algorithm):
    # Calculate the total number of cache sets
    set_num_tot = int(line_num / k)

    # Calculate the number of bits needed to represent the set number
    len_set_num = math.ceil(math.log2(set_num_tot))

    # Initialize the cache as a tree structure with set and line nodes
    cache = TreeNode()

    # Create the cache structure with sets and lines
    for i in range(set_num_tot):
        set_node = TreeNode()
        for j in range(k):
            line_node = TreeNode(name=None)
            set_node.addChild(line_node)
        cache.addChild(set_node)

    increment = 0
    cache_children = cache.getChildren()

    # Iterate through the list of items to read from memory
    for i in read_item_list:
        # Extract the set number bits from the memory address
        set_num = i.getAddr()[len_page_num - len_set_num:len_page_num]

        # Convert the binary set number to an integer for indexing
        search_idx = int(set_num, 2)

        # Get the set within the cache where the item belongs
        search_set = cache_children[search_idx]
        set_children = search_set.getChildren()

        # Find the line index where the item is located (or None if not found)
        line_idx = find_line(search_set, i, len_page_num)

        if line_idx is not None:
            # If the item is found in the cache (cache hit)
            line = set_children[line_idx]
            i.setIsHit(True)
            was_hit = line.getName()
            was_hit.setLastRead(increment)
        else:
            # If the item is not found in the cache (cache miss)
            match algorithm:
                case "fifo":
                    # Use the First-In-First-Out (FIFO) algorithm to determine the replacement line
                    index = first_in_first_out(search_set)
                case "lru":
                    # Use the Least Recently Used (LRU) algorithm to determine the replacement line
                    index = least_recently_used(search_set)

            # Get the old line that will be replaced
            old = set_children[index]

            if old.getName() is not None:
                i.setReplaceLoc(old.getName)

            # Replace the old line with the new item
            old.setName(i)
            i.setTimeAdded(increment)
            i.setLastRead(increment)

        # Update the set and cache data structures
        search_set.setChildren(set_children)
        cache_children[search_idx] = search_set
        cache.setChildren(cache_children)
        increment += 1

    return read_item_list
def associative_map_cache(read_item_list, line_num_tot, len_page_num, algorithm):
    # Initialize the cache as a tree structure with line nodes
    cache = TreeNode()

    # Create the cache structure with lines
    for i in range(line_num_tot):
        line = TreeNode(name=None)
        cache.addChild(line)

    increment = 0
    cache_children = cache.getChildren()

    # Iterate through the list of items to read from memory
    for i in read_item_list:
        # Find the line index where the item is located (or None if not found)
        line_idx = find_line(cache, i, len_page_num)

        if line_idx is not None:
            # If the item is found in the cache (cache hit)
            line = cache_children[line_idx]
            i.setIsHit(True)
            was_hit = line.getName()
            was_hit.setLastRead(increment)
        else:
            # If the item is not found in the cache (cache miss)
            match algorithm:
                case "fifo":
                    # Use the First-In-First-Out (FIFO) algorithm to determine the replacement line
                    index = first_in_first_out(cache)
                case "lru":
                    # Use the Least Recently Used (LRU) algorithm to determine the replacement line
                    index = least_recently_used(cache)

            # Get the old line that will be replaced
            old = cache_children[index]

            if old.getName() is not None:
                i.setReplaceLoc(old.getName)

            # Replace the old line with the new item
            old.setName(i)
            i.setTimeAdded(increment)
            i.setLastRead(increment)

        # Update the cache data structure
        cache.setChildren(cache_children)
        increment += 1

    return read_item_list


def direct_map_cache(line_num_tot, read_item_list, len_page_num, len_line_num):
    # Initialize the cache as a tree structure with line nodes
    cache = TreeNode()

    # Create the cache structure with lines
    for i in range(line_num_tot):
        line = TreeNode(name=None)
        cache.addChild(line)

    # Get the list of cache lines (children of the cache)
    cache_children = cache.getChildren()
    increment = 0

    # Iterate through the list of items to read from memory
    for i in read_item_list:
        # Extract the line number bits from the memory address
        line_num = i.getAddr()[len_page_num - len_line_num:len_page_num]

        # Convert the binary line number to an integer for indexing
        search_idx = int(line_num, 2)

        # Get the cache line corresponding to the extracted line number
        search_node = cache_children[search_idx]

        # Retrieve the data stored in the cache line
        search_data = search_node.getName()

        if search_data is None:
            # If the cache line is empty (cache miss), store the new item in the cache
            search_node.setName(i)
            i.setLastRead(increment)
            i.setTimeAdded(increment)
        else:
            # If the cache line is not empty (cache hit)
            search_value = search_data.getAddr()[:len_page_num]

            if search_value == i.getAddr()[:len_page_num]:
                # If the stored address matches the requested address (cache hit), mark as hit
                i.setIsHit(True)
                search_data.setLastRead(increment)
            else:
                # If there is a different address stored in the cache (cache miss), replace it
                search_data.setReplaceLoc(i.getAddr())
                search_node.setName(i)
                i.setLastRead(increment)
                i.setTimeAdded(increment)

        increment += 1

    return read_item_list

def find_line(set, item, len_page_num):
    idx = 0

    # Iterate through the lines within the specified set
    for i in set.getChildren():
        line_data = i.getName()

        # Check if the line is not empty (contains data)
        if line_data is not None:
            # Compare the address of the data in the line with the address of the item
            if line_data.getAddr()[:len_page_num] == item.getAddr()[:len_page_num]:
                # If the addresses match, return the index of the line (cache hit)
                return idx
        idx += 1

    # If the item is not found in any line of the set, return None (cache miss)
    return None



class TreeNode:
    def __init__(self, name='root', children=None):
        self.__name = name
        self.__children = []
        if children:
            for i in children:
                self.__addChild(i)

    def addChild(self, child):
        if isinstance(child, TreeNode):
            self.__children.append(child)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getChildren(self):
        return self.__children
    
    def setChildren(self, value):
        self.__children = value
    

if __name__ == "__main__":
    bit_list = ["0000000001", "0000000001", "0000000000", "0000000000", "0100000001", "1000000001"]
    read_list = []
    for i in bit_list:
        read_obj = readItem(i)
        read_list.append(read_obj)
    cache_sim(2**10,2**5,2**9, "set-associative", 4, "fifo",read_list)
