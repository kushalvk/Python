
import sys

sys.setrecursionlimit(2000) # that is use to change a limit of the function recursion - default(1000)

print(sys.getrecursionlimit())

i = 0

def Greet():
    global i
    i += 1
    print("Hello ", i)
    Greet()

Greet()