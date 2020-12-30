def personal_data(var_1, var_2, var_3, var_4, var_5, var_6):
    data_print = (var_1, var_2, var_3, var_4, var_5, var_6)
    data_print = str(data_print)
    return print(data_print)


personal_data(var_1=input('введите имя '), var_2=input('введите фамилию '), var_3=input('введите год рождения '),
              var_4=input('введите город проживания '), var_5=input('введите контактный email '),
              var_6=input('введите контактный номер телефона '))
