# All operation are perform in IDLE Shell


# 2 + 3
# 5

# x = 2
# x + 3
# 5

# y = 3
# x + y
# 5

# x = 9
# x + y
# 12

# x
# 9

# abc
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     abc
# NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?

# x + 10
# 19

# _ + y (_) means -> prev output
# 22

# name = 'Kushal'
# name
# 'Kushal'

# name + ' Vaghela'
# 'Kushal Vaghela'

# name[0]
# 'K'

# name[6]
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     name[6]
# IndexError: string index out of range

# name[5]
# 'l'

# name[-1] -> start index from revers
# 'l'

# name[-2]
# 'a'

# name[0:2]
# 'Ku'

# name[1:4]
# 'ush'

# name[1:]
# 'ushal'

# name[:4]
# 'Kush'

# name[3:10]
# 'hal'

# name[0:3] = 'my' -> you can't change a value of string (immutable)
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     name[0:3] = 'my'
# TypeError: 'str' object does not support item assignment

# name[0] = 'v'
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     name[0] = 'v'
# TypeError: 'str' object does not support item assignment

# 'my ' + name[3:]
# 'my hal'

# myname = "Kushal Vaghela"
# len(myname)
# 14



# more about variable

# num = 7
# id(num)
# 140704021480552 -> address of the variable

# name = 'Kushal'
# id(name)
# 1861956536768

# a = 10
# b = a
# a
# 10

# b
# 10

# id(a)
# 140704021480648

# id(b)
# 140704021480648

# id(10)
# 140704021480648

# k = 10
# id(k)
# 140704021480648

# a = 9
# id(a)
# 140704021480616

# id(b)
# 140704021480648

# k = a
# id(k)
# 140704021480616

# b = 8

# PI = 3.14 -> python doesn't support const variable but variable name is uppercase for best practices
# PI
# 3.14

# PI = 3.15
# PI
# 3.15

# type(PI)
# <class 'float'>

# type(a)
# <class 'int'>

