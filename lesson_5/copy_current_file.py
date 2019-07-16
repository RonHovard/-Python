import os
import shutil

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
