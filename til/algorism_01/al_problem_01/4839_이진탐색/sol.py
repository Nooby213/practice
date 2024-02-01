import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스

for t in range(1, T + 1):
    end_book, A, B = map(int, input().split())
    A_start = 1
    B_start = end_book
    A_count = 0
    B_count = 0
    # print(A,B)
    # print(A_start, B_start)

    # A 가 해당 페이지를 찾을 때까지 반복
    A_end = end_book
    A_middle = 0
    while A_middle != A:

        if int((A_start + A_end) / 2) < A:  # 중간값이 A 보다 작을 때
            A_start = int((A_start + A_end) / 2)
        else:   # 중간값이 A 보다 클 때
            A_end = int((A_start + A_end) / 2)

        A_middle = int((A_start + A_end) / 2)

        A_count += 1    # 카운팅
        # print(A_start, A_end, A_count)

    # B 가 해당 페이지를 찾을 때까지 반복
    B_end = 1 # B는 역순으로
    B_middle = 0
    while B_middle != B:    # 값 찾을때까지 반복

        if int((B_start + B_end) / 2) < B:  # 중간값이 B보다 작으면 중간값이 끝 값이 된다.
            B_end = int((B_start + B_end) / 2)
        else:
            B_start = int((B_start + B_end) / 2)

        B_middle = int((B_start + B_end) / 2)

        B_count += 1    # 카운팅
        # print(B_start, B_end, B_count)

    if A_count == B_count:  # 같으면 0
        print(f'#{t} 0')
    elif A_count < B_count: # 횟수 적은사람이 이김
        print(f'#{t} A')
    else:
        print(f'#{t} B')