from os import write

# f = open("MyData","r")

# print(f.read())
# print(f.readline())
# print(f.readlines())
# print(f.readable()) # it give a Boolean value

# print(f.readline(), end="#")
# print(f.readline())

# print(f.readline(4)) # Four Character

# f1 = open("abc","w") # it will create a file if it's not exist.
# f1.write("Something")
# f1.write("People")

# f1 = open("abc","a")
# f1.write("Laptop")

# TODO: Read all the data from MyData & past it in abc file

# f = open("MyData","r")

# f1 = open("abc","w")

# for data in f:
#     f1.write(data)

# TODO: Read Image Create a Copy of it.

f = open("NEXT.jpeg", "rb")
f1 = open("NEW.jpeg", "wb")

for i in f:
    f1.write(i)