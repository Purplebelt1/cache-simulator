#File written my Monsour Sims

from input_reader import read_inputs
from cache_sim import cache_sim
from data_analysis import data_analysis

def main():

    main_data = read_inputs()

    post_read_list = cache_sim(*main_data)

    data_analysis(post_read_list)



main()

    