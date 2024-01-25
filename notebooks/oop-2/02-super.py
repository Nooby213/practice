class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id


class Student2(Person):
    def __init__(self, name, age, number, email,student_id):
        super().__init__(name, age, number, email)
        # Person.__init__(name, age, number, email) # 다중 상속일 때 상속 순서 결정을 수퍼가 해줄 수 있다.
        self.student_id = student_id