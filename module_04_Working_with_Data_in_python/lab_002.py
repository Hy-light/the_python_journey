# Write and save files in python

'''
Writing Files
We can open a file object using the method write() to save the text file to a list. To write to a file, the mode argument must be set to w. Let’s write a file Example2.txt with the line: “This is line A”
'''

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")


# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# We can write multiple lines:

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    

with open(exmp2, 'r') as writefile:
    print(writefile.read())

'''
The method .write() works similarly to the method .readline(), except instead of reading a new line it writes a new line. The process is illustrated in the figure. The different colour coding of the grid represents a new line added to the file after each method call.
'''

# We write a list to a .txt file as follows:
# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# However, note that setting the mode to w overwrites all the existing data in the file
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


'''
Appending Files
We can write to files without losing any of the existing data as follows by setting the mode argument to append: a. You can append a new line as follows:
'''
# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    testwritefile.write("Prince\n")

# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


'''
Additional modes

It's fairly inefficient to open the file in a or w and then reopen it in r to read any lines. Luckily we can access the file in the following modes:

    r+ : Reading and writing. Cannot truncate the file.
    w+ : Writing and reading. Truncates the file.
    a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

Let's try out the a+ mode:

'''
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

'''
There were no errors but read() also did not output anything. This is because of our location in the file.

Most of the file methods we've looked at work in a certain location in the file. .write() writes at a certain location in the file. .read() reads at a certain location in the file and so on. You can think of this as moving your pointer around in the notepad to make changes at a specific location.

Opening the file in w is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows. Whereas opening the file in a is similar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text.
It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -

    .tell() - returns the current position in bytes
    .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to the beginning, relative to current position and end

'''

# Now lets revisit a+
with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing by me...') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )


'''
Finally, a note on the difference between w+ and r+. Both of these modes allow access to read and write methods; however, opening a file in w+ overwrites it and deletes all pre-existing data.
To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
In the following code block, Run the code as it is first and then run it with the .truncate().
'''

with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    print(data)
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished...\n")
    #Uncomment the line below
    # testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())


# -------------------------- Copy a File --------------------------
# Let's copy the file Example2.txt to the file Example3.txt
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
