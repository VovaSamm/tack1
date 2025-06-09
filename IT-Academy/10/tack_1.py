'''Tsis procram cgois taste of soda'''

ANSWER_TRUE_DICT = {1: 'ДА', 2: 'YES'}


class Soda:

    def __init__(self):
        self.__choic_taste = 'обычная газировка'

    @property
    def change_taste(self):
        return self.__choic_taste

    @change_taste.setter
    def change_taste(self, new_taste):
        self.__choic_taste = new_taste

    def __str__(self):
        if self.__choic_taste == 'обычная газировка':
            return f'У вас обычная газировка'
        else:
            return f'У вас  газировка c {self.__choic_taste} вкусом.'


def interfase(answer: str):
    if answer.upper().strip() in (ANSWER_TRUE_DICT[1], ANSWER_TRUE_DICT[2]):
        chois_user_of_taste_soda = Soda()
        print('Do you wain change taste soda')
        answer_user = input("Enter yes or not ")
        if answer_user.upper().strip() in (ANSWER_TRUE_DICT[1], ANSWER_TRUE_DICT[2]):
            chois_user_of_taste_soda.change_taste = input('Enter new taste: ')
            print(chois_user_of_taste_soda)
        else:
            print(chois_user_of_taste_soda)


print("Hello")
print(__doc__)
ANSWER_TRUE_DICT = {1: 'ДА', 2: 'YES'}
answer = input('Enter yes or not ')
while answer.upper().strip() in (ANSWER_TRUE_DICT[1], ANSWER_TRUE_DICT[2]):
    interfase(answer)
    answer = input('Again ')
print("Good bay see you again")
