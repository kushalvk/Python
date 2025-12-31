# Tow type of variable in OOPS
# 1. Instance Variable -> inside __init__
# 2. Class Variable -> Outside of __init__ inside of Class

class Car:

    wheels = 4 # class Variable/namespace

    def __init__(self):
        self.mil = 10 # This both are instance variable/namespace
        self.com = 'BMW'

c1 = Car()
c2= Car()

c1.mil = 20

Car.wheels = 7

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)