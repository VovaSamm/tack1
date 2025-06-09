'''This program answer what talk animal'''



class Animal:
    def speak(self):
        print()


class Dog(Animal):

    def speak(self):
        answer = 'Waf'
        return answer

    def __str__(self):
        return f'It speak {self.speak()}'

class Cow(Animal):

    def speak(self):
        answer = 'Myyyy'
        return answer

    def __str__(self):
        return f'It speak {self.speak()}'


class Cat(Animal):

    def speak(self):
        answer = 'Miay'
        return answer

    def __str__(self):
        return f'It speak {self.speak()}'


class AnimalFactory:
    @staticmethod
    def corest_cat_or_dog(answer):
        while answer.lower().strip() not in ['cat', 'dog','cow']:
            if answer.lower().strip() not in ['cat', 'dog','cow']:
                answer = input('Please correct answer for qweshon you wont cat or dog or cow ').lower().strip()

        return answer.lower().strip()

    def create_animal(self, answer):
        if self.corest_cat_or_dog(answer) == 'cat':
            return Cat()
        elif self.corest_cat_or_dog(answer) == 'dog':
            return Dog()
        return Cow()


class Intefece:
    @staticmethod
    def corest_yes_0r_not(answer):
        while answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
            if answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
                answer = input('Please correct answer for qweshon ')
            else:
                answer = input('Do you wont take animal again enter yes or not ').lower().strip()
        return answer

    def __init__(self, user_answer_yes_or_not):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(user_answer_yes_or_not)

    def new_ansfer_yes_not(self, new_amswer_yes):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(new_amswer_yes)

    def make_range(self):
        print(AnimalFactory().create_animal(input('Enter cat or dog or cow ').lower().strip()))


print(__doc__)
answer = input('Do you wont take animal enter yes or not ').lower().strip()
user1 = Intefece(answer)

while user1.user_answer_yes_or_not in ['yes', 'да']:
    user1.make_range()
    user1.new_ansfer_yes_not(input('Do you wont take new animal again enter yes or not '))

print('See you again;)')
