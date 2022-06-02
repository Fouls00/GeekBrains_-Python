# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
<<<<<<< Updated upstream
=======

def my_func(arg_1, arg_2):
    return arg_1 ** arg_2 if arg_2 < 0 else print("Needs negative value, try again")


print(my_func(float(input("Print float number:")), int(input("Print int number:"))))


# 2 Way

def my_func(arg_1, arg_2):
    i = 1
    arg_3 = 1
    while i <= abs(arg_2):
        arg_3 = arg_3 * arg_1
        i += 1
    return 1 / arg_3 if arg_2 < 0 else print("Needs negative value, try again")


print(my_func(float(input("Print float number:")), int(input("Print int number:"))))
>>>>>>> Stashed changes

def my_func(arg_1, arg_2):
    return arg_1 ** arg_2 if arg_2 < 0 else print("Needs negative value, try again")


print(my_func(float(input("Print float number:")), int(input("Print int number:"))))


# 2 Way

def my_func(arg_1, arg_2):
    i = 1
    arg_3 = 1
    while i <= abs(arg_2):
        arg_3 = arg_3 * arg_1
        i += 1
    return 1 / arg_3 if arg_2 < 0 else print("Needs negative value, try again")


print(my_func(float(input("Print float number:")), int(input("Print int number:"))))
