from numpy import *

arr = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])

# print(arr)
# print(arr.dtype)
# print(arr.ndim) # number dimensions you have like 2D, 3D Array
# print(arr.shape) # it give number of rows and columns.
# print(arr.size) # size of complete block


arr1 = arr.flatten() # that is use to print complete array in 1 Dimensional

# print(arr1)


# arr2 = arr1.reshape(3, 4) # it's reshape the array 3, 4 means 3 rows and 4 columns
arr2 = arr1.reshape(2, 2, 3) # 2 array with 2 row and 3 column

# print(arr2)


arr3 = array([
    [1, 2, 3, 6],
    [4, 5, 6, 7]
])

m = matrix(arr3) # output will be same but you can perform matrices operations
# print(m)

# m1 = matrix('1 2 ; 3 4 ; 5 6 ; 7 8') # you can change array of dimension with coma(;)
# print(m1)

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
# print(diagonal(m1)) # you got all diagonal elements

# print(m1.min())
# print(m1.max())
# print(m1.sum())

m2 = matrix('9 8 7; 5 4 6; 3 1 2')

m3 = m1 * m2 # that is not a normal multiplication that is matrices multiplication
print(m3)