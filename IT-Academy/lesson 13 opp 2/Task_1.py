class Product:
    @staticmethod
    def valid_cost(number):
        while not isinstance(number,(float,int)):
            try:
                number=float(number)
            except Exception:
                number=input('Enter corect number ')

        return number
    def __init__(self, name_product, name_shop,cost_product):
        self.__name_product=name_product
        self.__name_shop= name_shop
        self.__cost_product=self.valid_cost(cost_product)

    @property
    def name_pr(self):
        return self.__name_product

    @property
    def name_sh(self):
        return self.__name_shop

    @property
    def name_co(self):
        return self.__cost_product
    def __add__(self, other):
        return  self.__cost_product+other

    def __radd__(self, other):
        return self.__cost_product + other
    def __str__(self):
        return f'{self.__dict__}'

class WareHouse:

    def __init__(self):
        self.__closers_in_warehouse=[]

    @property
    def get_closers_in_warehouse(self):
        return self.__closers_in_warehouse
    @get_closers_in_warehouse.setter
    def get_closers_in_warehouse(self,shoes):

        self.__closers_in_warehouse.append(shoes)

    def __getitem__(self, item):
        return self.__closers_in_warehouse[item]




    @property
    def close_in(self):
        return self.__closers_in_warehouse

    def get_name(self,name):
        for product in self.__closers_in_warehouse:
            if product.name==name:
                return product
        raise ValueError ('Hot this name')

    def sort_by_name(self):
        print(self.__closers_in_warehouse.sort(key=lambda closers_in_warehouse:closers_in_warehouse.name_pr))

    def sort_by_cost(self):
        return self.__closers_in_warehouse.sort(key=lambda closers_in_warehouse:closers_in_warehouse.name_co)
    def sort_by_name_shop(self):
        return self.__closers_in_warehouse.sort(key=lambda closers_in_warehouse:closers_in_warehouse.name_sh)

products=[Product('name'+f' {i}','name shop'+f' {i}', int(i)) for i in range(10)]
war_house=WareHouse()
for i in products:
    war_house.get_closers_in_warehouse=i

war_house.sort_by_name()
print(war_house.sort_by_name_shop())
war_house.sort_by_cost()
print(sum(products))