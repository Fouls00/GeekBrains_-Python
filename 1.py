# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
<<<<<<< Updated upstream
=======

def my_operation(arg_1, arg_2):
    try:
        return int(arg_1) / int(arg_2)
    except ZeroDivisionError:
        print("The second number is wrong")


print(my_operation(int(input("Print first number:")), int(input("Print second number:"))))
>>>>>>> Stashed changes

def my_operation(arg_1, arg_2):
    try:
        return int(arg_1) / int(arg_2)
    except ZeroDivisionError:
        print("The second number is wrong")


print(my_operation(int(input("Print first number:")), int(input("Print second number:"))))
