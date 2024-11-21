# Uncomment these if working locally, else let the following code cell run.

import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Download Example file
# !wget Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt


# # Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")

print(file1.name)
print(file1.mode)

# Reading the file context
FileContent = file1.read()
print(FileContent)

# type of file content
print(type(FileContent))

# # Close file after finish
file1.close()

'''
A Better Way to Open a File¶

Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.
'''
# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
print(file1.closed)

# We don’t have to read the entire file, for example, we can read the first 4 characters by entering three as a parameter to the method .read():
# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))


# Once the method .read(4) is called the first 4 characters are called. If we call the method again, the next 4 characters are called. The output for the following cell will demonstrate the process for different inputs to the method read():

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# We can also read one line of the file at a time using the method readline():

## Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

# We can also pass an argument to  readline() to specify the number of charecters we want to read. However, unlike  read(),  readline() can only read one line at most.
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# We can use a loop to iterate through each line:
with open(example1, 'r') as file1:
    i = 0
    for line in file1:
        print('Iteration', str(i), ': ', line)
        i = i + 1


# We can use the method readlines() to save the text file to a list:
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# print the entire list
print(FileasList)

# print the first line 
print(FileasList[0])
# print the second line
print(FileasList[1])
# print the third line
print(FileasList[2])

