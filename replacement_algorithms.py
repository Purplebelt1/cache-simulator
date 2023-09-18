def first_in_first_out(set):

    first_in = float("inf")
    inc = 0
    idx = 0

    for i in set.getChildren():

        if i.getName() == None:
            return idx
        
        if first_in > i.getName.getTimeAdded():
            idx = inc
            first_in = i.getName.getTimeAdded()

        inc += 1

    return idx


def least_recently_used(set):

    last_used = float("-inf")
    inc = 0
    idx = 0

    for i in set.getChildren():

        if i.getName() == None:
            return idx
        
        if last_used < i.getName.getLastRead():
            idx = inc
            last_used = i.getName.getLastRead()

        inc += 1

    return idx