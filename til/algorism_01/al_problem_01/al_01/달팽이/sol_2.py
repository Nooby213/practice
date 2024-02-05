import sys

sys.stdin = open('input.txt')

# N * N

def snail(N):
    snail = [[0] * N for _ in range(N)]  # N x N
    num = 1  # 출력할 숫자 초기화

    # 방향 설정: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 시작 좌표
    x = 0
    y = 0
    dir = 0  # 초기 방향 설정

    while num <= N ** 2:
        snail[x][y] = num
        num += 1

        nx = x + dx[dir]
        ny = y + dy[dir]

        # 방향을 바꿔야 하는 경우
        if nx < 0 or ny < 0 or nx >= N or ny >= N or snail[nx][ny] != 0:
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]

        x = nx
        y = ny

    # 결과 출력
    for row in snail:
        print(*row)


# 테스트 케이스 입력 및 실행
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    snail(N)
