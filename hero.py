class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return f'Имя героя:{self.name}'

    def double_health(self):
        self.health_points *= 2
        return f'Удвоенное здоровье:{self.health_points}'

    def __str__(self):
        return f'Прозвище:{self.nickname},\n' \
               f'Суперспособность:{self.superpower},\n' \
               f'Текущее здоровье:{self.health_points}'

    def __len__(self):
        len({self.catchphrase})


hero = SuperHero('Tick', 'Boss', 'speed', 100, 'go on!')
print(hero.get_name())
print(hero.double_health())
print(hero)
print(f'Длина фразы:{len(hero.catchphrase)}')


class Sups(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=0, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        print(f'Здоровье Аватара x2: {self.health_points * self.health_points}')
        self.fly = True

    def crit_hero(self):
        print(f'Урон Аватара x2: {self.damage * self.damage}')

    def fly_phrase(self):
        if self.fly_phrase:
            print('fly in the True_phrase')

    def hp(self):
        print(f'Здоровье Тайм Мастера x2: {self.health_points * self.damage}')
        self.fly = True

    def critt(self):
        print(f'Урон Тайм Мастера x2: {self.damage * self.damage}')

    def fly_phras(self):
        if self.fly_phrase:
            print('fly in the True_phrase')

    def double_hp(self):
        print(f'Здоровье Бумa x2: {self.health_points * self.health_points}')
        self.fly = True

    def crit(self):
        print(f'Урон Бума x2: {self.damage * self.damage}')

    def gen_x(self):
        pass

    class First_hero(SuperHero):
        people = 'people'

    class Scond_hero(SuperHero):
        people = 'people'

    class Villian(SuperHero):
        people = 'monster'



first_hero = Sups('Aang', 'Avatar', 'elements', 100, 'I"m an Avatar!', 100)
second_hero = Sups('Time Master', 'time', 100, 'I"ve no Time!', 100)
villian = Sups('Cosmo', 'Boom', 'Bombs', 100, 'uhaha!', 50)

print(first_hero.double_health())
print(first_hero.crit_hero())
print(first_hero.fly_phrase())

print(second_hero.hp())
print(second_hero.critt())
print(second_hero.fly_phras())

print(villian.double_hp())
print(villian.crit())

