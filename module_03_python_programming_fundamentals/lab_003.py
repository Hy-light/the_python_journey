# Functions 
def noWork():
    pass
noWork()

# Complete the function  f so that it returns the product of a and b. Use the next cell to test the function
def f(a,b):
    return a * b

print(f(2,3))

# Test the function using the next cell
a = 4
b = 2

if a * b == f(a,b):   
    print("Correct.")   
else:    
    print("Incorrect.")

# Complete the function g such that the input c is a list of integers and the output is the sum of all the elements in the list.
def g(c):
    return sum(c)

c = [1,2,3,4,5]

if sum(c) == g(c):   
    print("Correct.")   
else:    
    print("Incorrect.")

# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Replicate string by multiplying with an integer
# Use mult() multiply two different type values together

replicate_integer = Mult(2, "Michael Jordan ")
print(replicate_integer)

# If there is no return statement, the function returns None. The following two functions are equivalent:
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See what functions returns are
print(MJ())
print(MJ1())

# Pre-defined functions
# The print() function:

# Built-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# The sum() function adds all the elements in a list or tuple:

# Use sum() to add every element in a list or tuple together
sum_album_ratings = sum(album_ratings)
print(sum_album_ratings)

# The len() function returns the length of a list or tuple:
print(len(album_ratings))

# In-Built functions
# In Python, an in-built function is a pre-defined function that is always available for use, providing common functionality without requiring any imports.

# Define a tuple
a = (1, 2)
# Pass the tuple to the sum function and store the result in a variable
c = sum(a)
# Print the result
print(f"The sum of the elements in the tuple {a} is {c}.")

# Define a list
a = [1, 2]
# Pass the list to the sum function and store the result in a variable
c = sum(a)
# Print the result
print(f"The sum of the elements in the list {a} is {c}.")

"""
Using if/else Statements and Loops in Functions
The return() function is particularly useful if you have any IF statements in the function, when you want your output to be dependent on some condition
"""
# Function example
def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
y = type_of_album("Franklin Edwards", "The Definition", 2009)
print(x)
print(y)

# We can use a loop in a function. For example, we can <code>print</code> out each element in a list:
# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])

"""
String comparison in Functions
The relational operators compare the Unicode values of the characters of the strings from the zeroth index till the end of the string. 
It then returns a boolean value according to the operator used
"""
#Compare Two Strings Directly using in operator
# add string
string = "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operator to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

print(check_string("Michael Jackson is the best"))

"""
This program uses a user-defined function named compareStrings() to compare two strings.
This function receives both strings as its argument and returns 1 if both strings are equal using == operator
"""
#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x == y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check == 1:
    print("\nString Matched")
else:
    print("\nString not Matched")

"""
Count the Frequency of Words Appearing in a String Using a Dictionary.
Find the count of occurence of any word in our string using python. 
This is what we are going to do in this section, count the number of word in a given string and print it.
Lets suppose we have a ‘string’ and the ‘word’ and we need to find the count of occurence of this word in our string using python. 
This is what we are going to do in this section, count the number of word in a given string and print it.
The first thing, we will do is define a function and and then create a list that will be empty initially.
Next, we will add a code to convert the string to a list. Python string has a split() method. It takes a string and some separator to return a list.
Now we will declare an empty dictionary.
Next we will add code using for loop to iterate the words and value will will count the frequency of each words in the string and store them to the dictionary.
Finally we will print the dictionary.
"""
# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

"""
Setting default argument values in your custom functions
You can set a default value for arguments in your function. 
For example, in the isGoodRating() function, what if we wanted to create a threshold for what we consider to be a good rating? 
Perhaps by default, we should have a default rating of 4:
"""
# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input

isGoodRating()
isGoodRating(10)
