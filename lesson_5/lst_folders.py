import os

# Функция возвращает список папок в текущей директории


def lst_folders():
    lst_f = list()
    for i in os.listdir():
        if not os.path.isfile(i):
            lst_f.append(i)
    return lst_f


if __name__ == '__main__':
    print(lst_folders())
