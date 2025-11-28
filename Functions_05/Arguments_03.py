
# Formal Arguments
# def add(a, b):
#     c = a + b
#     print(c)
#
# add(1, 2)

# Actual Arguments
#     1. Position
#     2. Keyword
#     3. Default
#     4. Variable Length

# Position
# def person(name, age):
#     print(name, age + 2)

# person('Kushal', 20) # Index Matters
# person(20, 'Kushal') # This will you error of you are performing an operation on value
# person(age=20, name='Kushal')

# Default
# def person(name, age = 18):
#     print(name, age + 2)
#
# person('Kushal')
# person('Kushal', 20)

# Variable Length
# def Sum(a, *b): # you can pass only one variable also like (*b) it will also accept multiple values
#     c = a
#     for i in b:
#         c += i
#
#     print(c)
#
# Sum(5, 6, 7, 8) # in this 5 is treat as int and other are b and the type of it is Tuples

# Keyword
def person(name, **data): # give it ** if you are giving data with key(keyword)

    print(name, data)

    for i, j in data.items():
        print(i, j)

person('name', age=28, city='Surat', mob=147852369)