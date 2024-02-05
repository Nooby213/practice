import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for n in range(N):
    lenth_list, num_count = map(int,input().split())
    num_list = list(map(int,input().split()))
    sum_of_num = []
    for i in range(lenth_list - num_count + 1):
        sum_of_num.append(sum(num_list[i:i+num_count]))
    print(f'#{n+1} {max(sum_of_num) - min(sum_of_num)}')