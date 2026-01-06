
pos = -1

def search(list, n):
    i = 0

    while i < len(list):
    # for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

arr = [5, 8, 4, 6, 9, 2]

n = 9

if search(arr, n):
    print('Found at index', pos)
else:
    print('Not Found')