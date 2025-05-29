import os

with open(os.path.join(input('Впиши сюда путь своего файла где спісок с белебердой ')), 'r', encoding='utf-8') as file:
    text_data=file.read()
text_data+=' '
suma_elem=0
number=''
for i in range(len(text_data)):
    if text_data[i].isdigit():
        number += text_data[i]
    else:
        if number != '':
            suma_elem += int(number)
            number = ''

print('Сумма всех чисел:', suma_elem)
