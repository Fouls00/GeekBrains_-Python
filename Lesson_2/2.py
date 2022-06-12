# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
# Пример: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
i = 0

for i in range(int(input("Enter count of list elements:"))):
    my_list.append(int(input('Enter next number:')))
print(my_list)

a = 0
b = 1

for a in range(len(my_list)):
    while b < len(my_list):
        my_list[a], my_list[b] = my_list[b], my_list[a]
        b = b + 2
print(my_list)

