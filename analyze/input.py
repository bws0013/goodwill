

import glob
import csv
import yaml
import os
import re

from itertools import combinations

CONFIG_FILE_PATH = 'config.yaml'

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
