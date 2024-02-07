import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    stack = []
    result = 1
    sent = input()
    if ('(' not in sent and '{' not in sent and '[' not in sent):
        result = 0

    else:
        for s in sent:
            if s in '({[':
                stack.append(s)
            elif s in ']})':
                if not stack:
                    result = 0
                    break
                else:
                    top = stack.pop()
                    if (s == ')' and top != '(') or (s == '}' and top != '{') or (s == ']' and top != '['):
                        result = 0

    if stack:
        result = 0
    print(f'#{t} {result}')
