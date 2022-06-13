# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

main_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
title_list = []

# Добавляем в список new_list элементы, которые дублируются в исходном списке
new_list_generator = [new_list.append(word1) for i, word1 in enumerate(main_list) for j, word2 in enumerate(main_list)
                      if word1 == word2 and word1 not in new_list and i != j]

#Добавляем в итоговый список элементы, которые не дублируются в исходном списке
for i in main_list:
    if i not in new_list:
        title_list.append(i)

print(title_list)




