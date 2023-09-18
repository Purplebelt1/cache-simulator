from cache_sim import read_item_list
from collections import Counter

hit_ratio = 0
replacement_count = 0

for i in read_item_list:
    if i.getIsHit == True:
        hit_ratio += 1
    if i.getReplaceLoc != None:
        replacement_count += 1
    else:
        pass

hit_ratio = hit_ratio/len(read_item_list)
spacial_locality = counter(read_item_list)

#temporal locality, this will probably change
for i in read_item_list:
    print i.getAddr()
