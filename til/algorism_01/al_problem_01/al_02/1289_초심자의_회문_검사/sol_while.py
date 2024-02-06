import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    word = input()
    i = len(word) // 2
    while i > 0:
        if word[i] != word[len(word) - i - 1]:
            print(f'#{t} 0')
            break
        i -= 1
    else:
        print(f'#{t} 1')
