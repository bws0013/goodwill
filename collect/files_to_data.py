

# Very important file here. Given the set of combinations take each set of data validate that its valid and then take the r and r^2 value and add it to a list to be compared with others and provide stats such as dates.

# Ideally we want to keep ccc.py as untouched as possible, thats the math, this is the application. We can (and should) call on its functions.

# Once this has been created the expectation is that hundreds to thousands of combinaitaions can be quickly tested for correlation, there may need to be a threshhold built in to account for low amounts but this should be done in a config file rather than specifically here, though I will probably implement it here for now.

from itertools import combinations

from input import read_global_config, get_files_in_dir, get_floats_from_file
from ccc import read_floats, get_all
from sheet_talking import sheet_write, sheet_append

# The below 2 variables are to be set by a global config
APPEND = False
USE_HEADER = False

# These last used variables are used as a cache mechanism
LAST_USED_NAME = ''
LAST_USED_DATA = ''

DATA_PATH = ''

def get_configs():
    local_config = read_global_config("files_to_data")
    global APPEND
    global USE_HEADER
    global DATA_PATH
    global REGEX
    APPEND = local_config['append']
    USE_HEADER = local_config['use_header']
    DATA_PATH = local_config['data_path']
    REGEX = local_config['regex']

def get_security_name_from_combo_name(name):
    components = name.split("/")
    last = components[len(components) - 1]
    return last[:-4]

def combos_to_data(combos):

    header = ['DATE','COMPANY 1','COMPANY 2','r VALUE','r^2 VALUE','SD']

    output_list = []
    if USE_HEADER == True:
        output_list.append(header)

    for c in combos:

        x_name = get_security_name_from_combo_name(c[0])
        y_name = get_security_name_from_combo_name(c[1])

        x_input = []
        y_input = []

        global LAST_USED_NAME
        global LAST_USED_DATA

        if x_name == LAST_USED_NAME:
            x_input = LAST_USED_DATA
        else:
            LAST_USED_NAME = x_name
            x_input = get_floats_from_file(c[0])
            LAST_USED_DATA = x_input

        # x_input = get_floats_from_file(c[0])
        y_input = get_floats_from_file(c[1])

        if len(x_input) != len(y_input):
            print("> SIZE DIFFERENCE")
            print(x_name)
            # print(x_input)
            print(y_name)
            # print(y_input)
            exit(1)
        x_name_partial = x_name.split("_")
        y_name_partial = y_name.split("_")

        # Quick debug uncomment line below
        # print(x_name, y_name)

        output = get_all(x_input, y_input)

        # print(x_name_partial[1], x_name_partial[0], y_name_partial[0], output, sep=",")

        output_line = "{},{},{},{}".format(x_name_partial[1], x_name_partial[0], y_name_partial[0], output)
        # print(output_line)

        output_list.append(output_line.split(','))
    return output_list

def send_to_db(rows_to_write, db='sheets'):
    if db == 'sheets':
        if APPEND == True:
            sheet_append(rows_to_write)
        else:
            sheet_write(rows_to_write)
    else:
        print('> NO DATABASE FOUND FOR THIS OPTION:', db)

def parse_data_files(date):
    get_configs()
    # print(REGEX)
    # print(DATA_PATH)
    files = []
    try:
        files = get_files_in_dir(DATA_PATH + date, REGEX)
    except:
        print("> NO FILES FOUND IN BELOW DIRECTORY")
        print(">", DATA_PATH + date)
        print("> Make sure this path exists and make sure the data path config ends with a '/'")
        exit(3)
    combos = combinations(files, 2)
    data_to_write = combos_to_data(combos)
    send_to_db(data_to_write)

#### The below can be used to run a local test
# date = '20200420'
# parse_data_files(date)

#### OLD The below can be used to run a local test
# dir = './../data/20200420'
# regex = "(aapl.*|ba.*|cost.*)"
#
# parse_data_files(dir, regex)
