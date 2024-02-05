import sys
sys.stdin = open('input.txt')
from pprint import pprint as pp
T = int(input()) # 테스트 케이스 갯수

for t in range(1, T + 1):
    N, M = map(int, input().split()) # N * M  배열
    balloons = []
    for n in range(N): # 풍선 판 만들기
        m_list = list(map(int, input().split()))
        balloons.append(m_list)
    # print(balloons)
    # balloons = [list(map(int, input().split())) for _ in range(N)]
    
    score =[[0] * M for _ in range(N)]
    # print(score)
    for n in range(1, N):   # 밑에 풍선 점수 더한다.
        for m in range(M):
            score[n][m] += balloons[n - 1][m]
        # pp(score)
    for n in range(N - 1):  # 위에 풍선 점수 더한다.
        for m in range(M):
            score[n][m] += balloons[n + 1][m]
        # pp(score)
    for n in range(N):  # 왼쪽 풍선 점수 더한다.
        for m in range(1, M):
            score[n][m] += balloons[n][m - 1]
        # pp(score)
    for n in range(N):  # 오른쪽 풍선 점수 더한다.
        for m in range(M - 1):
            score[n][m] += balloons[n][m + 1]
    # pp(score)
    for n in range(N):
        for m in range(M):
            score[n][m] += balloons[n][m]
    # pp(score)
    
    best = []   # 최고점 
    for s in score: # 각 행의 최고점
        best.append(max(s))

    print(f'#{t} {max(best)}')