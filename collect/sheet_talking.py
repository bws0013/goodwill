

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

def sheet_append(rows):
    get_configs()
    get_ws()
    ws = WS
    if len(rows) == 0:
        print('> NO ROWS TO WRITE')
        return
    ws.append_rows(rows)
    preferred_format()

# Assumes all rows are of the same length
# Writes assuming there is no header row
def sheet_write(rows):
    get_configs()
    get_ws()
    ws = WS
    if len(rows) == 0:
        print('> NO ROWS TO WRITE')
        return

    # The range here surprisingly works even when you have multiple columns
    # I was finding the number of rows to use and their length but am not doing that if this works fine
    # range = 'A1:B'

    # I can investigate further at some point but I think setting the range to
    # `range = 'A1:B'` was working without specifying the true range but that
    # seems to not be the case anymore.

    elem_size = len(rows[len(rows) - 1])
    if elem_size > 26:
        print('> MORE THAN 26 COLUMNS REQUIRED, CANNOT WRITE TO SHEET')
        exit(1)

    letter = chr(ord('@')+elem_size)

    range = 'A1:' + letter

    ws.batch_update([{
        'range': range,
        'values': rows,
    }])

    preferred_format()

def preferred_format():
    if FORMAT == False:
        return
    freeze()
    sort_by_companies_and_date()

# Sorts by same pair of companies by date, my preferred sort
# Doesn't assume a header row exists therefore the header should be frozen.
def sort_by_companies_and_date():
    WS.sort((2, 'asc'), (3, 'asc'), (1, 'asc'))

def freeze():
    WS.freeze(1)

# sheet_list = sh.worksheets()

# print(sheet_list)

# get_configs()
# get_ws()
# sort_by_companies_and_date()
# ws = sh.worksheet("api-test")

# sort_by_companies_and_date(ws)
#

# rows = [['A1', 'B1'], ['A2', 'B2'], ['A3', 'B3']]
# sheet_write(rows)
# sheet_append(rows)

# write(ws, rows)
# freeze(ws)
# append(ws, rows)
