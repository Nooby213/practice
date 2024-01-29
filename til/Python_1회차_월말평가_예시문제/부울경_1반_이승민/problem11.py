############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if 1 == matrix[i][j]:   # 처음 위치 찾기
                x = j
                y = i

    for move in move_list:
        if move == 0:     # 0 은 위쪽
            y -= 1
        elif move == 1:   # 1 은 아래
            y += 1     
        elif move == 2:   # 2 는 왼쪽
            x -= 1
        elif move == 3:    # 3 은 오른쪽
            x += 1
        if x < 0  or y < 0 or x > N or y > N: # 장외로 나갈시 None 리턴
            return None
        
    return [y, x]
    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
