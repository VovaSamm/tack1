'''This program play witsh you in BeElephant'''

class BeElephant:

    @staticmethod
    def valid_path(item):

        while not isinstance(item,int) or 0<item<=100:
            try:
                item=int(item)
                if 0<=item<=100:
                    return item
            except Exception:
                item=input('Enter corect int number ')
            else:
                item = input('Enter corect int number 0<=number<=100 ')
        return item

    def __init__(self,part_of_elephant,part_of_an_bee):
        self.__part_of_elephant=self.valid_path(part_of_elephant)
        self.__part_of_an_bee=self.valid_path(part_of_an_bee)

    def fly(self):
        if self.__part_of_an_bee>self.__part_of_elephant:
            return True
        return False
    def trumper(self):
        if self.__part_of_an_bee<self.__part_of_elephant:
            return f'tu-tu-doo-doo'
        return f'wzzzz'
    def eat(self,meal,value):
        while meal not in ['nectar','grass']:
            print('Enter nectar or grass')
            meal=input().lower().strip()
        if meal=='nectar':
            if self.__part_of_elephant-self.valid_path(value)>=0:
                self.__part_of_elephant=self.__part_of_elephant-self.valid_path(value)
            else:
                self.__part_of_elephant=0

        else:
            if self.__part_of_an_bee - self.valid_path(value) >= 0:
                self.__part_of_an_bee = self.__part_of_an_bee - self.valid_path(value)
            else:
                self.__part_of_an_bee=0
    def __str__(self):
        return f'Слоновья часть - {self.__part_of_elephant}, пчелиная часть - {self.__part_of_an_bee}'
def valid_number(item):

    while not isinstance(item,int) or 0<item<=100:
        try:
            item=int(item)

            return int(item)
        except Exception:
            item=input('Enter corect int number ')

        return int(item)
def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = BeElephant(input('Enter your number one '),input('Enter your number second '))


        def corect_answer(answer_user):
            answer_user=valid_number(answer_user)
            while answer_user not in answer_true_dict2:
                print('Not correct action')
                answer_user = valid_number((input(f'Выбері действіе {answer_true_dict2}')))
            return int(answer_user)

        print('Do you check string? Yes or not')
        answer_user_yes_or_not = input("Enter yes or not ").upper().strip()
        while answer_user_yes_or_not in (answer_true_dict[1], answer_true_dict[2]):

            answer_user =  input(f'Выбері действіе нумер {answer_true_dict2} ').strip()
            corect_answer(answer_user)

            if answer_user == '1':
                print(chois_user.fly())
            elif answer_user == '2':
                print(chois_user.trumper())
            elif answer_user == '3':
                print(chois_user.eat(input('Enter ean bee or elephant nectar or grass').lower().strip(),input('Enter number 0-100')))
            elif answer_user == '4':
                print(chois_user)
            else:
                print('Не отработало')
            print('Do you do new  action? Yes or not')
            answer_user_yes_or_not = input("Enter yes or not ").upper().strip()

answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {1: 'проверка на часть печлы еслі меньше слона', 2: 'проверка на если часть слона не меньше части пчелы',3:'Ест ',4:'info'}

print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('You wait new string Yes or not ')
print("Good bay see you again")