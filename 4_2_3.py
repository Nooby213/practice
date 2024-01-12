def sum_of_digits(n):
    digits = [int(digit) for digit in str(n)]
    digit_sum = sum(digits)
    
    return digit_sum

number = 643

result = sum_of_digits(number)
print(f"{number}의 각 자릿수 합: {result}")
