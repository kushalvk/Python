import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])
# print(arr)

# print(arr[0])
# print(arr[0][1])
# print(arr[1][2])
# print(arr[1, 2]) # same as [1][2]

# arr[1][1] = 55
arr[1] = 7 # values is 7 of all element in the second row
print(arr)
print(arr[0] + 4) # [5 6 7]

# arr_new  = np.array([1, 2, 3])
# print(arr_new[-1]) # last value
# print(arr_new[-2]) # second last value