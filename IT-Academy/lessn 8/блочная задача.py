import os


def meke_syper_star(string_my, stringer_blovc):
    list_string_my = string_my.lower().split()
    for i in range(len(list_string_my)):

        for j in range(len(stringer_blovc)):

            if stringer_blovc[j] in list_string_my[i]:
                list_string_my[i] = list_string_my[i].replace(stringer_blovc[j], len(stringer_blovc[j]) * '*')

    return ' '.join(list_string_my)


print(os.listdir())
with open(os.path.join('черный список слов'), 'r', encoding='utf-8') as file_blok:
    blok_words = file_blok.read().lower().split()

with open(os.path.join(input('Впиши сюда путь своего файла ')), 'r', encoding='utf-8') as song:
    list_of_string = song.readlines()
    new_list_of_string = []
    for i in list_of_string:
        if '\n' in i:
            new_list_of_string.append(i.replace('\n', ''))
stringer = ''
for i in new_list_of_string:
    stringer += f' {i}'

print()
print(meke_syper_star(stringer, blok_words))
