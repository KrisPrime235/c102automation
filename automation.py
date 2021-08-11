import os
import shutil

path1 = '/Users/dineshsharma/Desktop/Coding/Python Programs'
fileList = os.listdir(path1)

for file in fileList:
    name,ext = os.path.splitext(file)
    ext = ext[1:]

    if ext == '':
        continue

    if os.path.exists(path1 + '/' + ext):
        shutil.move(path1 + '/' + file, path1 + '/' + ext + '/' + file)

    else:
        os.makedirs(path1 + '/' + ext)
        shutil.move(path1 + '/' + file, path1 + '/' + ext + '/' + file)
