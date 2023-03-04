# Создайте программу для игры в ""Крестики-нолики"".
import sys, os

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

clear = lambda: os.system('cls')
clear ()
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Привет! Играть будем так. Каждой клеточке будет задан номер. Чтобы походить надо будет указать номер клеточки.')
print_matrix(field)
print('Например, чтобы походить в середину правой колонки надо ввести «6»')
field[1][2] = 'X'
print_matrix(field)
print('Ну, что? Погнали! Крестики ходят первыми')
field=[['□']*3 for i in range(3)]           
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

# === ПРОВЕРКИ ===
def field_check(matrix_2_chek):
    res = any('□' in sub for sub in matrix_2_chek)
    return res

def win_check(matrix_2_chek):
    cross_win = ['X', 'X', 'X']
    zero_win = ['O', 'O', 'O']

    comb1=[matrix_2_chek[i][0] for i in range(3)]
    comb2=[matrix_2_chek[i][1] for i in range(3)]
    comb3=[matrix_2_chek[i][2] for i in range(3)]

    comb4=[matrix_2_chek[0][j] for j in range(3)]
    comb5=[matrix_2_chek[1][j] for j in range(3)]
    comb6=[matrix_2_chek[2][j] for j in range(3)]

    comb8=[matrix_2_chek[0][2],matrix_2_chek[1][1],matrix_2_chek[2][0]]
    comb7=[matrix_2_chek[i][j] for i in range(3) for j in range(3) if i==j]     

    if comb1 == cross_win or \
        comb2 == cross_win or \
        comb3 == cross_win or \
        comb4 == cross_win or \
        comb5 == cross_win or \
        comb6 == cross_win or \
        comb7 == cross_win or \
        comb8 == cross_win:
        print_matrix(matrix_2_chek)
        print('КРЕСТИКИ ПОБЕДИЛИ!!!')
        sys.exit()
    elif comb1 == zero_win or \
        comb2 == zero_win or \
        comb3 == zero_win or \
        comb4 == zero_win or \
        comb5 == zero_win or \
        comb6 == zero_win or \
        comb7 == zero_win or \
        comb8 == zero_win:
        print_matrix(matrix_2_chek)
        print('НОЛИКИ ПОБЕДИЛИ!!!')
        sys.exit()
    else: 
        return


# === ХОДЫ ===
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
                win_check(field)
                switch = 'zero'
            else:
                field[r][c] = 'O'
                win_check(field)
                switch = 'cross'
            print_matrix(field)
        else:
            print('Сюда ходить нельзя. Уже занято')
        next_turn(switch)
    else:
        print('Ходов больше нет. Ничья.')
        return

next_turn(switch)