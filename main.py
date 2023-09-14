from input_reader import read_inputs
from cache_sim import cache_sim

def main():

    main_data = read_inputs()

    cache_sim(*main_data)


main()

    