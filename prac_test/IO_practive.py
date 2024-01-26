data = list(map(int,input('숫자 2개를 입력하시오').split()))
sum_of_digit = 0
for num in data:
    print(num)
    sum_of_digit += num
print(sum_of_digit)
