# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("{}, let's go...".format(self.name))

    def stop(self):
        print('{}, stop machine'.format(self.name))

    def turn(self, course):
        print('to turning {}'.format(course))


class TownCar(Car):
    pass


class SportCar(Car):
    def __init__(self, speed, color, name, turbo=True):
        super().__init__(speed, color, name)
        self.turbo = turbo


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def siren(self):
        print('May,May....')


my_town_car = PoliceCar(120, 'Белый', 'Гранта')

my_town_car.siren()
print(my_town_car.name)
