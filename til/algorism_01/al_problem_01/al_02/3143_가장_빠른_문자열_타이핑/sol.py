import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):  # 테스트 케이스
    A, B = input().split()  # A 는 문자열, B 는 타이핑 키

    # 횟수는 길이 + B 갯수 - (B의 길이 * B의 갯수)
    count_num = len(A) + A.count(B) - (len(B) * A.count(B))
    print(f'#{t} {count_num}')


