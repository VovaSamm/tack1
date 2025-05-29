import os
import shutil

print('Window' if os.name == 'nt' else 'Not windows')
print(os.getcwd())
os.chdir('C:/Users/Марина/PycharmProjects/test/IT-Academy/lesson 9/pool')
list_file_and_foldef = os.listdir()
print(list_file_and_foldef)
sorse_patg = ''
coint=0
data_file=0
for i in list_file_and_foldef:
    sorse_patg = os.path.join(i)
    coint += 1
    data_file += os.path.getsize(sorse_patg)
    if os.path.isfile(i) and os.path.exists(i) == False:
        os.mkdir(i.split('.')[-1])
        folder = i.split('.')[-1]

        shutil.move(sorse_patg, os.path.join(folder))
    elif os.path.isfile(i) and os.path.exists(i) == True:
        folder = i.split('.')[-1]

        shutil.move(sorse_patg, os.path.join(folder))
for i in list_file_and_foldef:
    number_of_filse=len(os.listdir(i))
    data=0
    for j in os.listdir(i):
        new_path = os.path.join(i, f'1{j}')
        os.rename(os.path.join(i, j), new_path)
        print(f' файл {j}  был переіменован в {new_path}')

        data=os.path.getsize(os.path.join(i))


    print(f'Размер {data} байт, количество файлов {number_of_filse}')