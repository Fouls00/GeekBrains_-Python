# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

surname = []
i = 0
count = 0
aver_salary = 0

with open("3.txt", 'r', encoding='utf-8') as f:
    for line in f:
        # name, salary = (i for i in line.split())
        # if float(word) < 20000:
        #     surname.append(name)
        for word in line.split():
            try:
                if float(word) < 20000:
                    surname.append(line.split())
                count += 1
                aver_salary += float(word)
                aver_salary /= count
            except ValueError:
                pass

print(surname)
print(aver_salary)

