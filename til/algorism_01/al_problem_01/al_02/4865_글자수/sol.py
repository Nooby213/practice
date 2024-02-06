import sys

sys.stdin = open('input.txt')

T = int(input())

# str1 의 단어중 str2에 포함되어 있는 개수 > 최대 출력

for t in range(1, T + 1):
    wordict = {c: 0 for c in input()}  # input 각 단어를 키로 하고 갯수를 세는 딕셔너리

    for w in input():  # 딕셔너리 돌면서 단어가 있으면 카운트
        if w in wordict:
            wordict[w] += 1

    count = 0  # 최대 카운트 값
    for word in wordict:  # 단어당 갯수 비교
        if wordict[word] > count:
            count = wordict[word]

    print(f'#{t} {count}')
