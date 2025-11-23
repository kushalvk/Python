# All operation are perform in IDLE Shell

#  Datatypes
#   -   None -> variable has doesn't defined any values
#   -   Numeric -> int, float, complex, bool
#   -   List
#   -   Tuple
#   -   Set
#   -   String
#   -   Range
#   -   Dictionary(Map)


#   -   Numeric -> int, float, complex, bool

# num = 2.5
# type(num)
# <class 'float'>

# num = 5
# type(num)
# <class 'int'>

# num = 6 + 9j
# type(num)
# <class 'complex'>

# a = 5.6
# b = int(a)
# type(b)
# <class 'int'>

# b
# 5

# k = float(b)
# type(k)
# <class 'float'>

# k
# 5.0

# k = 6
# c = complex(b, k)
# c
# (5+6j)

# b < k
# True

# bool = b < k
# bool
# True
# type(bool)
# <class 'bool'>

# int(True)
# 1

# int(False)
# 0


# List

# lst = [25, 36, 45, 12]
# type(lst)
# <class 'list'>


# Set

# s = {25, 36, 45, 15, 12, 25}
# type(s)
# <class 'set'>


# Tuple

# t = (25, 36, 4, 57, 12)
# type(t)
# <class 'tuple'>


# String

# str = "Kushal"
# type(str)
# <class 'str'>


# Range

# range(10)
# range(0, 10)

# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list(range(2, 10, 2))
# [2, 4, 6, 8]

# type(range(10))
# <class 'range'>


# Dictionary

# d = {'Kushal': 'Oppo', 'Prince': 'Iphone', 'Harshil': 'Oneplus'}
# d
# {'Kushal': 'Oppo', 'Prince': 'Iphone', 'Harshil': 'Oneplus'}

# d.keys()
# dict_keys(['Kushal', 'Prince', 'Harshil'])

# d.values()
# dict_values(['Oppo', 'Iphone', 'Oneplus'])

# d['Kushal']
# 'Oppo'

# d.get('Prince')
# 'Iphone'
