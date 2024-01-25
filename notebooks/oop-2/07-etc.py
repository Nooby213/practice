# 딕셔너리에서 키를 조회할 때
# 키가 없다는 상황을 가정한다.
my_dict = {}

# try-except  # 웹서버 만들고 구동할 때 / 일단 서버 실행하고 문제해결 할 때 사용한다.
try: # 일단 찾아
    result = my_dict['a']
    print(result)
except KeyError: # 없으면 처리해
    print('Key가 존재하지 않습니다.') # 처리하고 가

# if-else  # 문제 해결
if 'a' in my_dict: # 없으면 브레이크 밟아, 있으면 확인해줘
    resutl = my_dict['a'] # 키 할당
else:
    print('Key가 존재하지 않습니다.')