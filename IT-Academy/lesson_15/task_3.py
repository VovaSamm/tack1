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

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True

        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .set_size("Large")
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .build())


# Создаем экземпляр PizzaBuilder
builder = PizzaBuilder()

# Создаем экземпляр PizzaDirector с PizzaBuilder
director = PizzaDirector(builder)

# Создаем пиццу
pizza = director.make_pizza()

# Выводим информацию о пицце
print(pizza)  # Вывод: Pizza(size=Large, toppings=cheese, pepperoni, mushrooms)