# import array
# array.array()

# import array as arr
# arr.array()

# type defined table
# TypeCode          C Type          Python Type         Min. size in bytes
#   'b'           signed char           int                     1
#   'B'          unsigned char          int                     1
#   'u'           Py_UNICODE      Unicode_character             2
#   'h'          signed short           int                     2
#   'H'          unsigned short         int                     2
#   'i'           signed int            int                     2
#   'I'          unsigned int           int                     2
#   'I'           signed long           int                     4
#   'L'          unsigned long          int                     4
#   'f'             float              float                    4
#   'd'             double             float                    8

from array import *
vals = array('i', [5, 9, -8, 4, 2])

# print(vals[1])

# print(vals.buffer_info()) # it gives address of the array and size of the array.
# print(vals.typecode) # Type of datatype code of array
vals.append(7) # Add Value

# for num in vals:
#     print(num)
# print()

vals.remove(7)

# for num in vals:
#     print(num)
# print()

vals.reverse()

# for num in vals:
#     print(num)
# print()

# Copy an array
# newArray = array(vals.typecode, (a for a in vals)) # same as old array
newArray = array(vals.typecode, (a*a for a in vals)) # square of old array

for num in newArray:
    print(num)
print()

print(len(newArray))

# Char
chars = ['a', 'e', 'i', 'o', 'u']

# for char in chars:
#     print(char)