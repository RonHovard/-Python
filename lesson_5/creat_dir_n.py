
import os

#  Функция создаёт нумерованные, пустые директории. Принимает две переменные:
#  названия первой и последней дикектории (из списка директорий, который
#  нужно создать) в формате: 'name_number'
#  , где name - имя, одинаковое для всех папок
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



