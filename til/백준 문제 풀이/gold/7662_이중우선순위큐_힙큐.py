import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    # 연산할 숫자 갯수, k ≤ 1,000,000
    k = int(input())
    # I는 삽입, D는 삭제 : 1 은 최대, -1 최소, 큐가 비어있으면 무시
    # 비어있으면 EMPTY, 최대, 최소 출력
    q = []
    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heappush(q, num)

        if command == 'D':
            if q:
                if num == -1:
                    heappop(q)
                else:
                    q.sort()
                    q.pop()
    if q:
        print(max(q), min(q))
    else:
        print('EMPTY')
