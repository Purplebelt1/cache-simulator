from cache_sim import read_item_list

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

