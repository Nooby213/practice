import sys

sys.stdin = open('input.txt')


def KMP(pat, tgt):
    def make_lps():
        # 내 앞에 나와 동일한 패턴이 몇 번 나왔는지 세어주는 리스트
        lps = [0] * len(pat)
        for idx in range(1, len(pat)):  # 0 번 인덱스는 앞에 중복되는 값이 없음
            if pat[lps[idx - 1]] == pat[idx]:
                # 내 다음 조사 대상은, 내 위치 + 1 번째부터 조사하도록
                lps[idx + 1] = lps[idx - 1] + 1
        lps.insert(0, -1)
        return lps

    lps = make_lps()

    print(lps)
    pat_idx = 0
    tgt_idx = 0
    # 현재 조사 위치가 조사 대상의 범위를 벗어나기 전까지
    while tgt_idx < len(tgt):
        print(lps[pat_idx])
        print(tgt_idx, tgt[tgt_idx], pat_idx, pat[pat_idx])
        # 일치하지 않으면
        if pat[pat_idx] != tgt[tgt_idx]:
            pat_idx = lps[pat_idx]

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
    KMP(str1, str2)
    if str1 in str2:
        result = 1
    print(f'#{tc} {result}')
