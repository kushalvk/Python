
def sort(list):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if list[j] < list[minpos]:
                minpos = j

        list[i], list[minpos] = list[minpos], list[i]

        print(list)

nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)