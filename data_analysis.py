# File written by Monsour Sims

from output import append_to_txt_file, write_to_txt_file

def data_analysis(read_item_list):
    hit_ratio = 0
    replacement_count = 0
    address_map = {}
    temp_list = []

    write_to_txt_file("./output/hit_replace.txt", ["Data Analysis", "------------------------","","Hit Ratio:"])


    for i in read_item_list:
        address = i.getAddr()
        temp_list.append(address)
        if address in address_map:
            address_map[address] += 1
        else:
            address_map[address] = 1
        if i.getIsHit() == True:
            hit_ratio += 1
        if i.getReplaceLoc() != None:
            replacement_count += 1

    hit_ratio = hit_ratio/len(read_item_list)

    append_to_txt_file("./output/hit_replace.txt", [str(hit_ratio)])

    append_to_txt_file("./output/hit_replace.txt", ["", "Replacement Count:", str(replacement_count)])
    
    write_to_txt_file("./output/spatial_locality.txt", ["Spactial Locality:", "------------------------", ""])

    result_list = [f"{key}: {value}" for key, value in address_map.items()]
    append_to_txt_file("./output/spatial_locality.txt", result_list)

    write_to_txt_file("./output/temporal_locality.txt", ["Temporal Locality:", "------------------------", ""])
    append_to_txt_file("./output/temporal_locality.txt", temp_list)
