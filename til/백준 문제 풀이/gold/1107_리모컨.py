# +, -, 0에서는 채널 안 바뀜
# 버튼 최소 몇 번 눌러야됨
# 현재 채널 100 > 채널 N으로 이동, 0 ≤ N ≤ 500,000
N = input()
# 고장난 버튼 M개, 0 ≤ M ≤ 10
M = int(input())
# 고장난 버튼
broken = list(map(str, input().split()))
goal = list(i for i in N)
now = 100
temp_channel = ''
cnt = 0
updn_cnt = abs(int(N) - now)

for i in N:
    cnt += 1
    if i not in broken:
        temp_channel += i
    else:
        j = int(i) - 1
        k = int(i) + 1
        if 0 <= j < 10 and str(j) not in broken:
            temp_channel += str(j)
            continue
        elif 0 <= k < 10 and str(k) not in broken:
            temp_channel += str(k)
            continue
        while (0 <= j < 10 and str(j) in broken) or (0 <= k < 10 and str(k) in broken):
            j -= 1
            k += 1
            if 0 <= j < 10 and str(j) not in broken:
                temp_channel += str(j)
                break
            elif 0 <= k < 10 and str(k) not in broken:
                temp_channel += str(k)
                break
else:
    cnt += abs(int(temp_channel) - int(N))

print(min(updn_cnt, cnt))
