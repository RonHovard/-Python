import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def mk_dir(path):
    try:
        os.mkdir(path)
        print('Директория успешно создана')
    except FileExistsError:
        print('Директория уже существует')
    except PermissionError:
        print('Недостаточно прав для создания директории')


def rm_dir(path):
    try:
        os.removedirs(path)
        print('Директория успешно удалена')
    except FileNotFoundError:
        print('Такой папки не существует')
    except PermissionError:
        print('Недостаточно прав для удаления директории')




# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Функция возвращает список папок в текущей директории


def list_dir():
    lst_folder = [i for i in os.listdir() if os.path.isdir(i)]
    return lst_folder


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(filename):
    if os.path.isfile(filename):
        name, extension = filename.split('.')
        newfile = name + '_copy.' + extension
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print(f"Файл {newfile} был успешно создан")
        else:
            print("Возникли проблемы при копировании")


if __name__ == '__main__':
    dir_path = 'dir_{}'
    [mk_dir(dir_path.format(i)) for i in range(1, 10)]
    [rm_dir(dir_path.format(i)) for i in range(1, 10)]
    print(list_dir())
    copy_file(__file__)
