# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def parameters(name, surname, date_of_birth, city, email, phone_number):
    return name, surname, date_of_birth, city, email, phone_number


print(parameters((input("Print name of the user:")),
                 (input("Print surname of the user:")),
                 (input("Print date of birth of the user:")),
                 (input("Print city of the user:")),
                 (input("Print email of the user:")),
                 (input("Print phone number of the user:"))))
