# Lab implementation in Vs code
# Title: - String Operations
# Assign string to variable

name = "Michael Jackson"
# Positive index
print(name[0])

# Negative index
# # Print the last element in the string
print(name[-1])

print(name[-13])

# printing the total lenght of the string
print(len(name))

# Slicing
# We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:

# Take the slice on variable name with only index 0 to index 3
print(name[0:4])

# Take the slice on variable name with only index 8 to index 11
print(name[8:12])


# Stride
print(name[::3])

# Get every second element. The elments on index 1, 3, 5 ...
print(name[::2])

# Get every second element in the range from index 0 to index 4
print(name[0:5:2])

# Duplicating a string
# Print the string for 3 times
a = 3 * "Michael Jackson \n"
print(a)

# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
print(name)

# Escape Sequence
# New line escape sequence
print("Michael Jackson \nis the best" )

# Tab escape sequence
print("Michael Jackson \t is the best" )

# Include back slash in string
print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string
o = 'king'
# Added the 'f' string to test if this was possible.
print(fr"Michael Jackson \ is the best and {o} of Pop. This is the place we added an 'r' before the text block" )

# Strings operation
# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("Before upper:", a)
# used the f string here
b = a.upper()
print(f"After upper: {b}")


# Convert all the characters in string to lower case
a = "MICHAEL JACKSON IS THE BEST"
print("Before lower:", a)
b = a.lower()
print("After lower:", b)

c = "PRINCE IS THE BEST"
print(f"Before lower: {c}")
d = c.lower()
print(f"After lower: {d}")

# The Replace method
a = "Michael Jackson is good"
b = a.replace('Michael', 'Janet')
print(b)

# Replace the old substring with the new target substring by removing some punctuations.
a = "Hello! Michael Jackson has: 12 characters."
print(a)
b = a.replace('!','').replace(':','').replace('.','')
print(b)

# The Find method
# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson"
f = name.find('el')
print(f)

# Find the substring in the string.
g = name.find('Jack')
print(g)

# If cannot find the substring in the string: -1
h = name.find('Jasdfasdasdf')
print(h)

# The method Split splits the string at the specified separator, and returns a list:
name = 'Michael Jackson'
split_string = name.split()
print(split_string)

