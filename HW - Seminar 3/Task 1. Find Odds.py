# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
for i in range(10):
    my_list.append (random.randint(-10, 10))
print (my_list)

odd_sum = 0
for i in range(1, len(my_list), 2):
    odd_sum += my_list[i]
print(odd_sum)    