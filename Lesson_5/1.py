# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

flag = True
with open("1.txt", 'x', encoding='utf-8') as f:
    while flag:
        line = input("Print some text:")
        if not line:
            flag = False
        print(line, file=f)
