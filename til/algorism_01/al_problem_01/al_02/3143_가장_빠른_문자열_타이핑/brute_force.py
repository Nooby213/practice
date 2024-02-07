import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    A, B = input().split()  # A 는 문자열, B 는 타이핑 키
    a = len(A)
    b = len(B)

    count_B = 0
    i = 0

    while i <= a - b:
        if A[i:i + b] == B:
            count_B += 1
            i += b
        else:
            i += 1

    count_num = a + count_B - (b * count_B)
    print(f'#{t} {count_num}')
