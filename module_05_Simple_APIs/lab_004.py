# API
# Random User api
from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users.

some_list = r.generate_users(10)
print(some_list)


# Getting full name
name = r.get_full_name()
print(name)

# 10 users with full names and their email addresses

for user in some_list:
    print(user.get_full_name()," ",user.get_email())

# Exercise 1¶

# In this Exercise, generate photos of the random 10 users.

for user in some_list:
    print(user.get_picture())

'''
To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the needed Get Methods. Then, we return pandas dataframe with the users
'''

def get_users(x):
    users =[]
     
    for user in RandomUser.generate_users(x):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)    

print(get_users(4))
df1 = pd.DataFrame(get_users(5))  
print(df1)