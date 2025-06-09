
'This finction make math action '
class Math:
    def addition(self,fefst_value,second_value):
        print( (fefst_value)+(second_value))
    def subtraction(self,fefst_value,second_value):
        print((fefst_value)-(second_value))

    def multiplication(self,fefst_value,second_value):
        print( (fefst_value)*(second_value))

    def division(self,fefst_value,second_value):
        print( (fefst_value)/(second_value))
def valid_of_chiselko(chicelco):
    while not isinstance(chicelco,(int,float)):
        try:
            chicelco = float(chicelco)
        except:
            chicelco = input(f'Введи число формата int or float и будкт тебе частье ')
    return chicelco

def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = Math()
        print('What do you do *,-,+/ ?')
        answer_user = input("Enter *,-,+/ ")
        while answer_user not in(answer_true_dict2[1],answer_true_dict2[2],answer_true_dict2[3],answer_true_dict2[4]):
            print('Not correct action')
            answer_user = input("Enter *,-,+/ plise ")
        if answer_user.upper().strip() == answer_true_dict2[1]:
            chois_user.multiplication(valid_of_chiselko(input("Enter ferst value ")),valid_of_chiselko(input("Enter second value ")))
        elif    answer_user.upper().strip() == answer_true_dict2[2]:
            chois_user.division(valid_of_chiselko(input("Enter ferst value ")),valid_of_chiselko(input("Enter second value ")))
        elif    answer_user.upper().strip() == answer_true_dict2[3]:
            chois_user.subtraction(valid_of_chiselko(input("Enter ferst value ")),valid_of_chiselko(input("Enter second value ")))
        elif    answer_user.upper().strip() == answer_true_dict2[4]:
            chois_user.addition(valid_of_chiselko(input("Enter ferst value ")),valid_of_chiselko(input("Enter second value ")))


answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {1: '*', 2: '/',3: '-', 4: '+'}
print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('Again ')
print("Good bay see you again")