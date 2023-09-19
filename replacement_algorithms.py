# File written by William DeBlieck

def first_in_first_out(set):
    # Initialize variables to track the first-in item and its index
    first_in = float("inf")  # Set to positive infinity to ensure replacement
    inc = 0  # Counter for iterating through cache lines
    idx = 0  # Index of the first-in item

    # Iterate through the cache lines within the specified set
    for i in set.getChildren():
        # Check if the cache line is empty (contains no data)
        if i.getName() is None:
            # If an empty line is found, return its index for replacement
            return idx
        
        # Compare the time added of the data in the line with the first-in time
        if first_in > i.getName().getTimeAdded():
            # If the current line's data was added earlier, update the first-in item and its index
            idx = inc
            first_in = i.getName().getTimeAdded()

        inc += 1

    # Return the index of the first-in item for replacement
    return idx


def least_recently_used(set):
    # Initialize variables to track the least recently used item and its index
    last_used = float("-inf")  # Set to negative infinity to ensure replacement
    inc = 0  # Counter for iterating through cache lines
    idx = 0  # Index of the least recently used item

    # Iterate through the cache lines within the specified set
    for i in set.getChildren():
        # Check if the cache line is empty (contains no data)
        if i.getName() is None:
            # If an empty line is found, return its index for replacement
            return idx
        
        # Compare the last read time of the data in the line with the last used time
        if last_used < i.getName().getLastRead():
            # If the current line's data was read more recently, update the least recently used item and its index
            idx = inc
            last_used = i.getName().getLastRead()

        inc += 1

    # Return the index of the least recently used item for replacement
    return idx
