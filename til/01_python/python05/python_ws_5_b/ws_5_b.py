data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''

# 아래에 코드를 작성하시오.
for data in data_1:
    if data.isupper() == True or data == " ":
        print(data, end='')
    else:
        continue

print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

str_list = list(map(str,'내힘들다'))
for word in str_list:
    arr.append(data_2.find(word))
print(arr)
arr.sort()
print(arr)
for arr_index in arr:
    print(data_2[arr_index],end='')
