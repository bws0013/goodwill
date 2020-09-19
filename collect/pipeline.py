

from input import set_default_config

from collect_data import get_data_files
from files_to_data import parse_data_files

### collect_data get_data_files
# symbols = ['DKNG', "NET", "RTX", "LHX", "AAL", "JPM", "HAS", "AES", "JMIA", "PEP"]
# date = "20200619"
#
# get_data_files(symbols, date)

### files_to_data parse_data_files
# dir = './../data/20200617/'
# regex = '*'
#
# parse_data_files(dir, regex)

def run_all(symbols, dates):
    for date in dates:
        get_data_files(symbols, date)
        # clean_data() # This is an empty function in case you want to build out data cleaning
        parse_data_files(date)
    return

def select_config_file(filepath):
    set_default_config(filepath)

# TODO build out better data cleaning and validation
def clean_data():
    # I perform the minimum required data cleaning in files_to_data -> combos_to_data
    # If you wanted to perform other data cleaning you could build out that functionality and I have this call to be used for it.
    return

symbols = ['DKNG', "NET", "RTX", "LHX", "AAL", "JPM", "HAS", "AES", "JMIA", "PEP"]
dates = ['20200622', '20200623', '20200624', '20200625', '20200626']

run_all(symbols, dates)
