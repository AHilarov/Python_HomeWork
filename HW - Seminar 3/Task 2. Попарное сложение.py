# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, -5, 1, 0, 6]
if len(my_list)%2 == 0:
    a = round(len(my_list)/2)
else:
    a = round(len(my_list)/2)+1

new_list = []
for i in range(a):
    new_list.append(my_list[i]*my_list[-i-1])
print(new_list)
