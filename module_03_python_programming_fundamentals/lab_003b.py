# Functions contd'
"""
So far, we've been creating variables within functions, but we have not discussed variables outside the function. These are called global variables.
Let's try to see what printer1 returns:
"""
# Example of global variable

artist = "Michael Jackson"
artist_1 = "Prince Chime"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
printer1(artist_1)
printer1("Mike Jordan")
# try runningthe following code
# printer1(internal_var1) returns name error

# create global variables from within a function 
artist = "Michael Jackson"
def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

"""
Scope of a Variable

The scope of a variable is the part of that program where that variable is accessible. 
Variables that are declared outside of all function definitions, such as the myFavouriteBand variable in the code shown here, are accessible from anywhere within the program. 
As a result, such variables are said to have global scope, and are known as global variables. 
myFavouriteBand is a global variable, so it is accessible from within the getBandRating function, and we can use it to determine a band's rating. 
We can also use it outside of the function, such as when we pass it to the print function to display it:
"""
# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand) # This will print the value from the global variable because the getBandRating function is not used here.

#  Collections and Functions

# When the number of arguments  are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')
printAll('Belgium','Hungary','UK','Portugal', 'Spain')

# Similarly, The arguments can also be packed into a dictionary as shown:

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    