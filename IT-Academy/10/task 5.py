'''This program chesk string on polindromr or unto in string'''

class Superstr(str):
    def __init__(self,user_enter_string):
        self.user_enter_string=user_enter_string
    def is_repition(self,user_string):
        string_copy=self.user_enter_string
        if  self.user_enter_string=='':
            return False
        else:
            while string_copy!='':

                if user_string in string_copy and string_copy[0:len(user_string)]==user_string :
                    string_copy=string_copy[len(user_string):]

                else:
                    return False
            return True
    def is_palindrome(self):
        if self.user_enter_string.lower()==self.user_enter_string.lower()[-1::-1]:
            return True
        return False
def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = Superstr(input('Enter your string '))


        def corect_answer(answer_user):

            while answer_user.lower().strip() not in [answer_true_dict2[i + 1].lower().strip() for i in range(len(answer_true_dict2))]:
                print('Not correct action')
                answer_user = input(f'Выбері действіе {[i.lower().strip()+',' for i in answer_true_dict2.values()]} ')
            return answer_user

        print('Do you check string? Yes or not')
        answer_user_yes_or_not = input("Enter yes or not ").upper().strip()
        while answer_user_yes_or_not in (answer_true_dict[1], answer_true_dict[2]):

            answer_user =  input(f'Выбері действіе {[i.lower().strip() for i in answer_true_dict2.values()]} ').strip()
            corect_answer(answer_user)

            if answer_user.lower().strip() == answer_true_dict2[1].lower().strip():
                print(chois_user.is_repition(input('Enter string that unto in old string ')))
            elif answer_user.lower().strip() == answer_true_dict2[2].lower().strip():
                print(chois_user.is_palindrome())

            else:
                print('Не отработало')
            print('Do you do new  action? Yes or not')
            answer_user_yes_or_not = input("Enter yes or not ").upper().strip()


answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {1: 'проверка на повторение', 2: 'проверка на полиндромность'}

print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('You wait new string Yes or not ')
print("Good bay see you again")
