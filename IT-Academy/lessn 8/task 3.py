import os

print(os.listdir())
print(os.path.join(os.listdir()[3]))
ignor_simbol = [',', ':', '"']
with open(os.path.join(os.listdir()[-2]), 'r', encoding='utf-8') as song:
    list_of_string = song.readlines()
    new_list_of_string = []
    for i in list_of_string:
        if '\n' in i:
            new_list_of_string.append(i.replace('\n', ''))
    for i in new_list_of_string:
        for j in range(len((ignor_simbol))):
            if ignor_simbol[j] in i:
                new = i.replace(ignor_simbol[j], '')

                new_list_of_string.remove(i)
                new_list_of_string.append(new)
list_alon_words_count_in_string = []
for i in new_list_of_string:
    list_alon_words_count_in_string.append(i.lower().split())
print(list_alon_words_count_in_string)
for i in list_alon_words_count_in_string:
    print('Следуюўая строка')
    for j in i:
        print(f'Количество слов в строке {i.count(j)}, слово в строке - {j}')

list_alon_words = []
for i in new_list_of_string:
    list_alon_words.extend(i.lower().split())

dict_of_words = {i: list_alon_words.count(i) for i in list_alon_words}
count_max_words = 0
max_words = ''
for i in dict_of_words:
    if dict_of_words[i] > count_max_words:
        max_words = i
        count_max_words = dict_of_words[i]
print(dict_of_words[max_words], max_words)