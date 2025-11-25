# 1)
# # # #
# # # #
# # # #
# # # #
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()
print()

# 2)
#
# #
# # #
# # # #
for i in range(4):
    for j in range(i + 1):
        print("#", end=" ")
    print()
print()


# 3)
# # # #
# # #
# #
#
for i in range(4):
    for j in range(4 - i):
        print("#", end=" ")
    print()
print()


# 4)
# 1 2 3 4
# 2 3 4
# 3 4
# 4
for i in range(1, 5):
    for j in range(i, 5):
        print(j, end=" ")
    print()
print()


# 5)
# A P Q R
# A B Q R
# A B C R
# A B C D
# n = 4
# for i in range(n):
#     for j in range(n):
#         if j < i:
#             # Print increasing letters from A
#             print(chr(ord('A') + j), end=' ')
#         else:
#             # Print decreasing letters from R, Q, P (reverse from R down)
#             print(chr(ord('A') + n - j - 1 + i), end=' ')
#     print()
# print()