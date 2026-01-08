import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])
# print(arr)

# print(arr[:]) # all row
# print(arr[0:1]) # First Row
# print(arr[0:1, 1:]) # First Row start from index 1 to end of row 1
# print(arr[0:1, 1:2]) # First Row start from index 1 to end at index 1

arr_max = np.array([[3, 4, 5, 6, 7, 9], [1, 0, 0, 1, 0, 1], [1, 3, 5, 7, 9, 1], [2, 4, 6, 8, 1, 3]])
# print(arr_max)
# print(arr_max[0:1]
# print(arr_max[0:2, 1:])
# print(arr_max[0:2, 1:4])
print(arr_max[0:3:2, 0:5:2]) # skip 1 value by (default is 1)