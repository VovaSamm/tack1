'This program show diferend information for share'

from math import pi


class Descriptor:
    @staticmethod
    def valid_number(value):
        while True:
            try:
                value = float(value)
                return value
            except ValueError:
                value = input('Enter an integer or float number please: ')

    def set_name(self, owner, name):
        self.name = '_' + name

    def get(self, instance, owner):
        return instance.__dict__[self.name]

    def set(self, instance, value):
        if self.name == '_radius' and value < 1:
            print("Radius can't be < 1. Please enter a new radius.")
            while value <= 1:
                value = self.valid_number(input('Enter correct radius: '))

        instance.__dict__[self.name] = self.valid_number(value)

class Share:
    radiys = Descriptor()
    coord_x = Descriptor()
    coord_y = Descriptor()
    coord_z = Descriptor()

    @staticmethod
    def valid_number(value):
        while not isinstance(value, (int, float)):
            try:
                value = float(value)
            except Exception:
                value = input('Enter integer or float number please ')
        return value

    def number_bigest_1(self,value):
        while value<=1:
            value=self.valid_number(input('Enter number >1 for radius'))
        return value
    def __init__(self, radiys=1, coord_x=0, coord_y=0, coord_z=0):
        self.__radiys = self.number_bigest_1(self.valid_number(radiys))
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__coord_z = coord_z



    def get_volume(self):
        return 3 / 4 * pi * self.__radiys ** 2

    def get_square(self):
        return 4 * pi * self.__radiys ** 2

    def ger_radius(self):
        return self.__radiys

    def get_sentre(self):
        return (self.__coord_x, self.__coord_y, self.__coord_z)

    def set_radius(self, value):
        while self.__radiys<=self.valid_number(value):
            value=self.valid_number(input('Radius can not be <1 plus enter corect '))
        self.__radiys=self.valid_number(value)

    def set_center(self, x, y, z):
        self.__coord_x = self.valid_number(x)
        self.__coord_y = self.valid_number(y)
        self.__coord_z = self.valid_number(z)

    def is_point_inside(self, x, y, z):
        way_of_senter = pow(pow((x - self.__coord_x), 2) + pow((y - self.__coord_y), 2) + pow((z - self.__coord_z), 2),
                            0.5)
        if way_of_senter > self.__radiys:
            return False
        return True


    def __str__(self):
        return f' Radius - {self.__radiys}, coord x - {self.__coord_x}, coord y - {self.__coord_y}, coord z - {self.__coord_z}'


def interfase(answer: str):
    if answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
        chois_user = Share(input('Enter radius <1 '), input("coord x "), input("Enter coord y "), input("coord z "))
        print(
            'What do you do показать:\n объем,площадь поверхности, радиус,  координаты центра или изменить:\n радиус, координаты центра?')

        def corect_answer(answer_user):

            while answer_user not in [answer_true_dict2[i + 1].lower().strip() for i in range(len(answer_true_dict2))]:
                print('Not correct action')
                answer_user = input(
                    "Enter corect what do you do показать:\n объем,площадь поверхности, радиус,  координаты центра или изменить:\n радиус, координаты центра?' plise ")
            return answer_user

        print('Do you create share or  show share? Yes or not')
        answer_user_yes_or_not = input("Enter yes or not ").upper()
        while answer_user_yes_or_not in (answer_true_dict[1], answer_true_dict[2]):
            answer_user = input(
                "What do you do показать:\n объем,площадь поверхности, радиус,  координаты центра или изменить:\n радиус, координаты центра, информашка ?")
            corect_answer(answer_user)

            if answer_user.lower().strip() == answer_true_dict2[1].lower().strip():
                print(chois_user.get_volume())
            elif answer_user.lower().strip() == answer_true_dict2[2].lower().strip():
                print(chois_user.get_square())
            elif answer_user.lower().strip() == answer_true_dict2[3].lower().strip():
                print(chois_user.ger_radius())
            elif answer_user.lower().strip() == answer_true_dict2[4].lower().strip():
                print(chois_user.get_sentre())
            elif answer_user.lower().strip() == answer_true_dict2[5].lower().strip():
                chois_user.set_radius(input('Enter new radius '))
            elif answer_user.lower().strip() == answer_true_dict2[6].lower().strip():
                chois_user.set_center(input('Enter new coord x '), input('Enter new coord y '),
                                      input('Enter new coord z '))
            elif answer_user.lower().strip() == answer_true_dict2[7].lower().strip():
                print(chois_user.is_point_inside(input('Enter  coord x '), input('Enter  coord y '),
                                                 input('Enter coord z ')))
            elif answer_user.lower().strip() == answer_true_dict2[8].lower().strip():
                print(chois_user)
            else:
                print('Не отработало')
            print('Do you do new  action? Yes or not')
            answer_user_yes_or_not = input("Enter yes or not ").upper()


answer_true_dict = {1: 'ДА', 2: 'YES'}
answer_true_dict2 = {1: 'объем', 2: 'площадь поверхности', 3: 'показать радиус ', 4: 'показать координаты центра ',
                     5: 'изменить радиус', 6: 'изменить координаты центра', 7: 'Лежит ли точка в приделаж сферы',8: 'информашка'}

print("Hello")
print(__doc__)
answer = input('Enter yes or not ')
while answer.upper().strip() in (answer_true_dict[1], answer_true_dict[2]):
    interfase(answer)
    answer = input('You wait new share Yes or not ')
print("Good bay see you again")
