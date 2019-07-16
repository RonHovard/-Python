import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#  Функция создаёт нумерованные, пустые директории. Принимает две переменные:
#   названия первой и последней дикектории (из списка директорий, который
#   нужно создать) в формате: name_number
#   , где name - имя, одинаковое для всех папок
#  number - порядковый номер папки, после _ (нижнего подчёркивания).
#  Например: creation_dir('dir_1', 'dir_9')


def creation_dir(a, b):
    name, start = a.split('_')
    start = int(start)
    end = int(b.split('_')[1]) + 1
    for i in range(start, end):
        path = '{}{}'.format(name, i)
        if not os.path.exists(path):
            os.mkdir(path)


if __name__ == '__main__':
    creation_dir('dir_1', 'dir_9')

# Функция удаляет нумерованные, пустые директории. Принимает две переменные:
#  названия первой и последней дикектории (из списка директорий,
#  которые нужно удалить) в формате: name_number
# ,где name - имя, одинаковое для всех папок
#  number - порядковый номер папки, после _ (нижнего подчёркивания).
#  Например: remove_dir('dir_1', 'dir_9')


def remove_dir(a, b):
    name, start = a.split('_')
    start = int(start)
    end = int(b.split('_')[1]) + 1
    for i in range(start, end):
        path = '{}{}'.format(name, i)
        if os.path.exists(path):
            os.rmdir(path)


if __name__ == '__main__':
    remove_dir('dir_1', 'dir_9')
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Функция возвращает список папок в текущей директории


def lst_folders():
    lst_f = list()
    for i in os.listdir():
        if not os.path.isfile(i):
            lst_f.append(i)
    return lst_f


if __name__ == '__main__':
    print(lst_folders())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# Функция создаёт копию файла, из которого была запущена.


def copy_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.copy'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print(f"Файл {newfile} был успешно создан")
        else:
            print("Возникли проблемы при копировании")


if __name__ == '__main__':
    copy_file(os.path.abspath(__file__))
