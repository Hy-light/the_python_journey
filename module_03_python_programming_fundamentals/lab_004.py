# Creating Class

# Import the library

import matplotlib.pyplot as plt
#


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

RedCircle = Circle(10, 'red')
print(RedCircle.color)

# draw the circle
# RedCircle.drawCircle()

# We can increase the radius of the circle by applying the method add_radius(). Let's increases the radius by 2 and then by 5:

# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)



# The Rectangle Class

# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Let’s create the object SkinnyBlueRectangle of type Rectangle. Its width will be 2 and height will be 3, and the color will be blue:

# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attribute height
print(SkinnyBlueRectangle.height)

# Print the object attribute width
print(SkinnyBlueRectangle.width)

# Print the object attribute color
print(SkinnyBlueRectangle.color)

# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()


# Let’s create the object FatYellowRectangle of type Rectangle:
# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Print the object attribute height, width and color
print(FatYellowRectangle.height)
print(FatYellowRectangle.width)
print(FatYellowRectangle.color)
FatYellowRectangle.drawRectangle()


