# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint as RI
from random import uniform as UF

my_list = [round(UF(0,100), RI(0,3)) for _ in range(10)]
print(my_list)

for _ in range(len(my_list)):
    item = my_list.pop(0)
    my_list.append(item if item != int(item) else int(item))

my_list2 = []
for item in my_list:
    if item !=int(item):
        my_list2.append(round(item%1, 3))

print(my_list2)
print('max = ', max(my_list2))
print('min = ', min(my_list2))
print('max - min = ', max(my_list2) - min(my_list2))
