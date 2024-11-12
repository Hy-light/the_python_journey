# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
print(genres_tuple)

# find the length of the tuple, genres_tuple:
print(len(genres_tuple))

# Access the element, with respect to index 3:
e_3 = genres_tuple[3]
print(e_3)

# Use slicing to obtain indexes 3, 4 and 5:
print(genres_tuple[3:6])

# Find the first two elements of the tuple genres_tuple:
print(genres_tuple[0:2])

# Find the first index of "disco":
in_disco = genres_tuple.index("disco")
print(in_disco)

# Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
C_tuple=(-5, 1, -3)
sorted_Tuple = sorted(C_tuple)
print(sorted_Tuple)



# -------------------- List ----------------------------
# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
a_list = [1, 'hello', [1,2,3], True]
print(a_list)

# Find the value stored at index 1 of a_list.
print(a_list[1])

# Retrieve the elements stored at index 1, 2 and 3 of a_list.
print(a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a'] 
B = [2, 1, 'd']
C = A + B
print(C)




