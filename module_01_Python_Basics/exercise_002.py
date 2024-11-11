import re 

# Write your code below and press Shift+Enter to execute 

# What is the value of the variable a after the following code is executed?
a = "1" # "1"
print(a)

# What is the value of the variable b after the following code is executed?
b = "2" # "2"
print(b)

# What is the value of the variable c after the following code is executed?
c = a + b # "12"


# Consider the variable d use slicing to print out the first three elements:
d = "ABCDEFG"
d = d[0:3] # Or d[:3]
print(d)

# Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
e = e[::2]
print(e)

# Print out a backslash:
print("\\")

# Convert the variable f to uppercase:
f = "You are wrong"
f = f.upper()
print(f)

# Convert the variable f2 to lowercase:
f2 = "YOU ARE RIGHT"
f2 = f2.lower()
print(f2)

# Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
# g = g.find('snow')
# print(g)

# In the variable g, replace the sub-string Mary with Bob:
g = g.replace('Mary', 'Bob')
print(g)

# In the variable g, replace the sub-string , with .:
# g.replace(',','.') 

# In the variable g, split the substring to list:
# g.split()

# In the string s3, find the four consicutive digit character using \d and search() function:
s3 = "House number- 1105"
pattern = r"\d\d\d\d"

result = re.search(pattern, s3)
# Check if a match was found
if result:
    print("Digit found")
else:
    print("Digit not found.")


# In the string str1, replace the sub-string fox with bear using sub() function:
str1= "The quick brown fox jumps over the lazy dog."
# Write your code below and press Shift+Enter to execute
new_string = re.sub('fox', 'bear', str1)
print(new_string)


# In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
pattern = 'woo'
result = re.findall(pattern, str2 )
print(result)




