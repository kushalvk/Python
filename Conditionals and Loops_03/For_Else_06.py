nums = [12, 13, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not Found")

# that else is for FOR loop when number not found in the loop the it print else if found then it will not execute else part.