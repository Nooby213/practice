import sys

sys.stdin = open('input.txt')


def boyer_moore(pat, tgt):
    lps = {pat[idx]: len(pat) - 1 - idx for idx in range(len(pat))}  # 스킵 가능한 범위 기록
    print(lps)
    pat_idx = len(pat)
    tgt_idx = 0

    while tgt_idx <= len(tgt) - pat_idx:
        for p_idx in range(pat_idx - 1, -1, -1):
            if tgt[tgt_idx + p_idx] != pat[p_idx]:
                tgt_idx += lps[tgt[tgt_idx + p_idx]]
                tgt_idx += lps.get(tgt[tgt_idx + p_idx], len(pat))
                break   # 틀렸으니까 p_idx 다시 len(pat) - 1 되도록 조사종료
        else:
            return True
    return False
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0  # 들어있지 않다고 가정
    boyer_moore(str1, str2)
    if str1 in str2:
        result = 1
    print(f'#{tc} {result}')