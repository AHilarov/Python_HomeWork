# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input('Enter day number (1 - monday... 7 - sunday): '))
if day_number == 1 or day_number == 2 or day_number == 3 or day_number == 4 or day_number == 5:
    print('weekday')
elif day_number == 6 or day_number == 7:
    print('weekend')
else:
    print('not a day number')

# нужно ввести номер дня недели 1-7

# num_day = input('Ведите номер дня недели: ')
# while num_day not in ('1', '3', '2', '4', '5', '6', '7') and num_day != 'exit': 
#     num_day = input('Ведите номер дня недели: ')

# if num_day.isdigit():
#     num_day = int(num_day)
#     print('Номер дня недели', num_day)
