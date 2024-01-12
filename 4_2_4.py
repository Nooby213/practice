score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
stem_leaf=[[0, 0, 2, 4, 7, 7, 9],[1, 1, 3, 8],[0]]
def qq():
    for i in stem_leaf:
        print(i)
def p_stem():
    x = int(input('숫자를 입력하시오.'))
    print(stem_leaf[x])
p_stem()