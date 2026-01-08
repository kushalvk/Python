# python does not support multidimensional array
# but we can do it with "Numpy"

# Normal Code(Array)
import time

# import time
#
# start_time = time.time()
#
# a = [i for i in range(100000000)]
# b = [i for i in range(100000000, 200000000)]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i] + b[i])
#
# print(time.time() - start_time)
# it's take approx 75 seconds

# Numpy Code(Array)
import  numpy as np
start_time = time.time()

a = np.arange(100000000)
b = np.arange(100000000, 200000000)

c = a + b
print(time.time() - start_time)
# it's take < 1 seconds