import xml.etree.ElementTree as ET
from data_creation import read_list

def conversion_to_decimal(x):
    byte_level = x[-2:]
    if byte_level == "BT":
        byte_level = 2
    if byte_level == "KB":
        byte_level = 2^10
    if byte_level == "MB":
        byte_level = 2^20
    if byte_level == "GB":
        byte_level = 2^30
    else:
        return ("Sizes must be in BT, KB, MB, or GB")
    
    return (x[:-2] * byte_level)

conversion_to_decimal("128MB")

def read_inputs():
    tree = ET.parse('./config.xml')
    root = tree.getroot()
    
    elements = []

    memory_size = root.find('memory_size').text.lower()


    elements.append(memory_size)

    page_size = root.find('page_size').text.lower()
    elements.append(page_size)

    cache_size = root.find('cache_size').text.lower()
    elements.append(cache_size)

    mapping_type = root.find('mapping_type').text.lower()
    elements.append(mapping_type)

    k = root.find('k').text.lower()
    try:
        k = int(k)
    except:
        return ("K must be an integer")

    if k is not None:
        elements.append(k)

    if mapping_type == 'direct' and k != 1:
        k = 1
        print ("Your k value had been overwritten to 1 due to your choice of direct mapping")

    if cache_size/page_size < k:
        raise ValueError()

    if k is None and mapping_type == 'set_associative':
        raise ValueError()

    elements.append(read_list)

    return elements

read_inputs()
