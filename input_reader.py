import xml.etree.ElementTree as ET
import data_creation

def conversion_to_decimal(x):
    byte_level = x[-2:]
    print(byte_level)
    if byte_level == "BT":
        byte_level = 1
    elif byte_level == "KB":
        byte_level = 2**10
    elif byte_level == "MB":
        byte_level = 2**20
    elif byte_level == "GB":
        byte_level = 2**30
    else:
        return ("Sizes must be in BT, KB, MB, or GB")
    
    y = int(x[:-2]) * byte_level

    return (y)

def read_inputs():
    tree = ET.parse('./config.xml')
    root = tree.getroot()
    
    elements = []

    memory_size = root.find('memory_size').text.lower()
    memory_size = conversion_to_decimal(memory_size)

    page_size = root.find('page_size').text.lower()
    page_size = conversion_to_decimal(page_size)

    if memory_size % page_size != 0:
        raise ValueError ("Page size not applicable to current memory size")

    if (memory_size/page_size) % 2 != 0:
        raise ValueError ("Memory size must be divisible by page size")
    
    elements.append(memory_size)
    elements.append(page_size)

    cache_size = root.find('cache_size').text.lower()
    cache_size = conversion_to_decimal(cache_size)
    elements.append(cache_size)

    mapping_type = root.find('mapping_type').text.lower()
    elements.append(mapping_type)

    k = root.find('k').text.lower()

    if k is None:
        pass

    else:
        try:
            k = int(k)
        except:
            raise ValueError ("K must be an integer")

        if mapping_type == 'direct' and k != 1:
            k = 1
            print ("Your k value had been overwritten to 1 due to your choice of direct mapping")

        if cache_size/page_size < k:
            raise ValueError("k must be less than the number of lines")

        if k is None and mapping_type == 'set_associative':
            raise ValueError("K must have a value for set associative mapping")
        
    elements.append(k)  



    num_reads = root.find('num_reads').text.lower()

    read_list = data_creation.data_creation(memory_size, num_reads)

    elements.append(read_list)

    return elements

if __name__ == "__main__":
    read_inputs()
