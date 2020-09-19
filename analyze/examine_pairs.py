

from input import read_global_config
from sheet_talking import get_all_data

HEADER = [] # Header for the data
ALL_DATA = [] # All of the data with a header removed

SIG_FIGS = 0

def get_configs():
    local_config = read_global_config("examine_pairs")
    global SIG_FIGS
    SIG_FIGS = local_config["sig_figs"]

# TODO determine if this is way over-engineered
# Find the average value of a column for each pair
# Takes in a column to take the average of and a list of columns to use as the key
# Assumes that the data has been sorted by the key_columns
def find_average_of_col(val_column=4, key_columns=[1,2]):
    get_configs()

    key_to_val = {} # Will contain the key and the value

    current_val = 0
    current_count = 0
    current_key = ''
    for row in ALL_DATA:
        compare_key = ''
        for key in key_columns:
            compare_key += row[key] + ','
        compare_key = compare_key[:-1] # Remove last comma

        if compare_key == current_key:
            current_val += float(row[val_column])
            current_count += 1
        else:
            if current_count > 0:
                current_val /= current_count
                key_to_val[current_key] = round(current_val, SIG_FIGS)
                current_val = 0
                current_count = 0
            current_key = compare_key
    return key_to_val

def get_data():
    data = get_all_data()
    if len(data) <= 1:
        print("> 1 OR FEWER ROWS OF DATA FOUND, PRINTING")
        print(data)
        print("> DATA PRINTED")

    global HEADER
    global ALL_DATA

    if data[0][0] == 'DATE':
        HEADER = data[0]
        data = data[1:]
    ALL_DATA = data

def get_sorted_dict_by_val(dict):
    all_tuples = []
    for key in dict:
        all_tuples.append([key, dict[key]])
    all_tuples.sort(key=lambda tup: tup[1])
    for tuple in all_tuples:
        print(tuple)

get_data()
key_to_val = find_average_of_col(3)

get_sorted_dict_by_val(key_to_val)

# print(key_to_val.items())

# {k: v for k, v in sorted(key_to_val.items(), key=lambda item: item[1])}
