# Exercise 2
import itertools

amt = int(input("Введите количество повторений: "))
count = 0
for i in itertools.cycle('123'):
    if count > amt:
        break
    else:
        print(i, end=" ")
        count += 1
