# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input('Enter X coortinate: '))
y = float(input('Enter Y coortinate: '))
if x == 0 and y == 0:
    print('You are at the origin')
elif x == 0:
    print('You are on abscissa')
elif y == 0:
    print('You are on ordinate')
elif x > 0 and y > 0:
    print('You are at 1st grid square')
elif x < 0 and y > 0:
    print('You are at 2nd grid square')
elif x < 0 and y < 0:
    print('You are at 3rd grid square')
elif x > 0 and y < 0:
    print('You are at 4th grid square')