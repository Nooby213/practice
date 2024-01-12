# 소수란 자기 자신과 1로만 나누어 지는 수
L = list(range(2,30))
print(L)

    
i = 0
while i < len(L):
    if L[i] != 2:
        j = 2
        while j < L[i]:
            if L[i] % j == 0:
                L.remove(L[i])
            else:
                j += 1
    i += 1


