import numpy as np

# Consider the following list a, convert it to Numpy Array. 

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)

# Calculate the numpy array size.
A_size = A.size
print('Result...', A_size)

# Access the element on the first row and first and second columns.
A_r1_c2 = A[0,0:2]
print('Result...', A_r1_c2)

# Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

C = np.dot(A,B)
print(C)

