# File written by William DeBlieck

def append_to_txt_file(filename, input_list):
    # Convert the input list to a comma-separated string
    new_line = '\n'.join(map(str, input_list)) + '\n'
    # Open the file in append mode ('a+'), which creates the file if it doesn't exist
    with open(filename, 'a+') as file:
        file.write(new_line)
        file.close()

def write_to_txt_file(filename, input_list):
    # Convert the input list to a comma-separated string
    new_line = '\n'.join(map(str, input_list)) + '\n'
    # Open the file in write mode ('w'), which overwrites the file if it exists
    with open(filename, 'w') as file:
        file.write(new_line)
        file.close()