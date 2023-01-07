def decode(equation:  dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0' 
    new_equation = new_equation.replace ('+ -', '- ')\
        .replace(' 1x*',' x*') .replace('x**1 ','x ') .replace('*x**0','')
    return new_equation