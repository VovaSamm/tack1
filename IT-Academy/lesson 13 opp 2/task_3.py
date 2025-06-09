class Bus:

    def __init__(self,speed,max_people_in_bus,max_speed,list_of_people):
        self.__speed=speed
        self.max_people_in_bus=max_people_in_bus
        self.__max_speed=valid_number(max_speed)
        self.dict_of_seats={i+1:list_of_people[i] if len(list_of_people)>=i+1 else None for i in range(valid_number(self.max_people_in_bus))}
        self.flag_free_seats=True  if  valid_number(self.max_people_in_bus)>len(list_of_people) else False
    @staticmethod
    def valig_of_integer(number):
        while isinstance(number,int):
            try:
                number=int(number)
                return number
            except Exception:
                number=input('Enter corect number ')

    def valig_corect_number(self,number):
        while number not in  self.dict_of_seats:
                number=self.valig_of_integer(input('Enter corect number '))
        return number
    @property
    def change_speeed(self):
        return self.__speed
    @change_speeed.setter
    def change_speeed(self,new_speed):
        self.valig_of_integer(new_speed)
        if 0<=valid_number(new_speed)<=self.__max_speed:
            self.__speed=new_speed

    def landing_of_number_out(self,number):
        number=self.valig_corect_number(self.valig_of_integer(number))
        self.dict_of_seats[number]=None

    def landing_of_name_out(self,name):
        for i in self.dict_of_seats:
            if self.dict_of_seats[i].lowers().stip()==name.lowers().stip():
                self.dict_of_seats[i]=None
                print('Высажен ')

    def landing_of_name_into_bus(self,name):
        if  self.flag_free_seats==True:
            for i in  self.dict_of_seats:
                if self.dict_of_seats[i]==None:
                    self.dict_of_seats[i]=name
                break
            self.flag_free_seats=all([self.dict_of_seats[i]!=None for i in self.dict_of_seats])
        else:
            print('Свободных мест нет ')

    def __iadd__(self, other):
        if self.flag_free_seats:
            self.landing_of_name_into_bus(self, other)
    def __isub__(self, other):
        self.landing_of_name_out(self, other)

    def __str__(self):
        return f'{self.dict_of_seats}'


def valid_number(item):

    while not isinstance(item,int) or 0<item<=100:
        try:
            item=int(item)

            return int(item)
        except Exception:
            item=input('Enter corect int number ')

def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = Bus(input('Enter speed '), input('Enter max seet in bus '), input('Enter max speed bus '), input('name piople for spase ').title().split())

        def corect_answer(answer_user):

            while answer_user not in answer_true_dict2:
                print('Not correct action')
                answer_user = (input(f'Выбері действіе {answer_true_dict2} '))
            return answer_user

        print('Do you check string? Yes or not')
        answer_user_yes_or_not = input("Enter yes or not ").upper().strip()
        while answer_user_yes_or_not in (answer_true_dict[1], answer_true_dict[2]):

            answer_user =  input(f'Выбері действіе нумер {answer_true_dict2} ').strip()
            corect_answer(answer_user)

            if answer_user == '1':
                chois_user.change_speeed=valid_number(input('Enter new speed '))
            elif answer_user == '2':
                chois_user.landing_of_number_out(valid_number(input('Enter out number ')))
            elif answer_user == '3':
                chois_user.landing_of_name_out(input('Enter out name ').title().strip())
            elif answer_user == '4':
                chois_user.landing_of_name_into_bus(input('Enter out name ').title().strip())
            elif answer_user == '5':
                print(chois_user)
            else:
                print('Не отработало')
            print('Do you do new  action? Yes or not')
            answer_user_yes_or_not = input("Enter yes or not ").upper().strip()

answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {'1': 'нова скорасть', '2': 'выкидываем чела по номеру','3':'выкидываем чела по имени ','4':'сажаем чела по имени ','5':'инфа '}

print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('You wait new string Yes or not ')
print("Good bay see you again")











