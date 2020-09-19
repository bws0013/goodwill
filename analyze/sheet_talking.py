

import gspread

from input import read_global_config

# The below 2 sheet variables are used store global config settings
SHEET_KEY = ''
SHEET_NAME = ''

# The below Format variable is used to determine if sheets formatting should be run. It will likely remain defaulted to True.
FORMAT = True

WS = None

def get_configs():
    local_config = read_global_config("sheet_talking")
    global SHEET_KEY
    global SHEET_NAME
    global FORMAT
    SHEET_KEY = local_config['sheet_key']
    SHEET_NAME = local_config['sheet_name']
    FORMAT = local_config['format']

def get_ws():
    gc = gspread.oauth()
    sh = gc.open_by_key(SHEET_KEY)
    ws = sh.worksheet(SHEET_NAME)
    global WS
    WS = ws

def get_all_data():
    get_configs()
    get_ws()
    return WS.get_all_values()

# print(get_all_data())
