import xml.etree.ElementTree as ET
from data_creation import read_list

def read_inputs():
    tree = ET.parse('./input/conf.xml')
    root = tree.getroot()
    
    elements = []

    memory_size = root.find('memory_size').text.lower()
    elements.append(memory_size)

    line_size = root.find('line_size').text.lower()
    elements.append(line_size)

    cache_size = root.find('cache_size').text.lower()
    elements.append(cache_size)

    mapping_type = root.find('mapping_type').text.lower()
    elements.append(mapping_type)

    k = root.find('k').text.lower()

    if k is not None:
        elements.append(k)

    if mapping_type == 'direct' and k != 1:
        k = 1
        print ("Your k value had been overwritten to 1 due to your choice of direct mapping)

    if k is None and mapping_type = 'set_associative':
        raise ValueError()

    elements.append(read_list)

    return elements

read_inputs()
