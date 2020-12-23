def first_func():
    try:
        var_1 = float(input('введите число: '))
        var_2 = float(input('введите еще одно число: '))
        return var_1 / var_2
    except ZeroDivisionError:
        return ('а на ноль делить нельзя!')


print(first_func())
