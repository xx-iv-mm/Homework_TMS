class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, num1, num2):
        if self.strategy is not None:
            return self.strategy.execute(num1, num2)


class Addition:
    @staticmethod
    def execute(num1, num2):
        return num1 + num2


class Subtraction:
    @staticmethod
    def execute(num1, num2):
        return num1 - num2


class Multiplication:
    @staticmethod
    def execute(num1, num2):
        return num1 * num2


class Division:
    @staticmethod
    def execute(num1, num2):
        return num1 * num2

