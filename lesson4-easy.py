# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [2, 4, 6, 12, 7, 5, 88]
new_numbers = [i ** 2 for i in numbers]
print(new_numbers)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['apple', 'banana', 'grapes', 'mango', 'orange', 'plum']
fruits_2 = ['lemon', 'banana', 'grapes', 'plum', 'peach']
# same_fruits = list(set(fruits_1) & set(fruits_2))
same_fruits = [i for i in fruits_1 if i in fruits_2]
print(same_fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

# numbers = [45, 4, 15, 33, -8, 120, 10, 897, -55, 1, -100]
numbers = [random.randint(-100, 100) for _ in range(100)]
# new_numbers = []
# for i in numbers:
#     if i % 3 == 0:
#         if i > 0:
#             if i % 4 != 0:
#                 new_numbers.append(i)
# for i in numbers:
print(numbers)
new_numbers = [i for i in numbers if i % 3 == 0 and i > 0 and i % 4 != 0]
print(new_numbers)
