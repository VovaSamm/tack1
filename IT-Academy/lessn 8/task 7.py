import os

with  open(os.path.join(input('Впиши сюда путь своего файла где спісок с белебердой ')), 'r', encoding='utf-8') as file:
    text_data=file.readlines()
new_text_data=[]
count=1
text_of_row=''
baza=0
for i in range(len(text_data)):
    for j in range(len(text_data[i])):
       baza = ord('A') if text_data[i][j].isupper() else ord('a')
       text_of_row += chr(baza+(ord(text_data[i][j])+count-baza)%26)
    new_text_data.append(text_of_row)
    text_of_row=''
    count+=1
print(new_text_data)
