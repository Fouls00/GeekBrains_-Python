# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

new_ranking = int(input("Print new element of ranking list:"))

if new_ranking in my_list[:]:
    my_list.insert(my_list.index(new_ranking), new_ranking)

for i in my_list[:]:
    if new_ranking not in my_list[:]:
        while new_ranking > i:
            my_list.insert(my_list.index(i), new_ranking)
            break
if new_ranking not in my_list[:]:
    my_list.append(new_ranking)
print(my_list)

