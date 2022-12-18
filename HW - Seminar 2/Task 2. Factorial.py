# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def int_check():
    while True:
        try:
            int_num = int(input('Enter integer number: '))
            return int_num
        except:
            print ('You need to enter INTEGER number!')


factorial = int_check()
new_list=[1]
for i in range(factorial):
    new_list.append(new_list[i]*(i+1))
new_list.remove(1)
print(new_list)




# def my_factorial (n):
#     if n == 1:
#         return 1
#     return n * my_factorial(n-1)

# print(my_factorial(n))

