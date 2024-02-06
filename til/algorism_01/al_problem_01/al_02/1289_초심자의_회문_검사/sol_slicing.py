import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    word = input()
    reword = ''.join(reversed(word))
    if word == reword:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
