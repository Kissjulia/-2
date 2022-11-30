# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
from random import randint
lst = [randint(-10, 10) for i in range(20)]
print('Исходный список', str(lst))
for i in range(len(lst) - 1, 0, -1):
  j = randint(0, i + 1)
lst[i], lst[j] = lst[j], lst[i]

print("Перемешанный список: " + str(lst))