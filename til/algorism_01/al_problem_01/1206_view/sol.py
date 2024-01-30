import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 나의 풀이
# for i in range(10):
#     N = int(input())
#     building_list = list(map(int,input().split()))
#     count_room = 0
#     for k in range(2, N-2):
#         near_by = [j for j in building_list[k-2 : k+3]]
#         if (max(near_by) == building_list[k]):
#             building = near_by[2]
#             near_by.pop(2)
#             count_room += building - max(near_by)
#     print(f'#{i+1} {count_room}')


for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
      # 방법 1
#     # 최종 결과값 : 조망권 총 개수
#     # 전부 다 조사
#     # 앞, 뒤 2칸은 건물 없음이 조건 (조사 범위에서 앞, 뒤 2개씩 뺌
#     for i in range(2, N - 2):
#         # 임시 변수 i > data[i] 번째 조사 대상 건물을 말한다.
#         # 항상 5개씩 조사
#         # 각 건물의 최대 높이 255
#         min_value = 256
#         for j in range(5):
#             if j != 2:
#                 if data[i] - data[i - 2 + j] < min_value:
#                     min_value = data[i] - data[i - 2 + j]
#         if min_value > 0:
#             result += min_value
#     print(result)

# 조사 범위는 동일
#     for i in range(2, N-2):
#         # 임시 변수 i를 기준으로 5개의 범위선정
#        max_neighbor = 0
#        for j in range(i-2, i+3):
#            if i == j: continue
#            # j번째가 제일 큰 애들중에, 조사 대상 i보다 작은애들
#
#           # j번째 위치가 조사대상 i번째보다 크거나 같으면 무시
#            if data[j] < data[i] and max_neighbor < data[j]:
#                 max_neighbor = data[j]
#           # 주변 아파트가 조사대상보다 크다면 break
#            elif data[j] >= data[i]:
#                 max_neighbor = data[i]
#                 break
#     # 최종 결과값 = 나의 크기 - 내 이웃 중 제일 큰애
#     result = data[i] - max_neighbor
#           # # j번째 위치가 조사대상 i번째보다 작다면
#           # if data[j] < data[i]:
#           #       # 조사대상 크기 - j번째 아파트 크기
#           #       temp = data[i] - data[j]
#     print(result)