import os

with open(os.path.join(input('Впиши сюда путь своего файла где спісак дітей ')), 'r', encoding='utf-8') as song:
    text_children=song.readlines()

for i in range(len(text_children)):
    text_children[i]=text_children[i].replace('\n','')
    if text_children[i][-1].isdigit() and int(text_children[i][-1])<3:
        print(text_children[i])