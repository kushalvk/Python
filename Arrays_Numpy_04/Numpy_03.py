from numpy import *

# arr = array([1, 2, 3, 4, 5])
# arr = array([1, 2, 3, 4, 5.0])
# arr = array([1, 2, 3, 4, 5],int)
# arr = array([1, 2, 3, 4, 5],float)

# arr = linspace(0, 15) # 0 is starting index and 15 is till go this number and last parameter is parts if can't mention that it will consider 2 parameter is also part of number.
# arr = linspace(0, 15, 16)
# arr = linspace(0, 15, 20)

# arr = arange(1, 15, 2) # first elem. last elem. and thread is number of steps

# arr = logspace(1, 40, 5) # log values

# arr = zeros((5,3)) # multidimensional array with 0's of this rows & columns 5 - rows, 3 - columns

# arr = ones((5,3)) # multidimensional array with 1's of this rows & columns 5 - rows, 3 - columns
arr = ones(5, int)

print(arr)
print(arr.dtype)