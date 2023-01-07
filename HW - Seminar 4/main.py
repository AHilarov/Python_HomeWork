from create import create_equation
from decoding import decode
from encoding import encode
from summ import sum_equation

if __name__ == '__main__':
    equation1 = create_equation() 
    equation2 = create_equation()
    print(decode(equation1))
    print(decode(equation2))
    # str_equation = decode(equation1)
    # print(str_equation)
    # str_equation = decode(equation2)
    # print(str_equation)    

    # dict_equation = encode(str_equation)
    # print(dict_equation)
    # dict_equation = encode(str_equation)
    # print(dict_equation)
 
    print(decode(sum_equation(equation1, equation2)))