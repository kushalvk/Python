
a = 10
print(id(a))

def somthing():

    # global a # if you are not specify this then a teat as a local variable(but after that you can't create a another 'a' local variable
    a = 9
    # b = 8
    print("in Fun", a)

    x = globals()['a']
    print(id(x))
    globals()['a'] = 15

somthing()
print("Out Fun", a)
# print(b) # you can't access it outside the function