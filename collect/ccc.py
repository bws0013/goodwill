

# No checks for length or other correctness are done here for the sake of keeping everything clean.
# The assumption here is that the data that comes in is clean.

import math
from input import read_global_config

# This sig_figs variable will be set at the global level
SIG_FIGS = 0

def get_configs():
    local_config = read_global_config("ccc")
    global SIG_FIGS
    SIG_FIGS = local_config['sig_figs']

def read_floats(filename):
    with open(filename) as f:
        return [float(x) for x in f]

def standard_deviation_of_ratios(x_input, y_input):
    ratios = []

    for i in range(len(x_input)):
        ratios.append(x_input[i] / y_input[i])

    return standard_deviation(ratios)

def standard_deviation(values):
    diff_sq = diff_sq_calc(values)
    variance = diff_sq / len(values)
    return math.sqrt(variance)

def diff_sq_calc(values):
    diff_sq_total = 0
    total = 0
    mean = 0

    for v in values:
        total += v

    mean = total / len(values)
    # print("MEAN:", mean)

    for v in values:
        diff_sq_total += (v - mean) * (v - mean)

    # print("SUM OF DIFFERENCE:", diff_sq_total)

    return diff_sq_total

def deviation(x_vals, y_vals):
    total = 0

    total_x = 0
    mean_x = 0

    total_y = 0
    mean_y = 0

    for v in x_vals:
        total_x += v

    for v in y_vals:
        total_y += v

    mean_x = total_x / len(x_vals)
    mean_y = total_y / len(y_vals)

    for v in range(len(x_vals)):
        total += (x_vals[v] - mean_x) * (y_vals[v] - mean_y)

    # print("DEVIATION SCORE:", total)
    return total

def r_calc(x_vals, y_vals):
    deviation_score = deviation(x_vals, y_vals)
    diff_sq_x = diff_sq_calc(x_vals)
    diff_sq_y = diff_sq_calc(y_vals)

    # The below may be more efficient with large numbers but it produces ugly (.9999...) results so for now I will not use it
    # temp = math.sqrt(diff_sq_x) * math.sqrt(diff_sq_y)

    temp = math.sqrt(diff_sq_x * diff_sq_y)

    r = deviation_score / temp
    # print("r:", r)
    return r

def r_squared(r):
    r_sq = r * r
    # print("r^2:", r_sq)
    return r_sq

def get_all(x_vals, y_vals):
    get_configs()

    r = round(r_calc(x_vals, y_vals), SIG_FIGS)
    r_2 = round(r_squared(r), SIG_FIGS)
    sd = round(standard_deviation_of_ratios(x_vals, y_vals),SIG_FIGS)

    return "{},{},{}".format(r, r_2, sd)

####################################################
# HOW TO ADD YOUR OWN FUNCTION AND ADD IT TO YOUR DB
# This is an explanation of how you would add you own function
#
# I am going to assume you only want to add it into sheets, if you are using
# something different you will need to adjust your schema accordingly
#
# Our new function takes in a list of numbers and adds them, it is an example after all.
# This code is not optimized and has lots excesive comments
#
# First, make a method or uncomment lines 108 through 112
#
# def add_list_of_numbers(list_of_numbers):
#     sum_total = 0 # Create a variable to store our total
#     for number in list_of_numbers: # Iterate over each number in our list
#         sum_total = sum_total + number # Add our number to the current total
#     return sum_total # Return our total
#
# We now have a function that adds all of numbers on our list
# Next we  need to modify the existing get_all function to allow us to pass data to it
#
# First comment out the get_all function on lines 88-94
# For the sake of example we will assume we want to get the sum of our X values
# To do this we first need to collect the output of the function
# One collected we need to modify the output format to account for our new values
#
# Uncomment lines 124-132 to get our new method
#
# def get_all(x_vals, y_vals):
#
#     r = round(r_calc(x_vals, y_vals), SIG_FIGS) # Unchanged
#     r_2 = round(r_squared(r), SIG_FIGS) # Unchanged
#     sd = round(standard_deviation_of_ratios(x_vals, y_vals),SIG_FIGS) # Unchanged
#
#     sum = add_list_of_numbers(x_vals) # New
#
#     return "{},{},{},{}".format(r, r_2, sd, sum) # Modified
#
# Note that we created a variable that stores our returned value
# We also changed the return value to format with our new variable in mind
# If we run the main program to send data to sheets it should now have our new column
#
# Optionally we could still change is the headers in files_to_data.py to account for this
# I won't be doing that but our new header can be seen in the next line
#
# header = ['DATE','COMPANY 1','COMPANY 2','r VALUE','r^2 VALUE','SD','Sum Total']
#
# You have now extended the functionality of this application.
#
# The end.
