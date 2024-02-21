import sys
sys.stdin = open('input.txt')

# N * N 파리판 5 <= N <= 15
# M * M 파리채로 죽인 파리채 2 <= M <= N
# 각 영역의 파리수는 30 이하

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]