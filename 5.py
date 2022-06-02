# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

def my_func(user_str):
    try:
        i = 0
        new_str_int = []
        return sum(int(i) for i in user_str.split())
    except ValueError:
        print("You picked a wrong symbol. Print a number")
        while i < len(user_str):
            user_str_num = ''
            a = user_str[i]
            while '0' <= a <= '9':
                user_str_num += a
                i += 1
                if i < len(user_str):
                    a = user_str[i]
                else:
                    break
            i += 1
            if user_str_num != '':
                new_str_int.append(int(user_str_num))
        return sum(new_str_int)


print(my_func(input("Print numbers split with space:")))
