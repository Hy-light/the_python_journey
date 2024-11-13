# List

# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)

# We can use negative and regular indexing with a list:
# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# List Content
# Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. The same indexing conventions apply for nesting:
# Sample List
L = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# List slicing
print(L[3:5])

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# Another similar method is append. If we apply append instead of extend, we add one element to the list:
# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

hr = 'hard rock'.split()
print(hr)

# Split the string by comma
L_a = 'A,B,C,D'.split(',')
print(L_a)

# Copy and Clone List
# When we set one variable B equal to A, both A and B are referencing the same list in memory:

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
print(B)

# Now if you change A, B will not change: 
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
