import sys

sys.stdin = open('input.txt')

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def snail(x, y):
    global m
    # 첫 값은 1
    # if 0 not in squa:
    #     return squa
    for dir in range(4):  # 4방향
        nx = x + dx[dir]
        ny = y + dy[dir]
        if dir == 2:
            squa[nx][ny] = m
            m += 1
            return snail(nx, ny)
        if 0 <= nx < N and 0 <= ny < N and squa[nx][ny] == 0:
            squa[nx][ny] = m
            m += 1
            return snail(nx, ny)

    return squa


for t in range(1, T + 1):
    N = int(input())  # 사각형 크기 N * N
    num_list = [i for i in range(1, N + 1)]
    squa = [[0] * N for _ in range(N)]
    squa[0][0] = 1
    m = 2
    print(f'#{t} {snail(0, 0)}')
