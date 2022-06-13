# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

main_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [main_list[i] for i in range(len(main_list)-1) if main_list[i+1] > main_list[i]]

print(new_list)
