# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

max_length = int(input("Print count of numbers:"))

for i in count(int(input("Print first-step number:"))):
    print(i)
    if i == max_length:
        break

user_list = input("Print elements split with space:").split()
i = cycle(user_list)

flag = True
key = 0

while flag:
    print(next(i))
    key += 1
    if key == len(user_list):
        flag = False


