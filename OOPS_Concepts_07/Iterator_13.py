# nums = [1, 2, 3, 4, 5, 6, 7]

# for i in nums:
#     print(i)

# it = iter(nums)
# print(it.__next__()) # Prints First element
# print(it.__next__()) # Prints Second element
# print(next(it)) # Prints Third element

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

value = TopTen()

print(value.__next__())
# we access first element ones that was not again print in loop that is power of own iterator
for i in value:
    print(i)