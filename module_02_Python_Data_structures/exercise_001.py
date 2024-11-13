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



# ----------------- Set --------------------------------
# Convert the list ['rap','house','electronic music', 'rap'] to a set:
my_set = set(['rap','house','electronic music', 'rap'])
print(my_set)

# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))
sum_A_B = sum(A) == sum(B)
print(sum_A_B)

# Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
print(album_set3)


# Find out if album_set1 is a subset of album_set3:
print(album_set1.issubset(album_set3))


# ----------------- Dictionaries -------------------
# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic)

# In the dictionary soundtrack_dic what are the keys ?
dic_keys = soundtrack_dic.keys()
print(dic_keys)

# In the dictionary soundtrack_dic what are the values ?

dic_values = soundtrack_dic.values()
print(dic_values)

# Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values. 
# Write your code below and press Shift+Enter to execute
album_sales_dict = { "Back in Black":50, "The Bodyguard":50, "Thriller":65}
print(album_sales_dict)

# Use the dictionary to find the total sales of Thriller:
print(album_sales_dict["Thriller"])

# Find the names of the albums from the dictionary using the method keys()
print(album_sales_dict["Thriller"])

# Find the values of the recording sales from the dictionary using the method values:
print(album_sales_dict.values())



