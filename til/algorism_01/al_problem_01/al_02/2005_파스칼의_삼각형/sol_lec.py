import sys

sys.stdin = open('input.txt')

T = int(input())

# 강의
memo = [[1] * 10 for _ in range(10)] # 최대로 주어지는 수가 10이기 때문에
for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    for i in range(N):
        print(*memo[i][:i+1])

# 수학 천재

# for t in range(1, T + 1):
#     N = int(input())
#     print(f'#{t}')
#     for i in range(N):
#         ans = str(11 ** i)
#         print(' '.join(ans))


