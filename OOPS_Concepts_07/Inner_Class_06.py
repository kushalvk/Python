
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name)
        print(self.rollno)
        self.lap.show()

    class Laptop: # Inner Class

        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Kushal", 7)
s2 = Student("vk", 3)

s1.show()

# print(s1.lap.brand)
#
# lap1 = s1.lap
# lap2 = s2.lap
#
# print(id(lap1))
# print(id(lap2))
