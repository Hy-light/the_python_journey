# Tuples in Python

# Create your first tuple
tuple1 = ("disco",10,1.2 )
print(tuple1)

# Print the type of the tuple you created
print(type(tuple1))

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Use negative index to get the value of the last element
print(tuple1[-1])

# Use negative index to get the value of the second last element
print(tuple1[-2])

# Use negative index to get the value of the third last element
print(tuple1[-3])

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Slice from index 0 to index 2
print(tuple2[0:3])

# Slice from index 3 to index 4, we obtain the last two elements of the tuple
print(tuple2[3:5])

# Get the length of tuple
print(len(tuple2))

# Sorting 
# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple, and save to a new tuple
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# Create a nest tuple
# Each element in the tuple, including other tuples, can be obtained via an index
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4], "\n")

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples, i.e. r in "rock"
print(NestedT[2][1][0])

# Print the second element in the second nested tuples, i.e. o in rock
print[NestedT[2][1][1]]

# Print the first element in the second nested tuples
print(NestedT[4][1][0])

# Print the second element in the second nested tuples
print(NestedT[4][1][1])
