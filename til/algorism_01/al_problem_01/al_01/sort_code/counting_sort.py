# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세어
# 선형 시간에 정렬하는 효율적인 알고리즘
# 정수나 정수로 표현할 수 있는 자료에만 적용 가능
# 집합 내의 가장 큰 정수를 알아야한다.
# 시간 복잡도 : O(n + k) : n은 리스트의 길이, k는 정수의 최댓값

# counts 배열에 기록하기
N = 6   # 원소 갯수
K = 9   # 0 ~ k
data = [7, 2, 7, 5, 7, 3] # 0 ~ 9 , K = 9
counts = [0] * (K+1) # 최댓값 + 1 (인덱스는 -1 이기때문에)
temp = [0] * N  # 정렬된 결과 저장
# 인덱스에 횟수 기록하기
for x in data:
    counts[x] += 1
# counts 누접합 구하기
for i in range(1, K+1):
    counts[i] += counts[i-1]


# data의 마지막 원소부터 정렬하기
for i in range(N-1, -1, -1): # N-1 > 0번 인덱스 
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]
    # print(counts)
    # print(temp)
print(*temp)

# data의 첫 원소부터 정렬하기
# for i in range(N): # N-1 > 0번 인덱스 
#     counts[data[i]] -= 1
#     temp[counts[data[i]]] = data[i]
#     print(counts)
#     print(temp)
# print(*temp)

# 숫자가 여러 개 있을 때
c = len(counts) - 1
while c != 0:
    while counts[c] != counts[c - 1]:
        data[counts[c] - 1] = c
        counts[c] -= 1
        # print(counts)
        # print(data)
    c -= 1