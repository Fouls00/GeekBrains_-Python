# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input("Enter words separated with space:").split()
print(user_str)

# 1 способ
for count, word in enumerate(user_str, 1):
        if len(word) >= 10:
            print(count, word[:10])
        else:
            print(count, word)

# 2 способ
n = 1
for i in user_str:
    print(n, i[:10]) if len(i) >= 10 else print(n, i)
    n += 1


