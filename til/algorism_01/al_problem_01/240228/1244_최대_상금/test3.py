import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # N 자리수 1 <= N <= 6, 교환 횟수 M번 1 <= M <= 10
    N, M = map(int, input().split())
    num = list(str(N))
    num_len = len(num)

    for _ in range(M):
        max_digit = max(num)
        max_index = num_len - 1 - num[::-1].index(max_digit)
        if max_index != 0:
            # 가장 큰 숫자를 가장 앞으로 이동
            num[0], num[max_index] = num[max_index], num[0]
        else:
            # 이미 가장 큰 숫자가 맨 앞에 있으면 다음으로 큰 숫자로 넘어감
            max_digit = max(num[1:])
            max_index = num.index(max_digit, 1)
            num[1], num[max_index] = num[max_index], num[1]

    result = int(''.join(num))
    print(f'#{t} {result}')
