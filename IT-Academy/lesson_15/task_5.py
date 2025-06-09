class Calculator:

    def __init__(self):
        self.strategy=None
    @staticmethod
    def corest_strategy(answer):
        while answer.lower().strip() not in ['+', '-', '/', '*']:
            if answer.lower().strip() not in ['+', '-', '/', '*']:
                answer = input('Please correct strategy for calculator ')
            else:
                answer = input('Do you wont take animal again enter yes or not ').lower().strip()
        return answer
    @staticmethod
    def valid_number(item):

        while not isinstance(item, (int,float)):
            try:
                item = int(item)

                return int(item)
            except Exception:
                item = input('Enter corect int number ')
    def set_strategy(self,strategy):
        self.strategy=self.corest_strategy(strategy.lower().strip())

    def calc(self):
        if self.strategy == None:
            raise ValueError ('Not correct strategy')
        elif self.strategy=='*':
            return Multiplication.execute(self.valid_number(input('Enter ferst number ')),self.valid_number(input('Enter second number ')))
        elif self.strategy=='/':
            return Division.execute(self.valid_number(input('Enter ferst number ')),self.valid_number(input('Enter second number ')))
        elif self.strategy == '+':
            return Addition.execute(self.valid_number(input('Enter ferst number ')),self.valid_number(input('Enter second number ')))
        elif self.strategy == '-':
            return Subtraction.execute(self.valid_number(input('Enter ferst number ')),self.valid_number(input('Enter second number ')))

    def __str__(self):
        return f' You choes {self.strategy}, answer = {self.calc()}'


class Addition:
    @staticmethod
    def execute(a,b):
        return a+b
class Subtraction:
    @staticmethod
    def execute(a, b):
        return a - b

class Multiplication:
    @staticmethod
    def execute(a, b):
        return a * b
class Division:
    @staticmethod
    def execute(a, b):
        return a / b


class Intefece:
    @staticmethod
    def corest_yes_0r_not(answer):
        while answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
            if answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
                answer = input('Please correct answer for qweshon ')
            else:
                answer = input('Do you wont take new expression again enter yes or not ').lower().strip()
        return answer



    def __init__(self, user_answer_yes_or_not):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(user_answer_yes_or_not)

    def new_ansfer_yes_not(self, new_amswer_yes):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(new_amswer_yes)

    def make_range(self):
        resalt=Calculator()
        resalt.set_strategy(input('Enter strategy *,-,+,- '))
        print(resalt)


print(__doc__)
answer = input('Do you wont take expression enter yes or not ').lower().strip()
user1 = Intefece(answer)

while user1.user_answer_yes_or_not in ['yes', 'да']:
    user1.make_range()
    user1.new_ansfer_yes_not(input('Do you wont take new animal again enter yes or not '))

print('See you again;)')
