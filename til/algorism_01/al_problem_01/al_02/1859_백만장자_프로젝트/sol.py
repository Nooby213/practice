import sys

sys.stdin = open('input.txt')
# 연속된 N일 동안의 물건의 매매가 예측
# 하루에 최대 1만큼 구입
# 판매 언제든지 가능

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    D = list(map(int, input().split()))
    price = 0
    max_price = D[-1]
    for i in range(N - 2, -1, -1):  # 최댓값이 커지면 바꾸니까 뒤에서부터
        if max_price < D[i]:
            max_price = D[i]
        else:
            price += max_price - D[i]
    print(f'#{t} {price}')
