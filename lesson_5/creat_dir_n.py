
import os

for i in range(1, 10):
    path = 'dir_{}'.format(i)
    if not os.path.exists(path):
        os.mkdir(path)



