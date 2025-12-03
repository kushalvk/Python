
class Computer:

    def config(self):
        print("i5, 16GB, 512GB")

com1 = Computer()
com2 = Computer()

# Prints followings
Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()