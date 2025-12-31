
a = 5
b = 2

try:
    print('resource Open')
    print(a/b)

    k = int(input('Enter a number: '))
    print(k)
except ZeroDivisionError as e:
    print("Hey, You can't divide a Number by zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something Went Wrong...!")

finally:
    print("resource Close")
    print("Goodbye")