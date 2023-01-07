def sum_equation (first_eq: dict, second_eq: dict):
    final_equation = {}
    final_equation.update(first_eq)
    final_equation.update(second_eq)

    for key in final_equation:
        final_equation[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    
    return final_equation