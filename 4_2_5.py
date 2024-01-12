def sum_of_digits():
    x = list(input('숫자를 입력하시오.'))
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    print(f'숫자의 합은 {sum}')
sum_of_digits()

def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))