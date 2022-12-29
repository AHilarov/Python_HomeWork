def int_check():
    while True:
        try:
            int_num = int(input('Enter integer number: '))
            return int_num
        except:
            print('You need to enter INTEGER number!')