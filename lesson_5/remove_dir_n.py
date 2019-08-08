import os

# Функция удаляет нумерованные, пустые директории. Принимает две переменные:
#  названия первой и последней дикектории (из списка директорий,
#  которые нужно удалить) в формате: name_number
# ,где name - имя, одинаковое для всех папок
#  number - порядковый номер папки, после _ (нижнего подчёркивания).
#  Например: dir_1 и dir_9


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
