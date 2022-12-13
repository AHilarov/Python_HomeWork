# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = float(input('Enter X coordinate for A: '))
y1 = float(input('Enter Y coordinate for A: '))
x2 = float(input('Enter X coordinate for B: '))
y2 = float(input('Enter Y coordinate for B: '))

l = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('Distance between A (',x1,',',y2,') and B (',x2,',',y2,') is ', "{:.2f}".format(l))
