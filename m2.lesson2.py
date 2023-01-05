class Max:
    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f'name is {self.name} \n' \
                f'age is {self.age}'
pu = Max('akerov alim', 14)
print(pu)

class Func:
    def x2(self):
        print(self * 2)
Func.x2(pu.age)