# 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
# 시간 복잡도 : O(n^2)

# 오름차순
# 정렬할 리스트 alist, 원소의 갯수 N
def bubble_sort(alist, N):
     # 범위의 끝 위치 
    for i in range(N - 1, 0, -1):  
        for j in range(0, i):    # 탐색 범위 축소 (매번 최댓값이 끝으로 가기때문에)
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]