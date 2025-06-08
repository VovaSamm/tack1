'''This program return range of fibonati if you get integer number'''


class Fibonatsi:
    def __init__(self, value):
        self.value = self.valid_number(value)
        self.count = 1
        self.ferst_number = 0
        self.second_number = 1

    @staticmethod
    def valid_number(item):

        while not isinstance(item, int) or 0 < item <= 100:
            try:
                item = int(item)

                return int(item)
            except Exception:
                item = input('Enter corect int number ')

    def __next__(self):
        if self.count <= self.value:
            self.ferst_number, self.second_number = self.second_number, self.second_number + self.ferst_number
            self.count += 1
            return self.ferst_number
        else:
            raise StopIteration

    def __str__(self):
        return f'number {self.ferst_number}, this is {self.count} valume '

    def __iter__(self):
        return self


class Intefece:
    @staticmethod
    def corest_yes_0r_not(answer):
        while answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
            if answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
                answer = input('Please correct answer for qweshon ')
            else:
                answer = input('Do you wont take fibonati again enter yes or not ').lower().strip()
        return answer

    def __init__(self, user_answer_yes_or_not):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(user_answer_yes_or_not)

    def new_ansfer_yes_not(self, new_amswer_yes):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(new_amswer_yes)

    def make_fibonati(self):
        result = Fibonatsi(input('Enter integer number '))
        for i in result:
            print(i, end=' ')
        print()


print(__doc__)
answer = input('Do you wont take fibonati enter yes or not ').lower().strip()
user1 = Intefece(answer)

while user1.user_answer_yes_or_not in ['yes', 'да']:
    user1.make_fibonati()
    user1.new_ansfer_yes_not(input('Do you wont take fibonati again enter yes or not '))

print('See you again;)')
