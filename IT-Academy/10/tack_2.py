'This finction make math action '
ANSWER_TRUE_DICT = {1: 'ДА', 2: 'YES'}
ANSWER_TRUE_DICT2 = {1: '*', 2: '/', 3: '-', 4: '+'}

class Math:
    def addition(self, fefst_value, second_value):
        return (fefst_value) + (second_value)

    def subtraction(self, fefst_value, second_value):
        return (fefst_value) - (second_value)

    def multiplication(self, fefst_value, second_value):
        return (fefst_value) * (second_value)

    def division(self, fefst_value, second_value):
        return  (fefst_value) / (second_value)


def valid_of_chiselko(chicelco):
    while not isinstance(chicelco, (int, float)):
        try:
            chicelco = float(chicelco)
        except:
            chicelco = input(f'Введи число формата int or float и будкт тебе частье ')
    return chicelco


def interfase(answer: str):
    if answer.upper().strip() in (ANSWER_TRUE_DICT[1], ANSWER_TRUE_DICT[2]):
        chois_user = Math()
        print('What do you do *,-,+/ ?')
        answer_user = input("Enter *,-,+/ ")
        while answer_user not in (
                ANSWER_TRUE_DICT2[1], ANSWER_TRUE_DICT2[2],ANSWER_TRUE_DICT2[3], ANSWER_TRUE_DICT2[4]):
            print('Not correct action')
            answer_user = input("Enter *,-,+/ plise ")
        if answer_user.upper().strip() == ANSWER_TRUE_DICT2[1]:
            print(chois_user.multiplication(valid_of_chiselko(input("Enter ferst value ")),
                                      valid_of_chiselko(input("Enter second value "))))
        elif answer_user.upper().strip() == ANSWER_TRUE_DICT2[2]:
            print(chois_user.division(valid_of_chiselko(input("Enter ferst value ")),
                                valid_of_chiselko(input("Enter second value "))))
        elif answer_user.upper().strip() == ANSWER_TRUE_DICT2[3]:
            print(chois_user.subtraction(valid_of_chiselko(input("Enter ferst value ")),
                                   valid_of_chiselko(input("Enter second value "))))
        elif answer_user.upper().strip() == ANSWER_TRUE_DICT2[4]:
            print(chois_user.addition(valid_of_chiselko(input("Enter ferst value ")),
                                valid_of_chiselko(input("Enter second value "))))



print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (ANSWER_TRUE_DICT[1], ANSWER_TRUE_DICT[2]):
    interfase(answer)
    answer = input('Again ')
print("Good bay see you again")
