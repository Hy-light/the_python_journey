# Loops

squares = ['red_square', 'yellow_square', 'Green_square', 'Purple_square', 'Blue_square']

'''
for i in range(0,5):
    squares[i] = 'white'
    print('Changing square', squares[i])    
print(squares)
'''

# Looping through every item in the squares list and changing them into white
for  i in range(len(squares)):
    # print('Changing', i, ' to white')
    print(squares[i])
    print('Changing', squares[i], ' to white')
    squares[i] = 'white'
print(squares)


# The enumerate function()
fruits = ['Bananas', 'Oranges', 'Apples']
for i, fruit in enumerate(fruits):
    print('Fruit', i, ' is', fruit)
    # print(i)


# simple while loop
x = 3
y = 1

while(y != x):
    print(y)
    y += 1

# For loop example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i]) 

# Example of for loop
for i in range(0, 8):
    print(i)

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

#  We can access the index and the elements of a list as follows: 
# Loop through the list and iterate on both index and element value, we use the enumerate function

squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    # print(i, square)
    print('Square at index', i, ' is', square)


# While loop
count = 1
while count <= 5:
    print(count)
    count += 1

'''
In this example, the condition count <= 5 is checked before each iteration. 
As long as count is less than or equal to 5, the code block inside the loop is executed. 
After each iteration, the value of count is incremented by 1 using count += 1. 
Once count reaches 6, the condition becomes false, and the loop stops.

Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. 
This can be done with the following block of code:
'''
# While Loop Example

dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[i]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    
print("It took ", i ,"repetitions to get out of loop.")