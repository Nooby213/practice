import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    word = input()

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')
