# 1. There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. 
# They want to know who was born in a leap year. 
# Write an if-else statement to determine who was born in a leap year.

Annie_age = 1996 
Jane_age = 1996

if (Annie_age%4 == 0) and (Jane_age%4 == 0):
    print("...both Annie and Jane were born in a leap")
elif (Annie_age%4 == 0):
    print("Annie was born in a leap")
elif (Jane_age%4 == 0):
    print("Jane was born in a leap")
else:
    print("None was born in a leap year")


# 2. In a school canteen, children under the age of 9 are only given milk porridge for breakfast. 
# Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger. 
# The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10. 
# Use if-else statement to determine what the canteen master will offer to him.
age = 10
if (age <= 9 ):
    print("You will have milk porridge for breakfast")
elif (age >= 10 ) and (age <= 14 ):
    print("You will have sandwich for breakfast")
elif (age >= 15 ) and (age <= 17 ):
    print("You will have burger for breakfast")
else:
    print("You are not covered")



# ----------------------- loops -----------------------
# Use loops to print out the elements in the list A:
A = [3,4,5]
for item in A:
    print('...printing', item)


# While Loops
# Find the value of  x that will print out the sequence  1,2,..,10 :
x = 11
y = 1
while(y != x):
    print(y)
    y += 1


# Loops exercises
# Write a for loop the prints out all the element between -5 and 5 using the range function.

for i in range(-5, 5):
    print(i)

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.
Genres = [ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print(genre)


# Write a for loop that prints out the following list:
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)


# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
# If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
score = PlayListRatings[i]

while (i < len(PlayListRatings) and score >= 6):
    print(score)
    i += 1
    score = PlayListRatings[i]


# Write a while loop to copy the strings 'orange' of the list squares_1 to the list new_squares_1. 
# Stop and exit the loop if the value on the list is not 'orange':

squares_1 = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares_1 = []
i = 0

while (i < len(squares_1) and squares_1[i] == 'orange'):
    new_squares_1.append(squares_1[i])
    i += 1
    print(new_squares_1)

'''
Some real-life problems!¶
Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. 
Help him memorise both the tables by printing them using for loop.
'''
# for loop for table 6
for i in range(13):
    xpl = i * 6
    print('6 *', i, 'is = ', xpl )

for i in range(13):
    xpl = i * 7
    print('7 *', i, 'is = ', xpl )


'''
The following is a list of animals in a National Zoo. Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
Your brother needs to write an essay on the animals whose names are made of 7 letters. 
Help him find those animals through a while loop and create a separate list of such animals.
'''

'''
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
Animal_7_letters = []
i = 0

while (i < len(Animals) and len(Animals[i]) == 7):
    Animal_7_letters.append(Animals[i])
    i += 1
    print('Animals made up of seven are: ',Animal_7_letters)
'''

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
Animal_7_letters = []
i = 0
while (i < len(Animals)):
    if len(Animals[i]) == 7:
        Animal_7_letters.append(Animals[i])
        print(f"Adding value for {Animals[i]}, to the new list")
    else:
        print(f"Skipping {Animals[i]}, as length is not 7")

    i += 1
print(f"Animals made up of seven letter are: {Animal_7_letters}")