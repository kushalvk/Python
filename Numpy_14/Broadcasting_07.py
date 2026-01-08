import numpy as np

# arr1 = np.array([1, 2, 3])
# print(arr1)
# arr2 = np.array([4, 5, 6])
# print(arr2)

# arr3 = arr1 + arr2
# arr3 = arr1 + 6
# print(arr3)


# Broadcasting

# arr1 = np.array([1, 2, 3]) # 1 X 3
# # print(arr1)
# arr2 = np.array([[4], [5], [6]]) # 3 X 1
# # print(arr2)
#
# arr3 = arr1 + arr2 # 3 X 3
# # arr3 = arr1 + 6
# print(arr3)


# arr1 = np.array([1, 2, 3]) # Shape: (3,)
# # print(arr1)
# arr2 = np.array([4, 5, 6, 7]) # Shape: (4,)
# # print(arr2)
#
# arr3 = arr1 + arr2
# print(arr3)
# Error: Shape Not match (Not Valid)


# arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1.ndim)
# arr2 = np.array([2, 2, 2])
# print(arr2.ndim)
#
# arr3 = arr1 + arr2
# print(arr3)


arr1 = np.array([[1, 2], [3, 4], [5, 6]]) # 3 X 2
arr2 = np.array([2, 2, 2]) # 1 X 3

arr3 = arr1 + arr2
print(arr3)
# Error: if arr2 adjust but arr1 can't adjustable
