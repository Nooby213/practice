import sys

sys.stdin = open('input.txt')

# N * N
# 길이가 M 인 회문을 찾아 출력 0 ~ M-1
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 길이가 M 인 회문을 찾아 출력
    str_lst = [list(map(str, input())) for _ in range(N)]  # N * N 리스트
    # print(str_lst)
    for k in range(N - (M - 1)):  # 가로
        for n in range(N):
            word = []
            for m in range(M):
                word.append(str_lst[n][m + k])
            if word == word[::-1]:
                print(f'#{t} {"".join(word)}')
                break

    for k in range(N - (M - 1)):
        for n in range(N):
            word = []
            for m in range(M):
                word.append(str_lst[m + k][n])
            if word == word[::-1]:
                print(f'#{t} {"".join(word)}')
                break
