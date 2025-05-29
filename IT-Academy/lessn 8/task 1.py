str1=''
with open('txt','r',encoding='utf-8') as file:
   str1=file.read()
   string_words=str1.split()
for i in range(len(string_words)):
    print(i)
    if string_words[i][0].isupper() and  string_words[i] not in string_words[0] and '.' not in string_words[i-1] :
        string_words[i]='N'
for i in range(1,len(string_words)):
    if string_words[i]==string_words[i-1]=='N':
        string_words[i-1]=''
while '' in string_words:
    string_words.remove('')

print(' '.join(string_words))