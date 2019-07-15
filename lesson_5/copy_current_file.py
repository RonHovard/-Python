import os
import shutil

def copy_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.copy'
        shutil.copy(filename, newfile)      #копируй
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False


copy_file(os.path.abspath(__file__))
