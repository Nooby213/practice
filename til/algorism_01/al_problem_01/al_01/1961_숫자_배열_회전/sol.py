import sys

sys.stdin = open('input.txt')

T = int(input())


def rotation(alist):  # 회전 함수
    alist_copy = [[0] * N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            alist_copy[n][m] = alist[(N-1) - m][n]
    return alist_copy


for t in range(1, T + 1):  # 테스트 케이스 반복
    N = int(input())  # N * N 행렬

    alist = [list(map(str, input().split())) for _ in range(N)]
    # print(alist)

    rotation_90 = rotation(alist)
    rotation_180 = rotation(rotation_90)
    rotation_270 = rotation(rotation_180)

    # print(rotation_90)
    # print(rotation_180)
    # print(rotation_270)

    row1 = [*rotation_90[0], *rotation_180[0], *rotation_270[0]]
    row2 = [*rotation_90[1], *rotation_180[1], *rotation_270[1]]
    row3 = [*rotation_90[2], *rotation_180[2], *rotation_270[2]]

    print(f'#{t}')

    for n in range(N):
        print(''.join(rotation_90[n]), ''.join(rotation_180[n]), ''.join(rotation_270[n]))
