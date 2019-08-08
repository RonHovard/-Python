
import os

#  Функция создаёт нумерованные, пустые директории. Принимает две переменные:
#  названия первой и последней дикектории (из списка директорий, который
#  нужно создать) в формате: name_number
#  , где name - имя, одинаковое для всех папок
#  number - порядковый номер папки, после _ (нижнего подчёркивания).
#  Например: creation_dir('dir_1', 'dir_9')
#  Для создания одной директории достаточно указать её имя в
#  поле для аргументов два раза через ",".
#  Например: creation_dir('dir', 'dir')


def creation_dir(a, b):
    try:
        name, start = a.split('_')
        start = int(start)
        end = int(b.split('_')[1]) + 1
        for i in range(start, end):
            path = '{}{}'.format(name, i)
            if not os.path.exists(path):
                os.mkdir(path)
    except ValueError:
        os.mkdir(a)


if __name__ == '__main__':
    creation_dir('dir_1', 'dir_9')
    creation_dir('dir', 'dir')

