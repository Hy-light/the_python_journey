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