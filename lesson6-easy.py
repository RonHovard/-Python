# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def go(self):
        print("Let's go...")

    def stop(self):
        print('stop machine')

    def turn(self, course):
        if course == 'left':
            print('to turn left')
        elif course == 'right':
            print('to turn right')


# zhuk = TownCar('j7', 'yellow')
# zhuk.go()
# zhuk.turn('left')
# zhuk.turn('right')
# zhuk.stop()
# print(zhuk.color)

# wolk = TownCar()
# print(wolk.name)


class SportCar(TownCar):
    def __init__(self, name, color, speed):
        super(SportCar, self).__init__(name, color)
        self.speed = speed


class PoliceCar(TownCar):
    def __init__(self, name, color):
        super(PoliceCar, self).__init__(name, color)
        self.is_police()

    def is_police(self):
        print('Мау, мау, мау...')


policay = PoliceCar('ment', 'бело-голубой')

print(policay.color, policay.name)

