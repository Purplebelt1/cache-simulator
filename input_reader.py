import xml.etree.ElementTree as ET
import data_creation

def conversion_to_decimal(x):
    byte_level = x[-2:]
    if byte_level == "bt":
        byte_level = 1
    elif byte_level == "kb":
        byte_level = 2**10
    elif byte_level == "mb":
        byte_level = 2**20
    elif byte_level == "gb":
        byte_level = 2**30
    else:
        ValueError("Sizes must be in BT, KB, MB, or GB")
    
    y = int(int(x[:-2]) * byte_level)

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

    print(k)

    if k == "null" or mapping_type != "set-associative":
        if mapping_type == "direct":
            k = cache_size/page_size
        elif mapping_type == "associative":
            k = 1
        elif mapping_type == "set-associative":
            ValueError("Can't set k to Null if set associative is mapping type.")
    else:
        print(type(page_size))
        print(type(cache_size))
        try:
            k = int(k)
        except:
            raise ValueError ("K must be an integer")
        print(type(k))
        if cache_size/page_size < int(k):
            raise ValueError("k must be less than the number of lines")
        
    elements.append(k)  

    algorithm = root.find('algorithm').text.lower()
    elements.append(algorithm)

    num_reads = root.find('num_reads').text.lower()
    try:
        num_reads = int(num_reads)
    except:
        ValueError("#Reads must be integer.")

    read_list = data_creation.data_creation(memory_size, num_reads)

    elements.append(read_list)

    return elements

if __name__ == "__main__":
    read_inputs()
