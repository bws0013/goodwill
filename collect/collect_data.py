

import requests
import pathlib
import datetime
import os

from input import read_global_config

# This token variable will be set at the global level
TOKEN = ''

# The below are constants that aren't likely to change
# The url contains a hardcoded token but this should be changed to use the above token
DATA_PATH = ''

BASE_URL = 'https://cloud.iexapis.com/stable/stock/<SYMBOL>/intraday-prices?token=<TOKEN>&format=csv&exactDate=<DATE>'

def get_configs():
    local_config = read_global_config("collect_data")
    global TOKEN
    global DATA_PATH
    TOKEN = local_config['token']
    DATA_PATH = local_config['data_path']

def replace_in_string(input, old_text, new_text):
    if input.count(old_text) > 1:
        print("> Multiple parts to change in string, use a different method.")
        print("> Input:", input)
        print("> Text to change:", old_text)
        exit(1)
    input = input.replace(old_text, new_text)
    return input

def replace_base_url(symbol, date):

    local_url_copy = BASE_URL
    local_url_copy = replace_in_string(local_url_copy, "<SYMBOL>", symbol.lower())
    local_url_copy = replace_in_string(local_url_copy, "<TOKEN>", TOKEN)
    local_url_copy = replace_in_string(local_url_copy, "<DATE>", date)
    return local_url_copy

def get_file_name(symbol, date):
    symbol = symbol.lower()
    return symbol + '_' + date + '.csv'

def does_file_exist(filepath):
    file = pathlib.Path(filepath)
    if file.exists ():
        return True
    else:
        return False

def get_csv_from_iex(url, filepath):
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')

        with open(filepath, "w") as file:
            file.write(decoded_content)

def get_day_format(date):
    return start_date.strftime("%Y") + start_date.strftime("%m") + start_date.strftime("%d")

def get_file_for_one_day(symbol, date):
    csv_url = replace_base_url(symbol, date)
    filepath = DATA_PATH + date + '/' + get_file_name(symbol, date)
    if does_file_exist(filepath):
        print("> FILE EXISTS")
        print(filepath)
        return
    get_csv_from_iex(csv_url, filepath)
    print("> Day Done: " + date)

def get_companies_for_one_day(symbols, date):
    for s in symbols:
        get_file_for_one_day(s, date)
    return

def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Unable to crate directory %s, it may already exist" % path)
    else:
        print ("Created directory %s " % path)

def get_data_files(symbols, date):
    get_configs()
    create_dir(DATA_PATH + date)
    get_companies_for_one_day(symbols, date)


### The below can be used to run a local test
# symbols = ['DKNG', "NET", "RTX", "LHX", "AAL", "JPM", "HAS", "AES", "JMIA", "PEP"]
# date = "20200619"
#
# get_data_files(symbols, date)



#### The below is not necessary to test
# DATA_PATH += date + "/"
# start_date = datetime.datetime(2019, 4, 2)

# create_dir(DATA_PATH)

# get_companies_for_one_day(symbols, date)

# x = get_n_weekdays(10, date)
# print(x)

# SYMBOL='aapl'
# DATE='20200424'
# get_file_for_one_day(SYMBOL, DATE)
