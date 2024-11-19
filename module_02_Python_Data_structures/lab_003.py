# Sets
# Casting a List to a Set
L = [ "Michael Jackson", 10.2, 1, 1, 2, 2, "a", "a"]
set_l = set(L) # The set function takes the List as an argument and transforms it into a set!
print(set_l)

set_l = {1, 2, 10.2, 'a', 'Michael Jackson'} # Sets don't have duplicate items

# Example 2
new_list = ['A','B','C','A','B','C']
new_list = set(new_list)
print(new_list)

# Add an Element to the Set
# Add the string 'D' to the set S.
S = {'A','B','C'}
S.add('D')
print(S)


# Intersection of Sets
# Find the intersection of set A and B.

A={1,2,3,4,5}
B={1,3,9, 12}
C = A.intersection(B)
print(C)
# or A & B

## Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)


# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)


# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)


# Set Operations 
# Let us go over set operations, as these can be used to change the set. Consider the set A:
# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# We can add an element to a set using the add() method: 
# Add element to set
A.add("NSYNC")
print(A)

#  If we add the same element twice, nothing will happen as there can be no duplicates in a set:
# Remove the element from set
A.remove("NSYNC")
print(A)

# We can verify if an element is in the set using the in command:
# Verify if the element is in the set
if "AC/DC" in A:
    print("AC/DC is in set A:", A)
else:
    print("Not found!")
# Sets Logic Operations
# Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:
# Consider the following two sets:

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
print(album_set1, album_set2)

# Find the intersections
intersection = album_set1 & album_set2
print(intersection)

# You can find all the elements that are only contained in album_set1 using the difference method:
# Find the difference in set1 but not set2
set_diff = album_set1.difference(album_set2) 
print(set_diff)

set_diff_2 = album_set2.difference(album_set1) 
print(set_diff_2)

# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2))

# Find the union of two sets
print(album_set1.union(album_set2))

# Check if superset
print(set(album_set1).issuperset(album_set2))

# Check if subset
print(set(album_set2).issubset(album_set1))   

# Here is an example where issubset() and issuperset() return true:
# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1) )

# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

