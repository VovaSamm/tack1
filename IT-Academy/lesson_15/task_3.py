'''This program make pizaa used pattern bialder'''

class Pizza:
    def __init__(self, size,cheese=False,peperoni=False,mushrooms=False,onions=False,bacon=False):
        self. size= size
        self.cheese=cheese
        self.peperoni=peperoni
        self.mushrooms=mushrooms
        self.onions=onions
        self.bacon=bacon


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False
        self.pizza=None

    def set_size(self, size):
        self.size = size


    def add_cheese(self):
        self.cheese = True


    def add_pepperoni(self):
        self.pepperoni = True


    def add_mushrooms(self):
        self.mushrooms = True


    def add_onions(self):
        self.onions = True


    def add_bacon(self):
        self.bacon = True



    def build(self):
        self.pizza=Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    @staticmethod
    def corest_yes_0r_not(answer):
        while answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
            if answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
                answer = input('Please correct answer for qweshon ')
            else:
                answer = input('Do you wont take pizza again enter yes or not ').lower().strip()
        return answer.lower().strip()
    @staticmethod
    def corect_size_pizza(size):
        while size.lower().strip() not in ['large','small','normal']:
            if size.lower().strip() in ['large','small','normal']:
                return size
            else:
                size=input('Please enter corect size pizza: large, small, normal ').lower().strip()
    def make_pizza(self):
        self.builder.set_size(self.corect_size_pizza(input('Enter size pizza: large, small, normal ')))
        if self.corest_yes_0r_not(input('Enter wait you chesse ')) in['yes', 'да']:
            self.builder.add_cheese()
        if self.corest_yes_0r_not(input('Enter wait you pepperoni ')) in['yes', 'да']:
            self.builder.add_pepperoni()
        if self.corest_yes_0r_not(input('Enter wait you mushrooms ')) in['yes', 'да']:
            self.builder.add_mushrooms()
        if self.corest_yes_0r_not(input('Enter wait you onions ')) in['yes', 'да']:
            self.builder.add_onions()
        if self.corest_yes_0r_not(input('Enter wait you bacon ')) in ['yes', 'да']:
            self.builder.add_bacon()

    def __str__(self):
        return f'Size - {self.builder.size}, cheese - {self.builder.cheese}, pepperoni - {self.builder.pepperoni}, mushrooms - {self.builder.mushrooms}, onions - {self.builder.onions}, bacon - {self.builder.bacon}'



class Intefece:
    @staticmethod
    def corest_yes_0r_not(answer):
        while answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
            if answer.lower().strip() not in ['no', 'yes', 'да', 'нет', 'not']:
                answer = input('Please correct answer for qweshon yes or not')
            else:
                answer = input('Do you wont take pizza again enter yes or not ').lower().strip()
        return answer

    def __init__(self, user_answer_yes_or_not):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(user_answer_yes_or_not)

    def new_ansfer_yes_not(self, new_amswer_yes):
        self.user_answer_yes_or_not = self.corest_yes_0r_not(new_amswer_yes)

    def make_range(self):
        builder=PizzaBuilder()
        director=PizzaDirector(builder)
        director.make_pizza()
        print(director)


print(__doc__)
answer = input('Do you wont take pizza enter yes or not ').lower().strip()
user1 = Intefece(answer)

while user1.user_answer_yes_or_not in ['yes', 'да']:
    user1.make_range()
    user1.new_ansfer_yes_not(input('Do you wont take new pizza again enter yes or not '))

print('See you again;)')
