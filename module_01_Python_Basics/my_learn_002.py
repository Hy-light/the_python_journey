# Check for Python version
import sys

print(sys.version)
print(sys.float_info)

# get the total hours
total_min = 43 + 42 + 57
total_hr = total_min / 60
print(total_hr)

# using a function to do this with one argument 'x'
'''
def get_total_hr(x):
    total_min = x
    total_hr = total_min / 60
    return total_hr

print(get_total_hr(6789))
'''

# Getting the total minutes during runtime
def get_total_hr():
    x = input('What is the total number of minutes you want to convert to hour? \n')
    total_hr = int(x) / 60
    return total_hr

print(get_total_hr())

