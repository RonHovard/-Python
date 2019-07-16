import os
import shutil
# импортирую функцию из модуля созданных при выполнении easy
from creat_dir_n import creation_dir

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('Добро пожаловать!')

while True:
    print('Меню доступных опций: ')
    print(" [1] - перейти в папку")
    print(" [2] - посмотреть содержимое текущей папки")
    print(" [3] - создать папку")
    print(" [4] - удалить папку")
    answer = int(input('Введите номер действия(для выхода введите 0): '))

    if answer == 1:
        folder_name = input('Введите имя папки: ')
        os.chdir(folder_name)
        print(f'Зашёл в папку{folder_name}')
    elif answer == 2:
        print(os.listdir())
    elif answer == 3:
        folder_name = input('Введите имя папки: ')
        creation_dir(folder_name, folder_name)
        print(f'папка: {folder_name}, успешно создана')
    elif answer == 4:
        folder_name = input('Введите имя папки: ')
        os.rmdir(folder_name)
        print(f'папка: {folder_name}, была удалена')
    elif answer == 0:
        break