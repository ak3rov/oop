class Age:
    def __init__(self, age):
        self.age = age
class Name(Age):
    def __init__(self, name):
        self.name = name

class M1:
    def r(self):
        print(f'cтолько лет методу: {self.name}')

class M2:
    def f(self):
        print(f'имя метода: {self.age}')

class All(M2, M1, Name, Age):
    def __init__(self, name ,age):
        Age.__init__(self, name)
        Name.__init__(self, age)

j = All('Nursaid', 14)
j.f()
j.r()
