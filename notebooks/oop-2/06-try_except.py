# try:
#     result = 10 / 0
# except ZeroDivisionError:  # 제로 디비전 일 때만 / 0으로 나눌 때만
#     print('0으로 나눌 수 없습니다.')

# try:
#     print(name)
# except:  # 어떠한 예외가 발생해도
#     print('0으로 나눌 수 없습니다.')

# try:
#     num = int(input('숫자 입력 : '))
# except ValueError:
#     print('숫자가 아닙니다.')

try:
    num = int(input('100을 나눌 숫자를 입력하시오. : '))
    100/num
# except BaseException:   # 부모 클래스는 밑으로 가야 됨
    # print('숫자를 넣어줘')
except ValueError:
    print('숫자가 아닙니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('알 수 없는 에러가 발생했습니다.')
