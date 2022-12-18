# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11

my_num = input('Enter number: ')
sum_num = 0
for i in range(len(my_num)):
    if my_num[i].isdigit():
        temp = int(my_num[i])
        sum_num = sum_num + temp
print('Sum of digits in', my_num, 'is', sum_num)




