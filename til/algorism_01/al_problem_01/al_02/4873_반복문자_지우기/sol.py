import sys
sys.stdin = open('input.txt')

# 반복 문자 s 지운다.
# 지워진 부분은 다시 앞뒤를 연결
# 연결해서 생기면 또 지운다.
# 다 지운 후 남는 길이 출력 없으면 0

T = int(input())

for t in range(1, T+1):
    word = list(input())

    i = 0
    while len(word) > 1 and i < len(word) - 1:
        if word[i] == word[i + 1] and i != 0:
            word.pop(i)
            word.pop(i)
            i -= 1
        elif word[i] == word[i + 1] and i == 0:
            word.pop(i)
            word.pop(i)
        else:
            i += 1
    print(f'#{t} {len(word)}')
