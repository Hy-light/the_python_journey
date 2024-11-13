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


