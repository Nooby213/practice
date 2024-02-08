import sys

sys.stdin = open('input.txt')

# 크기가 N인 파스칼 삼각형
# 첫 번째 숫자 1
# 두 번째 숫자는 왼쪽과 오른쪽 위의 합

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tri = [[1] * i for i in range(1, N + 1)]
    # print(tri)

    # for i in range(N):  # 양 쪽은 1  리스트를 0으로 만들었다면
    #     for j in 0, i:
    #         tri[i][j] = 1
    # # print(tri)

    for i in range(2, N):   # 가운데 숫자만들기
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{t}')
    for tr in tri:
        print(*tr)
