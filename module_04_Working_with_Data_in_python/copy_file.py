# -------------------------- Copy a File --------------------------
# Let's copy the file Example2.txt to the file Example3.txt
# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())


'''
After reading files, we can also write data into files and save them in different file formats like .txt, .csv, .xls (for excel files) etc. You will come cross these in further examples

'''