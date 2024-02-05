import sys
sys.stdin = open('input.txt')

# 테스트 케이스
N = 10 

for i in range(1, N + 1):
    dump = int(input()) #  덤프 횟수
    tile = list(map(int, input().split()))  # 타일 리스트

    for d in range(dump):  # 덤프 한다.
        tile[tile.index(min(tile))] += 1    # 최솟값은 메꾸고
        tile[tile.index((max(tile)))] -= 1  # 최댓값은 깎고

    print(f'#{i} {max(tile) - min(tile)}')  # 최댓값과 최솟값 차이
