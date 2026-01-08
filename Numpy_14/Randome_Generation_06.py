
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

arr_rg = gen(pcg(seed=300)) # seed = size of the values
# arr = arr_rg.normal(size=(5, 5)) # 5 X 5 array with random value
# arr = arr_rg.integers(low=10, high=100, size=(5, 5)) # random value(10 - 100)
arr = arr_rg.random(size=(5, 5)) # 0 - 1
print(arr)