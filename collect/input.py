

import glob
import csv
import yaml
import os
import re

from itertools import combinations

CONFIG_FILE_PATH = 'collect_config.yaml'

# This method will read the global config yaml file
def read_global_config(config_name):
    with open(CONFIG_FILE_PATH, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    # for section in cfg:
    #     print(section)
    return(cfg[config_name])

def set_default_config(filepath):
    global CONFIG_FILE_PATH
    CONFIG_FILE_PATH = filepath

# get_files_in_dir("./../data/", "*.csv")
def get_files_in_dir(dir, regex):
    # Complex line but to break it down into steps
    # 1) List the files in dir
    # 2) Get a list of filenames that match the regex
    # 3) Add the dir name to the start of each filename in the list
    # 4) Return the list of file names in the format dir/filename
    return [dir + '/' + f for f in os.listdir(dir) if re.search(r'{}'.format(regex), f)]

# Given some csv files get the pricing data we care about
def read_csv_file(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print("date,marketAverage") # If we want to include headers
                line_count += 1
                continue
            if row["marketAverage"] == '':
                # print("> MISSING AVERAGE")
                continue
            print(row["date"], row["marketAverage"],row["symbol"], sep=',')
            # print(row["marketAverage"])

def get_floats_from_file(filename):
    with open(filename, mode='r') as csv_file:
        float_list = []
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        last = '0'
        for row in csv_reader:
            if line_count == 0:
                # print("date,marketAverage") # If we want to include headers
                line_count += 1
                continue
            if row["marketAverage"] == '':
                # print("> MISSING AVERAGE IN", filename)
                # print("> REPLACING WITH LAST NUMBER USED")
                float_list.append(last)
                continue
            float_list.append(row["marketAverage"])
            last = row["marketAverage"]

        list_loc = len(float_list) - 1
        while list_loc >= 0 :
            if float_list[list_loc] != '0':
                last = float_list[list_loc]
            else:
                float_list[list_loc] = last
            list_loc -= 1

        return [float(x) for x in float_list]


# vars = read_global_config("ccc")
# print(vars['sig_figs'])

# all = get_floats_from_file("./../data/20200617/has_20200617.csv")
#
# for a in all:
#     print(a)

# dir = './../data/20200424/'
# reg = '*'
#
# files = get_files_in_dir(dir, reg)
# print(files)
#
# combos = combinations(files, 2)
# for c in list(combos):
#     print(c)
