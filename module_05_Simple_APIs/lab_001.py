# Numpy 
# import numpy library
import numpy as np

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)

# Check the type of the array
type(a)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))


# Create numpy array
c = np.array([20, 1, 2, 3, 4])

# Change the value of a partiular element via it's index
c[4] = 8
print(c)

c = np.array([-10, 201, 43, 94, 502])
# Enter your code here
d = (c.min())
e = (c.max())
f = (d + e)
print(f)

# multiply
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

# Enter your code here
c = np.multiply(arr1, arr2)
print(c)

# dot products
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

# Enter your code here
arr3 = np.dot(arr1, arr2)
print(arr3)

'''
Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
'''

# Write your code below and press Shift+Enter to execute
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
print(arr3, 'Add...')

arr4 = np.subtract(arr1, arr2)
print(arr4, 'Subtracting...')

arr5 = np.multiply(arr1, arr2)
print(arr5, 'Multiplying...')


arr6 = np.divide(arr1, arr2)
print(arr6, 'Dividing...')

arr7 = np.dot(arr1, arr2)
print(arr7, '= Dot product...')
