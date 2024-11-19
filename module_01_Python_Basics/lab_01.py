# Lab implementation in Vs code
# Title: Write your first Python Code!

# Try your first Python output
print('Hello, Python!')

# Check the Python Version
import sys
print(sys.version)

# Practice on writing comments
print('Hello, Prince learning python !') # This line prints a string
# print('Hi')

# ------------ Data Types in Python: Numbers (integers and floats) and Strings -------------
# Type of 12
print(type(12)) # Int

# Type of 2.14
print(type(2.14)) # float

# Type of "Hello, Python 101!"
print(type("Hello, Python 101!")) #Str

# Type of True
print(type(True)) # Boolean

# Type of False
print(type(False)) # Boolean

# --------- Converting from one type to another ( Casting )----------
# Convert 2 to a float
print(float(2))

# Convert a string into an integer
print(type(int('1')))

# Convert the string "1.2" into a float
print(type(float('1.2')))

# Convert an integer to a string
print(type(str(1)))

# Convert a float to a string
print(type(str(1.2)))

# Convert True to int
print(int(True)) # returns 1

# Convert 1 to boolean
print(bool(1)) # returns a True

# Convert 0 to boolean
print(bool(0))

# Convert True to float
float(True)

# ----------------- Expression and Variables ------------------
# Expressions

# Addition operation expression
print(43 + 60 + 16 + 41)

# Subtraction operation expression
print(50 - 60) 

# Multiplication operation expression
print(5 * 5)

# Division operation expression 1
print(25 / 5)

# Division operation expression 2
print(25 / 6)

# Integer division operation expression
print(25 // 5)

# Integer division operation expression
print(25 // 6) # We lose some values here


# Variables
# Just like with most programming languages, we can store values in variables, so we can use them later on.

# Store value into variable
x = 43 + 60 + 16 + 41
print(x)

# Use another variable to store the result of the operation between variable and value
y = x / 60
print(y)

# Overwrite variable with new value
x = x / 60
print(x)

# Name the variables meaningfully
total_min = 43 + 42 + 57 # Total length of albums in minutes
print(total_min)

# Name the variables meaningfully
total_hours = total_min / 60 # Total length of albums in hours 
print(total_hours)

# Complicate expression
total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
print(total_hours)

