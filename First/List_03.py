# All operation are perform in IDLE Shell
# List is multable(you can change it's value)


# nums = [25, 12, 36, 95, 14]
# nums
# [25, 12, 36, 95, 14]

# num[0]
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     num[0]
# NameError: name 'num' is not defined. Did you mean: 'nums'?

# nums[0]
# 25

# nums[4]
# 14

# nums[2:
#      ]
# [36, 95, 14]

# nums[-1]
# 14

# num[-5]
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     num[-5]
# NameError: name 'num' is not defined. Did you mean: 'nums'?

# nums[-5]
# 25

# name = ['Kushal', 'Prince', 'Harshil']
# name
# ['Kushal', 'Prince', 'Harshil']

# values = [9.5, 'Kushal', 25]
# values
# [9.5, 'Kushal', 25]

# mil = [nums, name]
# mil
# [[25, 12, 36, 95, 14], ['Kushal', 'Prince', 'Harshil']]

# nums.append(45)
# nums
# [25, 12, 36, 95, 14, 45]

# nums.insert(2, 77)
# nums
# [25, 12, 77, 36, 95, 14, 45]

# nums.remove(14)
# nums
# [25, 12, 77, 36, 95, 45]

# nums.pop(1)
# 12
# nums
# [25, 77, 36, 95, 45]

# nums.pop()
# 45
# nums
# [25, 77, 36, 95]

# del nums[2:]
# nums
# [25, 77]

# nums.extend(19, 12, 14, 36)
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     nums.extend(19, 12, 14, 36)
# TypeError: list.extend() takes exactly one argument (4 given)

# nums.extend([19, 12, 14, 36])
# nums
# [25, 77, 19, 12, 14, 36]

# min(nums)
# 12

# max(nums)
# 77

# sum(nums)
# 183

# nums.sort()
# nums
# [12, 14, 19, 25, 36, 77]
