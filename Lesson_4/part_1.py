from sys import argv

first_param, second_param, third_param, fourth_param = argv

print("Выработка в часах ", second_param)
print("Ставка ", third_param)
print("Премия ", fourth_param)
print("Итоговая зп ", (int(second_param) * int(third_param)) + int(fourth_param))