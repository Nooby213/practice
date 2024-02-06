import sys

sys.stdin = open('input.txt')
def brute_force(pat, tgt):
    pat_idx = 0
    tgt_idx= 0
    # 현재 조사 위치가 조사 대상의 범위를 벗어나기 전까지
    while tgt_idx < len(tgt):
        # 일치하지 않으면
        if pat[pat_idx] != tgt[tgt_idx]:
            pat_idx -= 1

        # 일치하면
        tgt_idx += 1
        pat_idx += 1

        # 패턴의 끝까지 index가 증가했다
        # > target과 patten이 일치하는 부분 없이
        # 패턴의 끝까지 조사했다.
        if pat_idx == len(pat):
            return True
    return False

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0  # 들어있지 않다고 가정
    if str1 in str2:
        result = 1
    print(f'#{tc} {result}')
