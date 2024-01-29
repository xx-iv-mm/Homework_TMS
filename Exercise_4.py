# Exercise_4
class Animal:
    def speak(self):
        raise NotImplementedError("Абстрактный метод должен быть переопределён в классе потомке")

class Dog(Animal):
    def speak(self):
        print("Гав!")


class Cat(Animal):
    def speak(self):
        print("Мяу!")


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()