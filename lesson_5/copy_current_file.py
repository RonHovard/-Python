import os
import shutil

def copy_file(filename):
    # if os.path.isfile(filename):
    newfile = filename + '.copy'
    shutil.copy(filename, newfile)
    if os.path.exists(newfile):
        print("Файл ", newfile, " был успешно создан")
    else:
        print("Возникли проблемы копирования")


copy_file(os.path.abspath(__file__))
