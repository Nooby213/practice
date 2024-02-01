import sys
sys.stdin = open('input.txt')

T = int(input())    # 테스트 케이스

for t in range(1, T + 1):
    # N은 숫자 갯수
    N = int(input())
    # 숫자들을 리스트에 받고 정렬한다.
    alist = list(map(int, input().split()))
    alist.sort()
    # 정렬된 숫자를 담기위한 빈 리스트를 만든다.
    sort_list = []

    # 최대, 최소값을 구한뒤 원래 리스트에서 제거시킨다.
    for _ in range(int(5)): 
        sort_list.append(max(alist))
        alist.pop(-1)
        sort_list.append(min(alist))
        alist.pop(0)
    

    print(f'#{t} ',end='')
    for i in sort_list:
        print(i,end=' ')
    print()