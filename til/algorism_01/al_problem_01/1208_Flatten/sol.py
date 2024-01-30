import sys
sys.stdin = open('input.txt')

N = 10
for i in range(1, 11):
    dump = int(input())
    tile = list(map(int, input().split()))

    for d in range(dump):
        tile[tile.index(min(tile))] += 1
        tile[tile.index((max(tile)))] -= 1

    print(f'#{i} {max(tile) - min(tile)}')
