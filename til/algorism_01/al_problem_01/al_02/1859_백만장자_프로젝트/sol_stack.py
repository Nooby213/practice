import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]   # 최댓값이 커지면 바꾸니까 뒤에서부터
    profit = 0
    for i in range(N - 1, -1, -1):  # 최댓값이 커지면 바꾸니까 뒤에서부터
        if max_price < price[i]:
            max_price = price[i]
        else:
            profit += (max_price - price[i])

    print(f'#{test_case} {profit}')

# T = int(input())
#
# for t in range(1, T + 1):
#     N = int(input())
#     D = list(map(int, input().split()))
#     money = 0
#     for i in range(N):
#         if i < D.index(max(D[i:])):
#             money += max(D[i:]) - D[i]
#
#     print(f'#{t} {money}')

