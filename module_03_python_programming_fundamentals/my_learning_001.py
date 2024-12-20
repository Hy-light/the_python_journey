# help(print)
help(input)


# Classes and Objects
"""
You will need the class Car for the next exercises. 
The class Car has four data attributes: make, model, colour and number of owners (owner_number). 
The method  car_info() prints out the data attributes and the method sell() increments the number of owners by 1.
"""

class Car(object):
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1

# Create a  Car object "my_car" with the given data attributes: 
"""
make="BMW"
model="M3"
color="red"
"""

my_car = Car("BMW", "M3", "red")

# Use the method car_info() to print out the data attributes.
print(my_car.car_info())

# Call the method  sell() in the loop, then call the method  car_info() again

for i in range(5):
    my_car.sell()

print(my_car.car_info())