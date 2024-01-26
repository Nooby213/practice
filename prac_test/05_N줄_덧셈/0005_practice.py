import sys
sys.stdin = open('input.txt')

num = 0
N = int(input())

if N > 10000:
    print('10000이하의 숫자를 넣어주세요')
    N = int(input())

for i in range(1,N+1):
    num += i
    
print(num)