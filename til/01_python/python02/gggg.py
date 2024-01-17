list_1 = [1, 2, 3, 4, 5, 6]
list_2 = list_1
sorted(list_1)
print(list_1)
print(list_2)

a = '1 5 4 2 3 6 7 8'
b = list(a.split())
c = a
a = '1 2 3 4 5 7 8 6'
b.sort()
sorted(a)
print(sorted(a))
print(b)   # 숫자만 표현
print(c)

qqq = '12333333'
bbb = list(qqq)
print(str(list(qqq)))
