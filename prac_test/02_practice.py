class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.place = (x, y)

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.a, self.b = self.p1.place
        self.c, self.d = self.p2.place

    def show_alpha(self):
        print(p1.place)
        print(p2.place)
        print(self.a, self.b, self.c, self.d)

    def get_area(self):
        print(abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y))
    
    def get_perimeter(self):
        print((abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y)) * 2)
    
    def is_square(self):
        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):
            print('정사각형입니다.')
        else:
            print('정사각형이 아닙니다')
    
p1 = Point(1, 3)
p2 = Point(3, 1)

r1 = Rectangle(p1, p2)
r1.get_area()
r1.get_perimeter()
r1.is_square()
r1.show_alpha()