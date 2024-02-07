import sys

sys.stdin = open('input.txt')
# 연속된 N일 동안의 물건의 매매가 예측
# 하루에 최대 1만큼 구입
# 판매 언제든지 가능

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    D = list(map(int, input().split()))
    money = 0
    cnt = 0
    for i in range(N):
        if i < D.index(max(D[i:])):
            money += max(D[i:])-D[i]
            cnt += 1
    print(cnt)
    print(f'#{t} {money}')

