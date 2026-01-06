
pos = -1

def search(list, n):
    L = 0
    U = len(list) - 1

    while L <= U:
        mid = (L + U) // 2 # '//' this is for get only int value not float value

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                L = mid + 1
            else:
                U = mid - 1
    return False

arr = [4, 7, 8, 12, 45, 99, 102, 702, 10987, 56666]

n = 10987

if search(arr, n):
    print('Found at index', pos)
else:
    print('Not Found')