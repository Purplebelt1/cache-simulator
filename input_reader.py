# File written by Monsour Sims

import xml.etree.ElementTree as ET
import data_creation
import math

def conversion_to_decimal(x):
    # Extract the last two characters from the input string to determine the byte level (e.g., "BT", "KB", "MB", "GB")
    byte_level = x[-2:]

    # Convert the byte level abbreviation to the corresponding multiplier value
    if byte_level == "bt":
        byte_level = 1  # Byte
    elif byte_level == "kb":
        byte_level = 2**10  # Kilobyte (2^10 bytes)
    elif byte_level == "mb":
        byte_level = 2**20  # Megabyte (2^20 bytes)
    elif byte_level == "gb":
        byte_level = 2**30  # Gigabyte (2^30 bytes)
    else:
        # Raise a ValueError if the byte level abbreviation is not recognized
        raise ValueError("Sizes must be in BT, KB, MB, or GB")
    
    # Extract the numeric part of the input string and convert it to an integer
    numeric_part = int(x[:-2])

    # Calculate the total size by multiplying the numeric part with the byte level multiplier
    total_size = int(numeric_part * byte_level)

    return total_size


def read_inputs():
    # Parse the XML configuration file located at './config.xml'
    tree = ET.parse('./config.xml')
    root = tree.getroot()
    
    elements = []

    # Read and convert memory size from the XML file
    memory_size = root.find('memory_size').text.lower()
    memory_size = conversion_to_decimal(memory_size)
    if not math.sqrt(memory_size).is_integer():
        ValueError("Memory size must be a power of 2")

    # Read and convert page size from the XML file
    page_size = root.find('page_size').text.lower()
    page_size = conversion_to_decimal(page_size)
    if not math.sqrt(page_size).is_integer():
        ValueError("Page size must be a power of 2")

    # Check if the page size is applicable to the memory size
    if memory_size % page_size != 0:
        raise ValueError("Page size not applicable to current memory size")

    # Check if the memory size is divisible by the page size
    if (memory_size / page_size) % 2 != 0:
        raise ValueError("Memory size must be divisible by page size")
    
    elements.append(memory_size)
    elements.append(page_size)

    # Read and convert cache size from the XML file
    cache_size = root.find('cache_size').text.lower()
    cache_size = conversion_to_decimal(cache_size)
    if not math.sqrt(cache_size).is_integer():
        ValueError("cache size must be a power of 2")
    elements.append(cache_size)

    # Read the cache mapping type from the XML file
    mapping_type = root.find('mapping_type').text.lower()
    elements.append(mapping_type)

    # Read and process the value of 'k' from the XML file
    k = root.find('k').text.lower()

    if k == "null" or mapping_type != "set-associative":
        if mapping_type == "direct":
            k = cache_size / page_size
        elif mapping_type == "associative":
            k = 1
        elif mapping_type == "set-associative":
            raise ValueError("Can't set 'k' to Null if set associative is the mapping type.")
    else:
        try:
            k = int(k)
            if not math.sqrt(k).is_integer():
                ValueError("k must be a power of 2")
        except:
            raise ValueError("K must be an integer")
        if cache_size / page_size < int(k):
            raise ValueError("k must be less than the number of lines")
        
    elements.append(k)  

    # Read and convert the replacement algorithm from the XML file
    algorithm = root.find('replacement_algorithm').text.lower()
    elements.append(algorithm)

    # Read and convert the number of reads from the XML file
    num_reads = root.find('num_reads').text.lower()
    try:
        num_reads = int(num_reads)
    except:
        raise ValueError("#Reads must be an integer.")

    # Create a list of read items based on memory size and the specified number of reads
    read_list = data_creation.data_creation(memory_size, num_reads)

    elements.append(read_list)

    return elements

if __name__ == "__main__":
    read_inputs()
