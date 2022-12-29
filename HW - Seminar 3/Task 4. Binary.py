# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from mycode import int_check as IC

def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2) 
    print(n%2, end=' ')

decimalToBinary(IC())