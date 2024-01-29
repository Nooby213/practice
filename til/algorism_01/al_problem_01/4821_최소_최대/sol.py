import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for n in range(N):
    lenth_list = int(input())
    num_list = list(map(int, input().split()))
    print(f'#{n+1} {max(num_list) - min(num_list)}')

