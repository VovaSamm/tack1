'This program show you information of your car'


class Car:
    def __init__(self, color='red', type='bmw', year='1'):
        self.color = color
        self.type = type
        self.year = year
        self.status = 'Заглушено'

    def start_of_car(self):
        print("Автомобиль заведен;)")
        self.status = 'Автомобиль заведен;)'

    def stop_of_car(self):
        print('Твоя шоха заглохла :(')
        self.status = 'Твоя шоха заглохла :('

    def information(self):
        print(
            f'Цвет тачкм - {self.color}, тип тачки {self.type}, возвраст тaчки - {self.year},  статус - машины - {self.status} ')


def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = Car(input("Enter color "), input("Enter type "), input("Enter year "))
        print('What do you do start,stop,info ?')

        def corect_answer(answer_user):
            while answer_user not in (answer_true_dict2[1], answer_true_dict2[2], answer_true_dict2[3]):
                print('Not correct action')
                answer_user = input("Enter start,stop or info plise ")
            return answer_user

        print('Do you create status auto? Yes or not')
        answer_user_yes_or_not = input("Enter yes or not ").upper()
        while answer_user_yes_or_not in (answer_true_dict[1], answer_true_dict[2]):
            answer_user = input("Enter start,stop or info ")
            corect_answer(answer_user)
            if answer_user.lower().strip() == answer_true_dict2[1]:
                chois_user.start_of_car()
            elif answer_user.lower().strip() == answer_true_dict2[2]:
                chois_user.stop_of_car()
            elif answer_user.lower().strip() == answer_true_dict2[3]:
                chois_user.information()
            print('Do you create status auto? Yes or not')
            answer_user_yes_or_not = input("Enter yes or not ").upper()


answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {1: 'start', 2: 'stop', 3: 'info'}
print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('You wait new car? Yes or not ')
print("Good bay see you again")
