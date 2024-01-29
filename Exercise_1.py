# Exercise 1
def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


n = int(input("Введите количество чисел Фибоначчи, которое вы хотите сгенерировать? "))

fib = fibonacci()
for _ in range(n):
    print(next(fib), end=" ")
