# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число следующим образом.
# 1)  Строится двоичная запись числа N.
# 2)  К этой записи дописывается справа два нуля, если число четное,
# или две единицы в противном случае
# Укажите максимальное число N, после обработки которого с помощью этог
# алгоритма получается число менее 94. В ответе это число запишите в десятичной системе.

# n=int(input('>'))
import math
# test = math.inf

# def func(n):
#     a=bin(n)
#     if n%2==0:
#         a+='00'
#     else:
#         a+='11'
#     a=a[2:]
#     a=int(a, 2)
#     return a

# for i in range(150,1,-1):
#     if func(i)<94:
#         print(i)
#         break

# print(func(23))


# sting = '>'+'1'*26+'2'*10+'3'*14
# print(sting)

# while '>1' in sting or '>2' in sting or '>3' in sting:
#     sting=sting.replace('>1', '22>')
#     sting=sting.replace('>2', '2>')
#     sting=sting.replace('>3', '1>')

# print(sting)

# a= sting.count('2')*2+sting.count('1')
# print(a)


# Операнды арифметического выражения записаны в системах счисления с основаниями 12 и 14:

# yAAx12 + x02y14

# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим
# и кратно 80. Для найденных значений x и y вычислите частное от деления значения арифметического
# выражения на 80 и укажите его в ответе в десятичной системе счисления. Основание системы счисления
# в ответе указывать не нужно.
# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits):
#         return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result

# lst1=[]
# for x in '123456789ab':
#     for y in '123456789ab':
#         f1 = int(f'{y}aa{x}', 12)
#         lst1.append(f1)

# lst2=[]
# for x in '123456789ab':
#     for y in '123456789ab':
#         f2 = int(f'{x}02{y}', 14)
#         lst2.append(f2)

# lst3=[]
# for i in lst1:
#     for j in lst2:
#         a = i+j
#         if a %80==0:
#             lst3.append(a)
#             print(f'{i} + {j} = {a}')
            

# print(min(lst3))
# '3297 + 5503 = 8800'
# # 3299 + 2781 = 6080

# print(convert_to(3299, 12))
# print(convert_to(2781, 14))
# print(6080/80)
# yAAx12 + x02y14



# В файле содержится последовательность из 10 000 целых положительных чисел.
# Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество
# пар элементов последовательности, у которых разность элементов кратна 60 и хотя бы один 
# из элементов кратен 15, затем максимальную из разностей элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.



with open('17.txt') as f:
    data = [int(i) for i in f]

res=[]
for i in range(len(data)):
    for k in range(len(i+1,data)):
        if ((i %15==0) or (k %15==0)) and (abs(k-i)%60==0):
            res.append(abs(k-i))

# with open('17.txt') as f:
#     s = [int(x)for x in f]
#     res = []
#     for i in range (0, len(s)):
#         for j in range(i+1, len(s)):
#             if ((s[i]-s[j]) % 60 == 0) and (((s[i]) % 15 == 0) or ((s[j]) % 15 == 0)):
#                 res.append(s[i]-s[j])
# print(len(res), max(res))


print(len(res))
print(max(res))