import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 갯수

for t in range(1, T + 1):
    N, M = map(int, input().split()) # N * M  배열
    balloons = []
    for n in range(N): # 풍선 판 만들기
        m_list = list(map(int, input().split()))
        balloons.append(m_list)
    # print(balloons)

    scores = []
    for n in range(N): # 풍선 터뜨렸을 때 최댓값
        for m in range(M):
            if m < 0:
            elif m == M # if m = 0 으로 값지정 a =balloons[n-1][m]
                score = balloons[n][m] + balloons[n -1][m] + balloons[n + 1][m] + balloons[n][m - 1] + balloons[n][m + 1]
                scores.append(score)
    print(f'#{t} {max(scores)}')