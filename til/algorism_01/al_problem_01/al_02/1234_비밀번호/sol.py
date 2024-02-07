import sys

sys.stdin = open('input.txt')


class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, num):
        self.top += 1
        self.data[self.top] = num

    def pop(self):
        if self.is_empty():
            pass
        else:
            self.top -= 1
            return self.data[self.top + 1]

    def __str__(self):  # instance print 했을 때, stack안의 data를 바로 출력
        return f'{self.data}'

    def is_empty(self):
        return self.top == -1


for t in range(1, 11):
    N, P = input().split()  # N 길이, P는 비밀번호
    # P = list(P)
    N = int(N)
    stack = Stack(len(P))
    # print(stack)

    for i in range(len(P)):
        if i == 0:
            stack.push(P[i])
        elif P[i] == stack.data[stack.top]:
            stack.pop()
        else:
            stack.push(P[i])

    print(f'#{t}', end=' ')
    print(''.join(stack.data[:stack.top+1]))
