
# Break
# available = 10
#
# x = int(input("How many Candies you want ? "))
#
# i = 1
# while i <= x:
#
#     if i > available:
#         print("Our Of Stock")
#         break
#
#     print("Candies ", i)
#     i += 1
#
# print("Bye")


# Continue
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)
# print("Bye")


# Pass
for i in range(1, 101):
    if i % 2 != 0:
        pass # it will only pass the next statement
    else:
        print(i)
print("Bye")

def func():
    pass # temporary you don't know the login then we can go with pass because empty function gives Error(Use to Skip the block)
x = 7