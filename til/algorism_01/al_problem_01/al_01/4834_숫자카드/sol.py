import sys
sys.stdin = open('input.txt')

N = int(input())    # 테스트 횟수
for n in range(N):  # N 번만큼 실행
    num_list = [0 for _ in range(10)]   # 숫자를 인덱스 값으로 받고 인자가 나온 횟수인 리스트
    M = int(input())    #  숫자 길이
    for c in input():   # input 값이 str type 이기때문에 순회가능하다
        num_list[int(c)] += 1   # 숫자가 있다면 num_list 에 기록
        # 최댓값을 찾아야되며 같을 경우 큰 숫자를 받아야 하기 때문에 뒤에서 부터 출력하며,
        # 뒤집어서 출력하기 때문에 인덱스값도 역순이라 9에서 출발
    print(f'#{n+1} {9 - num_list[::-1].index(max(num_list))} {max(num_list)}')


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 문자열 > iterable
#     ai = list(map(int, input()))
#     # 각 정수가 나온 횟수를 세기 위한 리스트
#     counting_list = [0 for _ in range(10)]
#
#     # 데이터 전체 순회하며 카운팅
#     for num in ai:
#         counting_list[num] += 1
#
#     max_count = 0   # 보유 개수
#     result = 0  # 카드 번호
#     # 0~9 전부 순회
#     for i in range(10):
#         # 보유 개수가 많거나 같다면
#         # 같다면 > 카드 번호가 더 큰 것
#         if max_count <= counting_list[i]:
#             max_count = counting_list[i]
#
#     print()