# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

user_month = int(input("Print number of the month:"))

dict_sample = dict({
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
})

for key in dict_sample:
    if key == user_month:
        print("By the dict way to solve:")
        print('Season time for the month is', dict_sample[key])

# 2 способ
print("By the list way to solve:")
season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print('Season time for the month is', season_list[user_month-1])

