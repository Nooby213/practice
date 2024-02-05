import sys

input = sys.stdin.readline

N = int(input())


# def lenth(alist):  # 길이 순서로 정렬
#     for a in range(len(alist)):
#         min_idx = a
#         for i in range(a + 1, len(alist)):
#             if len(alist[min_idx]) > len(alist[i]):
#                 min_idx = i
#         alist[a], alist[min_idx] = alist[min_idx], alist[a]
#     return alist


word_lst = [[input().rstrip()] for _ in range(N)]
# print(word_lst)
word_lst.sort()

for n in range(N):
    word_lst[n].append(len(word_lst[n][0]))

print(word_lst)
woo = sorted(word_lst, key=lambda word: word[1])    # 숫자 순서대로 정렬

# lenth(word_lst)
# print(woo)

for w in woo:   # 단어 나열
    print(w[0])
