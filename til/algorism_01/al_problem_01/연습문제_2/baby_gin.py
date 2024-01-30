'''
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때,
3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고
3장의 카드가 동일한 번호를 갖는 경우를 triplet이라 한다.


6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin이라 한다.

6자리의 숫자를 입력받아 baby-gin 여부를 판단하는 프로그램을 작성하라
'''

num_list = [int(i) for i in str(input())]
# num_dict ={str(i) : 0 for i in num_list}
num_dict ={l : 0 for l in num_list}
for j in num_list:
    if num_list.count(j) == 6:  # triplet 2개
        print('baby-gin')
        break

    elif 3 <= num_list.count(j) <6: # triplet 2개/ triplet 1개, run 1개
        num_copy = num_list.copy()
        for _ in range(3):
            num_copy.remove(j)
        num_copy.sort()
        if num_copy[1] * 3 == sum(num_copy):
            print('baby-gin')
            break
    
    else:   # run 2개
        if len(num_dict) == 3: 
            num_list.sort()
            if num_list[1] * 3 == sum(num_list):
                print('baby-gin')
                break

        elif len(num_dict) == 4: 
            num_list.sort()
            if num_list[1] * 3 == sum(num_list[:2],num_list[3]):
                print('baby-gin')
                break

        elif (len(num_dict) == 5) or (len(num_dict) == 6): 
            num_list.sort()
            if num_list[1] * 3 == sum(num_list[:3]) and num_list[4] * 3 == sum(num_list[3:]):
                print('baby-gin')
                break









# if len(num_dict) == 1 or len(num_dict) == 2:    # triplet 2개
#     print('baby-gin')

# elif len(num_dict) == 3 or len(num_dict) == 4:  # trilpet 1개 run 1개
#     for num in num_list:
#         num_dict[str(num)] += 1

#     for key, value in num_dict.items():
#         if value % 3 == 0:
#             key_list = [int(j) for j in num_dict.keys()]
#             key_list.remove(int(key))
#             key_list.sort()
#             if sum(key_list) == (key_list[1] * 3):
#                 print('baby-gin')
#                 break
#         else:
#             key_list = [int(k) for k in num_dict.keys()]
#             key_list.sort()
#             if sum(key_list) == (key_list[1] * 3):
#                 print('baby-gin')
#                 break

# else:








# if len(set(num_list)) == 1 or len(set(num_list)) == 2: # triplet 2개
#     print('baby-gin')
# # run 1개 triplet 1개
# num_list.sort()
# print(num_list)

