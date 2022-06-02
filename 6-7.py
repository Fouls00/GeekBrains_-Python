# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(str_small):
    return str_small.title()


def int_fuc_2(user_int):
    user_str = user_int.split()
    for i, str_small in enumerate(user_str):
        if str_small.isascii():
            user_str[i] = int_func(str_small)
        else:
            print("Error")
    return print(' '.join(user_str))


print(int_fuc_2('text text text'))
