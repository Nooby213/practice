def plus_(a,b):
    a, b = map(int,input().split())
    print(a + b)
    return plus_()
try:
    plus_()
except ValueError:
    pass