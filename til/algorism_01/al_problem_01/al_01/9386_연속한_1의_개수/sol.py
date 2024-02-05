import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for t in range(1, T + 1):
    N = int(input()) # 숫자 갯수
    num_list = list(map(str,input().split('0'))) # 0 을 기준으로 자른다.
    # print(num_list)
    max_lenth = 0   # 자른 숫자의 최대 길이 초기화
    for num in num_list:    # 리스트 원소가 숫자라면 길이 측정 후 최댓값 비교하여 저장
        if num.isdecimal() and len(num) > max_lenth:
            max_lenth = len(num)
    
    print(f'#{t} {max_lenth}')
    