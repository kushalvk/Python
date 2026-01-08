import numpy as np

arr = np.arange(1,13) # it gives array value 1 - 12
print(arr)

reshaped = arr.reshape(3, 4) # divide into (Row, Column) here -> 3 Row & 4 Column
print(reshaped)

flattened = reshaped.flatten()  # it gives array in one line mean all array merge in one array
# flatten is create a another array. that's not affect original array (Slower)
print(flattened)

raveled = reshaped.ravel()  # same as flatten
# ravel is not create a another array. that's affect an original array (Faster)
# it's only create a view of Original array but actual array is in it's original formate
print(raveled)