
class Computer:

    def __init__(self):
        self.name = "Kushal"
        self.age = 22

    def compare(self, obj):
        if self.age == obj.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

c1.age = 24

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)