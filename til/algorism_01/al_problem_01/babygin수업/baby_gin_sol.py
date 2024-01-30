# num = int(input())
num = 456789
c = [0] * 12 # 카운트 배열과 뒤에 더미 2개 (run 조사하기 위해 더미 2개)
for i in range(6):  # 숫자가 몇 자린지 모른다면 while num >0:
    c[num % 10] += 1 # 각 자릿수를 알아내기 위한 연산
    num //= 10
# print(c)
j = 0
tri = run = 0
while j < 10:
    if c[j] >= 3: # triplete 조사휘 데이터 삭제
        c[j] -= 3
        tri += 1
        continue
    if c[j] >= 1 and c[j+1] >= 1 and c[j+2] >= 1: # run 조사 후 데이터 삭제
        c[j] -= 1
        c[j+1] -= 1
        c[j+2] -= 1
        run += 1
        # print(c)
        continue
    j += 1
if run + tri == 2:
    print('Baby Gin')
else:
        print('Lose')