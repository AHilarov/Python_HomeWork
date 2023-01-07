# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
from random import randint as RI
from mycode import int_check as IC

print('Enter the lenght of the list to be generated')
my_list = [RI(0,10) for _ in range(IC())]
print(my_list)
my_list2 = []
for _ in my_list:
    if my_list2.count(_) == 0:
        my_list2.append(_)
print(my_list2)