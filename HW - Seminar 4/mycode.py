def int_check():
    while True:
        try:
            int_num = int(input('Enter integer number: '))
            return int_num
        except:
            print('You need to enter an INTEGER number!')

# def positive_check(num):
#     while True:
#         try:
#             num > 0
#             return num
#         except:
#             print('You need to enter a positive number greater than 0!')