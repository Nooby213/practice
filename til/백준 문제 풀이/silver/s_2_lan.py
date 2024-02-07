import sys

input = sys.stdin.readline

# N개의 랜선 만든다.
# K선 가지고 있다.
# K 개의 랜선으로 N개의 같은 길이
# 1 <= K <= 10 000
# 1 <= N <= 10 000 00
# k <= N

K, N = map(int, input().split())
line = [int(input()) for i in range(K)]
# print(line)
n = sum(line) // N
# print(n)
cnt = N - 1
while cnt < N:
    cnt = 0
    for l in line:
        cnt += (l // n)

    if cnt >= N:
        print(n + 1)
        break
    else:
        n -= 1

