# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    min_arg = min(arg_1, arg_2, arg_3)

    if min_arg == arg_1:
        return arg_2 + arg_3
    elif min_arg == arg_2:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


# print(my_func(4, 5, 6))


print(my_func(int(input("Print first argument:")), int(input("Print second argument:")),
              int(input("Print third argument:"))))
