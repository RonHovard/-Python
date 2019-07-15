import os

lst_f = list()
for i in os.listdir():
    if not os.path.isfile(i):
        lst_f.append(i)

print(lst_f)
