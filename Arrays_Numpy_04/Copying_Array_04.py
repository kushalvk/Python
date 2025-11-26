from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])

# arr1 = arr1 + 5
# arr3 = arr1 + arr2

# print(arr3)

# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))
# print(concatenate((arr1, arr2)))


# Copy array
# arr3 = arr1 # this will not create a different array

# "shallow copy"
# arr3 = arr1.view() # view() create a different array at different location
# view create a "shallow copy" if you change in arr1 that will also change in arr3

# "Deep Copy"
arr3 = arr1.copy() # copy() create a different array at different location
# copy create a "Deep copy" if you change in arr1 that will not change in arr3

arr1[1] = 7

print(arr1)
print(arr3)

print(id(arr1))
print(id(arr3))