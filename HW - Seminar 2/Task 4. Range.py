# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.-??? Условие не понятно. Сделано без него
import random

def int_check():
    while True:
        try:
            int_num = int(input('Enter integer number: '))
            return int_num
        except:
            print ('You need to enter INTEGER number!')

print('Enter number N and you will get a list in range [-N, N]')
my_num = abs(int_check())
my_list = [i  for i in range(-my_num, my_num+1)]
print (my_list)

num_a = random.randint(-my_num, my_num)
num_b = random.randint(-my_num, my_num)
print('Product of random numbers', num_a, 'and', num_b, 'in range [-N, N] is', num_a*num_b)