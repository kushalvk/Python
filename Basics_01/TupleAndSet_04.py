# All operation are perform in IDLE Shell


# Tuple

# Tuple is immutable(you can't change it's value)

# tup = (21, 36, 14, 25)
# tup
# (21, 36, 14, 25)

# tup[1]
# 36

# tup[1] = 33
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     tup[1] = 33
# TypeError: 'tuple' object does not support item assignment

# tup.count(36) -> count how many time 36 in the tuple.
# 1


# Set

# Set Uses a Hash Concept.
# we get data not in sequence.
# motive - get fast data.(speed)

# s = {22, 25, 14, 21, 5}
# s
# {5, 21, 22, 25, 14} -> not follow sequence

# s = {25, 14, 98, 63, 75, 98}
# s
# {98, 25, 75, 14, 63} -> forgot repetition

# s[2] -> it does't support indexing because it's not follow sequence
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     s[2]
# TypeError: 'set' object is not subscriptable

# s.add(7)
# s
# {98, 7, 25, 75, 14, 63}
