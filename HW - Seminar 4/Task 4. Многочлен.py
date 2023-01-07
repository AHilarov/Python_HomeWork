# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as RI
from mycode import int_check as IC


print('Enter the degree for which you want the equation')
k=IC()
if k <1:
    print('You need to enter a positive number greater than 0!')
else:
    equation = []
    coeff = 0
    for i in range(k,0,-1):
        coeff = RI(0, 100)
        if coeff !=0:
            equation.append(coeff)
            equation.append('x^')
            equation.append(i)
            equation.append(' + ')
    equation.append(RI(0, 100))
    equation.append(' = 0')

    equation=[str(i) for i in equation]
    equation_str = ''.join(equation)
    equation_str= equation_str.replace('x^1 ', 'x ')
    equation_str= equation_str.replace('+ 0 =', '=')

    print(equation_str)