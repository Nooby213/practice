# 산술평균 : round(sum(N) / N, 1)
# 중앙값 : sum(N).sort[N//2]
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값   여러 개 있을 때는 두 번째로 작은 값 출력
# 범위 : max - min
N = int(input())
num_lst = [int(input()) for _ in range(N)]
num_lst.sort()
num_dict = {i: 0 for i in num_lst}

for k in num_lst:
    num_dict[k] += 1

print(int(round(sum(num_lst)/N, 0)))
print(num_lst[N//2])
mk = []
mv = 0
for k, v in num_dict.items():
    if v > mv:
        mv = v
for k in num_dict:
    if num_dict[k] == mv:
        mk.append(k)

if len(mk) > 1:
    print(mk[1])
else:
    print(mk[0])

print(num_lst[-1] - num_lst[0])
