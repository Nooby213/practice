import sys

sys.stdin = open('input.txt')

# N 개의 단어로 이루어진 회문
# 1개짜리도 회문이다.

for t in range(1, 11):
    N = int(input())  # 길이가 M 인 회문을 찾아 출력
    str_lst = [list(map(str, input())) for _ in range(8)]  # N * N 리스트
    # print(str_lst)

    count = 0

    for k in range(8 - (N - 1)):  # 가로
        for n in range(8):
            word = []
            for m in range(N):
                word.append(str_lst[n][m + k])
            if word == word[::-1]:
                count += 1

    for k in range(8 - (N - 1)):    # 세로
        for n in range(8):
            word = []
            for m in range(N):
                word.append(str_lst[m + k][n])
            if word == word[::-1]:
                count += 1

    print(f'#{t} {count}')

