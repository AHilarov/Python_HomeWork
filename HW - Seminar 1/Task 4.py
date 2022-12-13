# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

grid_square_num = int(input('Enter grid square number (1-4): '))
if grid_square_num == 1:
    print(f'For grid square number {grid_square_num} coordinates are: x > 0, y > 0')
elif grid_square_num == 2:
    print(f'For grid square number {grid_square_num} coordinates are: x < 0, y > 0')
elif grid_square_num == 3:
    print(f'For grid square number {grid_square_num} coordinates are: x < 0, y < 0')
elif grid_square_num == 4:
    print(f'For grid square number {grid_square_num} coordinates are: x > 0, y < 0')
else:
    print('You entered wrong number')

