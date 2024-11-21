# Comparison Operations
# Find the value of i that produces a True:
i = 1
i != 0
if i == 1:
    print(True)
else:
    print(False)

# Branching

# Find the value of x that prints the statement "this is a":
x = 'a'
if(x=='a'):
    print("this is a")
else:
    print("this is  not a")

# Logic Operators
# Find the value of y that produces a True statement:
y = 0 
x = 1
z = x > 0 and y < 10
print(z)

# If statement example

age = 19
# age = 18
#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("Hey, you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("Move on!")

# Condition statement example

album_year = 1983
if not (album_year == 1984):
    print ("Album year is not 1984")