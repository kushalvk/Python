class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 - A working")

    def feature2(self):
        print("Feature 2 working")


# class B(A):
class B:

    def __init__(self):
        # super().__init__()
        print("in B Init")

    def feature1(self):
        print("Feature 1 - B working")

    def feature4(self):
        print("Feature 4 working")

class C(A, B):

    def __init__(self):
        super().__init__() # Super for left side inheritance hear is A
        print("in C Init")

    def feat(self):
        super().feature2()

a1 = C()
a1.feature1() # It get form A Class - MRO (Method Resolution Order)
a1.feat()