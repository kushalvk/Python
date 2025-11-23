# Bitwise Operator

# 1. Complement(~)
# 2. And(&)
# 3. Or(|)
# 4. XOR(^)
# 5. Left Shift(<<)
# 6. Right Shift(>>)


# 1. Complement(~)

# ~12
# -13 -> reveres of 12 binary that is -13


# 2. And(&)

# AND
#   0   0   =   0
#   0   1   =   0
#   1   0   =   0
#   1   1   =   1

#       00001100
#   &   00001101
#       --------
#       00001100 -> 12

# 12 & 13
# 12 -> convert this both into binary and check condition and compare (AND {from table} ) the output then convert in octal

# 15 & 19
# 3


# 3. Or(|)

# OR
#   0   0   =   0
#   0   1   =   1
#   1   0   =   1
#   1   1   =   1

#       00001100
#   |   00001101
#       --------
#       00001101 -> 13

# 12 | 13
# 13 -> convert this both into binary and check condition and compare (OR {from table} ) the output then convert in octal

# 15 | 19
# 31


# 4. XOR(^)

# XOR
#   0   0   ->  0
#   0   1   ->  1
#   1   0   ->  1
#   1   1   ->  0

#       00001100
#   ^   00001101
#       --------
#       00000001 -> 1

# 12 ^ 13
# 1

# 15 ^ 19
# 28


# 5. Left Shift(<<)

# 10 << 2
# 40

# 10 -> 1010 -> (left 2 shift) -> 101000 -> 40


# 6. Right Shift(>>)

# 10 >> 2
# 2

# 10 -> 1010 -> (right shift) -> 10 -> 2