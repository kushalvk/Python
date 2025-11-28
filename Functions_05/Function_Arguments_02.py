# Python does not support coll by value & call by reference

# def update(x):
#     x = 8
#     print(x)
#
# a = 10
# update(a)
# print("a ", a)

def update(l):
    print(id(l))
    l[1] = 25
    print(id(l))
    print("l ", lst)

lst = [10, 20, 30]
print(id(lst))
update(lst)
print("lst ", lst)