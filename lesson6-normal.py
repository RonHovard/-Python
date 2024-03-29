# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health=100, armor=2, damage=10):
        self._name = name
        self._health = health
        self._armor = armor
        self._damage = damage
        self._lvl = 1

    def get_health(self):
        return self._health

    def get_armor(self):
        return self._armor

    def get_damage(self):
        return self._damage

    def _set_health(self, value):
        self._health = value

    def hit(self, damage):
        self._set_health(self._health - damage)

    def _calculate_damage(self, enemy):
        return self._damage / enemy.get_armor()

    def attack(self, enemy):
        damage = self._calculate_damage(enemy)
        enemy.hit(damage)


class Player(Person):
    pass


class Enemy(Person):
    def __init__(self, name, lvl):
        super().__init__(name)
        self._lvl = lvl
        self._health *= lvl
        self._armor *= lvl
        self._damage *= lvl


class Game:
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy

    def start(self):
        last_attacker = self._player
        while self._player.get_health() > 0 and self._enemy.get_health() > 0:
            if last_attacker == self._player:
                self._enemy.attack(self._player)
                last_attacker = self._enemy
            else:
                self._player.attack(self._enemy)
                last_attacker = self._player
        if self._player.get_health() > 0:
            print('Победил игрок! {}'.format(self._player._name))
        else:
            print('Победил враг!')


pl = Player('Batman', 500, 10, 50)
en = Enemy('Joker', 3)
battle = Game(pl, en)
battle.start()





