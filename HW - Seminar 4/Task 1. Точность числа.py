# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from mycode import int_check as IC

print('This programm returns Pi number. How accurate result you need (0-10)?')
num_pi = str(math.pi)
d = IC()
stop = num_pi.find('.')+1+d
print(num_pi[:stop])


# альтернативное более правильное решение
# print(round(math.pi, d))