# Создайте программу для игры в ""Крестики-нолики"".

def int_check():
    while True:
        try:
            int_num = int(input('Введите число от 1 до 9: '))
            if int_num in range(1, 10):
                return int_num
            else:
                print('Так не пойдёт!')
            # return false
        except:
            print('Так не пойдёт!')

def print_matrix(martix):
    for i in field:
        print(*i)


# === НАЧАЛО ИГРЫ ===
# def start():
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Привет! Играть будем так. Каждой клеточке будет задан номер. Чтобы походить надо будет указать номер клеточки.')
print_matrix(field)
print('Например, чтобы походить в середину правой колонки надо ввести «6»')
field[1][2] = 'X'
print_matrix(field)
print('Ну, что? Погнали! Крестики ходят первыми')
field=[['□']*3 for i in range(3)]           # field = [['□', '□', '□'], ['□', '□', '□'], ['□', '□', '□']]

switch = 'cross'

# === ПОЛЕ ===
dictionary = \
    {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }


def field_check(matrix_2_chek):
    res = any('□' in sub for sub in matrix_2_chek)
    return res


def next_turn(arg):
    switch = arg
    if field_check(field) == True:
        if switch =='cross':
            print("Ход крестиков")
        else:
            print("Ход ноликов")

        temp = dictionary[int_check()]
        r = temp[0]
        c = temp[1]

        if field[r][c] == '□':
            if switch =='cross':
                field[r][c] = 'X'
                switch = 'zero'
            else:
                field[r][c] = 'O'
                switch = 'cross'
            print_matrix(field)
        else:
            print('Сюда ходить нельзя. Уже занято')
        next_turn(switch)
    else:
        print('Ходов больше нет')
        return

next_turn(switch)
