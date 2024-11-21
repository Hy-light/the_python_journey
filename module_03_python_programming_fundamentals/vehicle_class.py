# Scenario: Car dealership's inventory management system

"""
You are working on a Python program to simulate a car dealership's inventory management system. 
The system aims to model cars and their attributes accurately.

Task-1. You are tasked with creating a Python program to represent vehicles using a class. 
Each car should have attributes for maximum speed and mileage.

Task-2. Update the class with the default color for all vehicles," white".

Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.

Task-4. Create a method to display all the properties of an object of the class.

Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kph
 and mileage of 50000kmpl with five seating capacities, 
and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.
"""

class Car_dealer_inventory:

    def __init__(self, max_speed, mileage, color='white'):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

    # method
    def seatingCapacity(self,seating_capacity):
        self.seatingCapacity = seating_capacity

    def displayAll_properties (self):
        print("Properties of the Vehicle:")
        print("max_speed: ", self.max_speed)
        print("mileage:", self.mileage)
        print("color:", self.color)
        print("seating_capacity:", self.seatingCapacity, '\n')

car_001 = Car_dealer_inventory('200kph', '50000kmpl')
car_001.seatingCapacity('5')
print(car_001.displayAll_properties())


car_002 = Car_dealer_inventory('180kph', '75000kmpl')
car_002.seatingCapacity('4')
print(car_002.displayAll_properties())