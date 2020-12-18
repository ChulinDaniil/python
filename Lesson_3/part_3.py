def my_func(var_1, var_2, var_3):
    maximal = max(var_1, var_2, var_3)
    other = max(min(var_1, var_2), min(var_1, var_3), min(var_2, var_3))
    return int(maximal) + int(other)

print(my_func(input('insert a number '), input('insert a number '), input('insert a number ')))