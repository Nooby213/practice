import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(10):
    N = int(input())
    building_list = list(map(int,input().split()))
    for num in range(2, len(building_list) - 1):
        show_list = []
        for j in range(2):
            if building_list[num] - building_list[num - j] <= 0 or building_list[num] - building_list[num + j] <= 0:
                break
            else:
                building_list[num] - building_list[num - j]
                building_list[num] - building_list[num + j]

