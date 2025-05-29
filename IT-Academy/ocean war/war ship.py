'''This is dame in war ship *-sea, S-ship, K-kill ship (or pace ship) #- sea whit can not stay ship'''


import random
from selectors import SelectSelector
from tkinter.messagebox import showerror


class Batelfield:

    def __init__(self,line:int,colum:int):
        self.line=line
        self.colum=colum
        self.batelfield=[[' * ' for  j in range(self.colum+2)]for i in range(self.line+2)]
        self.batelfield_enemy = [[' * ' for j in range(self.colum + 2)] for i in range(self.line + 2)]
    def meke_boord(self):
        for i in range(len(self.batelfield)):
            for j in range(len(self.batelfield[i])):
                if i==0 or i ==len(self.batelfield):
                    self.batelfield[i][j]=f'{j:^3}'
                    self.batelfield_enemy[i][j] =f'{j:^3}'
                if j==0 or j==len(self.batelfield[i]):
                    self.batelfield[i][j] = f"{i:^3}"
                    self.batelfield_enemy[i][j]= f"{i:^3}"
        for i in range(len(self.batelfield)):
            for j in range(len(self.batelfield[i])):
                if i==11:
                    self.batelfield[i][j] = f'{j:^3}'
                    self.batelfield_enemy[i][j] = f'{j:^3}'
                if j==11:
                    self.batelfield_enemy[i][j] = f"{i:^3}"
                    self.batelfield[i][j] = f"{i:^3}"
    def show(self):
        print('твое поле')
        for i in self.batelfield:
            print(*i)
        print('Поле врага')
        for i in self.batelfield_enemy:
            print(*i)

    def horifonr_front(self,n):
        if n==1:
            return True
        return False
    def make_not_ship(self):
        for i in range(len(self.batelfield)):
            for j in range(len(self.batelfield[i])):
                if self.batelfield[i][j]==' S ':
                    self.batelfield[i-1][j-1]=' # ' if self.batelfield[i-1][j-1]!=' S '  else ' S '
                    self.batelfield[i - 1][j] = ' # ' if self.batelfield[i - 1][j] != ' S ' else ' S '
                    self.batelfield[i - 1][j+1] = ' # ' if self.batelfield[i - 1][j+1] != ' S ' else ' S '
                    self.batelfield[i][j + 1] = ' # ' if self.batelfield[i][j + 1] != ' S ' else ' S '
                    self.batelfield[i][j - 1] = ' # ' if self.batelfield[i][j - 1] != ' S ' else ' S '
                    self.batelfield[i+1][j - 1] = ' # ' if self.batelfield[i+1][j - 1] != ' S ' else ' S '
                    self.batelfield[i + 1][j] = ' # ' if self.batelfield[i + 1][j] != ' S ' else ' S '
                    self.batelfield[i + 1][j+1] = ' # ' if self.batelfield[i + 1][j+1] != ' S ' else ' S '

    def mega_filtler(self,x):
        if x!=' S ' and x!=' # ':
            return True
        return False
    def add_ship_gorizont(self,i,j,num):
        new_x_start=i-1
        new_x_end=i+1
        new_y_start=j-1
        new_y_end=j+num+1
        list_elem=[]
        for i1 in range( new_x_start,new_x_end):
            for j1 in range(new_y_start, new_y_end):
                list_elem.append(self.batelfield[i1][j1])
        return all(list(map(self.mega_filtler,list_elem)))

    def add_ship_not_gorizont(self,i,j,num):
        new_x_start=i-1
        new_x_end=i+num+1
        new_y_start=j-1
        new_y_end=j+1
        list_elem=[]
        for i1 in range( new_x_start,new_x_end):
            for j1 in range(new_y_start, new_y_end):
                list_elem.append(self.batelfield[i1][j1])
        return all(list(map(self.mega_filtler,list_elem)))



    def add_ship(self,ship_size):
        horizon=random.randint(0,1)
        nose_ship_x=random.randint(1,self.line-ship_size)
        nose_ship_y = random.randint(1, self.colum -ship_size)
        good_point_horizon=self.add_ship_gorizont(nose_ship_x, nose_ship_y, ship_size)
        good_point_not_horizon=self.add_ship_not_gorizont(nose_ship_x, nose_ship_y, ship_size)
        while not (good_point_horizon or good_point_not_horizon):

            nose_ship_x = random.randint(1, self.line - ship_size)
            nose_ship_y = random.randint(1, self.colum - ship_size)
            good_point_horizon = self.add_ship_gorizont(nose_ship_x, nose_ship_y, ship_size)
            good_point_not_horizon = self.add_ship_not_gorizont(nose_ship_x, nose_ship_y, ship_size)

        if good_point_horizon:
            horizon=1
        else:
            horizon=0


        if horizon == 1 :
            for i in range(len(self.batelfield)):
                for j in range(len(self.batelfield[i])):
                    for num in range(ship_size):
                        self.batelfield[nose_ship_x][nose_ship_y+num] = ' S '
        else:
            for i in range(len(self.batelfield)):
                for j in range(len(self.batelfield[i])):
                    for num in range(ship_size):
                        self.batelfield[nose_ship_x+num][nose_ship_y] = ' S '




        self.make_not_ship()

class Game:
    def __init__(self,plauer1,plauer2):
        self.name1=plauer1
        self.name2=plauer2
        self.plauer1_fiell=Batelfield(10,10)
        self.plauer2_fiell = Batelfield(10, 10)
    def new_game(self):
        self.plauer1_fiell.add_ship(4)
        self.plauer1_fiell.add_ship(3)

        self.plauer1_fiell.add_ship(2)
        self.plauer1_fiell.add_ship(2)
        self.plauer1_fiell.add_ship(1)
        self.plauer1_fiell.add_ship(1)
        self.plauer1_fiell.add_ship(1)

        self.plauer1_fiell.meke_boord()

        self.plauer2_fiell.add_ship(4)
        self.plauer2_fiell.add_ship(3)

        self.plauer2_fiell.add_ship(2)
        self.plauer2_fiell.add_ship(2)
        self.plauer2_fiell.add_ship(1)
        self.plauer2_fiell.add_ship(1)
        self.plauer2_fiell.add_ship(1)

        self.plauer2_fiell.meke_boord()



    def step_player1(self,x,y,flag=True):

        if self.plauer2_fiell.batelfield[x][y]==' S ':
            self.plauer2_fiell.batelfield[x][y] = ' K '
            self.plauer1_fiell.batelfield_enemy[x][y] = ' K '
            print(f'Игрок {self.name1} попал твой выстрел был x-{x} y-{y} ,стреляй еще')
        else:
            self.plauer2_fiell.batelfield[x][y] = ' 0 '
            self.plauer1_fiell.batelfield_enemy[x][y] = ' 0 '
            print(f'Игрок {self.name1} промахнулся твой выстрел x-{x} y-{y},  стреляет игрок {self.name2}')
            flag=False

        return flag
    def step_player2(self,x,y,flag=True):
        if self.plauer1_fiell.batelfield[x][y]==' S ':
            self.plauer1_fiell.batelfield[x][y] = ' K '
            self.plauer2_fiell.batelfield_enemy[x][y] = ' K '
            print(f'Игрок {self.name2} попал твой выстрел был x-{x} y-{y}, стреляй еще ')
        else:
            self.plauer1_fiell.batelfield[x][y] = ' 0 '
            self.plauer2_fiell.batelfield_enemy[x][y] = ' 0 '
            print(f'Игрок {self.name2} промахнулся твой выстрел x-{x} y-{y} стреляет игрок {self.name1}')
            flag = False

        return flag

def valid_of_number(number: str) -> bool:
    '''Make numer integer value'''
    while type(number) != int :
        try:
            if 1<=int(number)<=10:
                number = int(number)
            else:
                number = valid_of_number(input('Plese ennter number 1<=number<=10 '))

        except Exception:
            number = input('Enter corect number ')
    return number

def enter_wunction(string_user: str) -> None:
    'This function call menu'
    data_corect_answer = ['yes', 'да']

    while string_user in data_corect_answer:
        print(f'new game')
        user1=input('Enter name ferst player ')
        user2 = input('Enter name second player ')
        part1=Game(user1,user2)
        part1.new_game()

        coin_ship_plauer1=sum([ i.count(' S ') for i in part1.plauer1_fiell.batelfield])
        coin_ship_plauer2 = sum([ i.count(' S ') for i in part1.plauer2_fiell.batelfield])
        while coin_ship_plauer1!=0 or coin_ship_plauer2!=0:

            print(f'ferst fill')
            part1.plauer1_fiell.show()
            choise_player1_x = valid_of_number(input('Enter x for player 1 '))
            choise_player1_y = valid_of_number(input('Enter y for player 1 '))
            while part1.step_player1(choise_player1_x,choise_player1_y ):
                part1.plauer1_fiell.show()
                choise_player1_x = valid_of_number(input('Enter x for player 1 '))
                choise_player1_y = valid_of_number(input('Enter y for player 1 '))
                coin_ship_plauer1 = sum([i.count(' S ') for i in part1.plauer1_fiell.batelfield])

            print(f'second fill')
            part1.plauer2_fiell.show()
            choise_player2_x = valid_of_number(input('Enter x for player 2 '))
            choise_player2_y = valid_of_number(input('Enter y for player 2 '))


            while part1.step_player2(choise_player2_x, choise_player2_y):
                part1.plauer2_fiell.show()
                choise_player2_x = valid_of_number(input('Enter x for player 2 '))
                choise_player2_y = valid_of_number(input('Enter y for player 2 '))
                coin_ship_plauer2 = sum([i.count(' S ') for i in part1.plauer2_fiell.batelfield])

        string_user = input('Do you wait play again? (write Yes or да) ')
    print('See you again;)')

#d1=Game('p','v')
#d1.new_game()
#d1.plauer1_fiell.batelfield
#d1.plauer1_fiell.show()
#d1.step_player1(1,1)
#d1.step_player1(2,2)
#d1.step_player1(3,3)
#d1.step_player1(4,4)
#d1.step_player1(5,5)
#d1.step_player1(6,6)
#print('player2')
#d1.plauer2_fiell.show()
#d1.plauer2_fiell.batelfield
#d1.step_player2(1,1)
#d1.step_player2(2,2)
#d1.step_player2(3,3)
#d1.step_player2(4,4)
#d1.step_player2(5,5)
#d1.step_player2(6,6)
print('Hello!')
print(__doc__)
enter_wunction(input('Do you want enter list? (write Yes or да) ').strip())