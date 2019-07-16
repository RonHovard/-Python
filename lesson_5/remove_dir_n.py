import os

for i in range(1, 10):
    path_2 = 'dir_{}'.format(i)
    if os.path.exists(path_2):
        os.rmdir(path_2)

