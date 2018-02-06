#path = 'PycharmProjects/python/bme590s18_lecture03'
import os
x= os.listdir()
for files in x:
    print(files)
import glob
csvfiles=glob.glob('*.csv')
for i in csvfiles:
        print(i)
files_exclude= csvfiles.remove('mlp6.csv')
for i in csvfiles:
    print(i)