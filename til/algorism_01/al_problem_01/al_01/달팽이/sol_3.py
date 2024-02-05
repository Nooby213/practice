import sys

sys.stdin = open('input.txt')

def print_snail_recursive(snail, num, x, y, direction):
    # 기저 조건: 배열이 모두 채워질 경우
    if num > N * N:
        return

    snail[x][y] = num
    nx, ny = x + dx[direction], y + dy[direction]

    # 방향을 바꿔야 하는 경우
    if nx < 0 or ny < 0 or nx >= N or ny >= N or snail[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]

    print_snail_recursive(snail, num + 1, nx, ny, direction)

def print_snail(N):
    snail = [[0] * N for _ in range(N)]  # N x N 크기의 2차원 배열 생성
    print_snail_recursive(snail, 1, 0, 0, 0)  # 시작 좌표 (0, 0), 초기 방향 오른쪽

    # 결과 출력
    for row in snail:
        print(*row)

# 테스트 케이스 입력 및 실행
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    dx = [0, 1, 0, -1]  # 방향 설정: 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]
    print_snail(N)
