from array import *

arr = array('i',[])

# insert
n = int(input("Enter the size of array: "))
for i in range(1 ,n + 1):
    x = int(input(f"Enter the number {i}: "))
    arr.append(x)

print(arr)

# search
s = int(input("Enter the value do you want eo Search: "))
for i in range(n):
    if arr[i] == s:
        print(f"The position of the element in index is {i}")
        break

# print(arr.index(s)) # this will give index directly