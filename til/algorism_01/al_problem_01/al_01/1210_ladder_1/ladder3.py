import sys
sys.stdin = open('input.txt')

def search(i, j):
    visited = [[0] * 100 for _ in range(100)]  # 방문했는지 체크
    while i != 99:  # 탐색 : x가 99가 될 때까지 순회
        for dir in [(-1, 0), (0, -1), (0, 1)]:  # 3방향 탐색 => 위 왼 오
            # 다음 탐색 대상의 i, j 좌표값
            ni = i + dir[0]
            nj = j + dir[1]
            # 범위를 벗어나지 않고
            # 해당 위치가 1이라 이동 가능하고
            # 이전에 방문한 적 없고
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] and not visited[ni][nj] == 1:
                if not visited[ni][nj]:
                    i, j = ni, nj  # 이동
                    visited[ni][nj] = 1  # 방문한적 있음을 표시
    return j


for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    # 사다리 크기 = 100 * 100
    for j in range(100):
        # 출발 지점 : i 좌표 0으로 고정
        if arr[99][j] == 2:
            result = search(99, j)
            if result != None:
                break

    print(f'#{test_case} {result}')