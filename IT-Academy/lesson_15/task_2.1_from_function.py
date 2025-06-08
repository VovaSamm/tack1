'''This program return range of range 1-2-3-1-2-3 if you get integer number'''


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

    def make_range(self):
        result = rangr_from_one_two_tree(valid_number(input('Enter integer number ')))
        for i in result:
            print(i, end='-')
        print()


def rangr_from_one_two_tree(number):
    count = 0
    value_runge = 0
    while count < number:
        if value_runge == 3:
            value_runge = 1
        else:
            value_runge += 1
        count += 1
        yield value_runge


def valid_number(item):
    while not isinstance(item, int):
        try:
            item = int(item)

            return int(item)
        except Exception:
            item = input('Enter corect int number ')


print(__doc__)
answer = input('Do you wont take range enter yes or not ').lower().strip()
user1 = Intefece(answer)

while user1.user_answer_yes_or_not in ['yes', 'да']:
    user1.make_range()
    user1.new_ansfer_yes_not(input('Do you wont take range again enter yes or not '))

print('See you again;)')
