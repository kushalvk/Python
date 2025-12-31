
a = 5
b = 6
# b = 'world'

# print(a + b)
# print(int.__add__(a, b))


c = '5'
d = '6'
# b = 'world'

# print(c + d)
# print(str.__add__(c, d))


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other): # + Operator
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other): # > Operator
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(4, 3)
s2 = Student(5, 2)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print('s1 Win :)')
else:
    print('s2 Win :)')

print(s1.__str__())
print(s2.__str__())