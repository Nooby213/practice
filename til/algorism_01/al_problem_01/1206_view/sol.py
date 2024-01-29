import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(10):
    N = int(input())
    building_list = list(map(int,input().split()))
    count_room = 0
    for k in range(2, N-2):
        near_by = [j for j in building_list[k-2 : k+3]]
        if (max(near_by) == building_list[k]):
            building = near_by[2]
            near_by.pop(2)
            count_room += building - max(near_by)
    print(f'#{i+1} {count_room}')