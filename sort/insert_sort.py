alist = [3, 1, 5, 6, 9, 8, 2, 4, 7, 0]


def insert_sort(alist):
    for n in range(1, len(alist)):
        for m in range(n, 0, -1):
            if alist[m] < alist[m - 1]:
                alist[m], alist[m - 1] = alist[m - 1], alist[m]
            else:
                break
    return alist


result = insert_sort(alist)
print((result))
