import sys

sys.stdin = open('input.txt')

T = int(input())


def tran(alist):
    trans = [["ZRO", 0], ["ONE", 1], ["TWO", 2], ["THR", 3], ["FOR", 4],
             ["FIV", 5], ["SIX", 6], ["SVN", 7], ["EGT", 8], ["NIN", 9]]
    for a in range(len(alist)):
        for tr in trans:
            if alist[a] == tr[0]:
                alist[a] = tr[1]
                break
    return alist


def itoa(alist):
    trans = [["ZRO", 0], ["ONE", 1], ["TWO", 2], ["THR", 3], ["FOR", 4],
             ["FIV", 5], ["SIX", 6], ["SVN", 7], ["EGT", 8], ["NIN", 9]]
    for a in range(len(alist)):
        for tr in trans:
            if alist[a] == tr[1]:
                alist[a] = tr[0]
                break
    return alist


for t in range(1, T + 1):
    ts, N = input().split()
    num_lst = list(map(str, input().split()))
    tran(num_lst)
    # print(num_lst)
    num_lst.sort()
    # print(num_lst)
    itoa(num_lst)
    print(ts)
    print(*num_lst)
