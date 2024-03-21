import sys

sys.stdin = open('input.txt')
from heapq import heappop, heappush


def bfs():
    q = [(0, 0)]
    min_dis = 11 * E
    sum_weight = 0
    while q:
        weight, now = heappop(q)

        sum_weight += weight
        if now == N:
            min_dis = min(min_dis, sum_weight)

        for w, to in adj[now]:
            heappush(q, (w, to))

    return min_dis

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))

    print(f'#{t} {bfs()}')