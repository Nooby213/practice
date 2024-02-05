import sys
sys.stdin = open('input.txt')

for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
 
    for i in range(100):
        if ladder[99][i] == 2:  # 2번인 곳 부터 출발
            x = i
            j = 98
            while j != 0:  # 밑에서부터 타고 올라간다
                if x > 0 and ladder[j][x - 1] == 1: # 0 < x 일 때는 out of range
                    while x > 0 and ladder[j][x - 1] == 1:
                        x -= 1
                    j -= 1
                elif x < 99 and ladder[j][x + 1] == 1: #99 > x 일 때는 out of range
                    while x < 99 and ladder[j][x + 1] == 1:
                        x += 1
                    j -= 1
                else:
                    j -= 1
                # print(j,x)
            print(f'#{T} {x}')