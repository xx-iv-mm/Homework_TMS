# Exercise 3
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onion):
        self.pizza.onions = onion
        return self

    def set_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self, size, cheese, peperoni, mushrooms, onion, bacon):
        return self.builder.set_size(size).set_cheese(cheese).set_pepperoni(peperoni).set_mushrooms(
            mushrooms).set_onions(onion).set_bacon(bacon).pizza
