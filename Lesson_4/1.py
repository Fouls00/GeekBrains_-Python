# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, output_in_hours, hourly_rate, bonus = argv

payroll = int(output_in_hours) * int(hourly_rate) + int(bonus)

print("Script name: ", script_name)
print("Print output in hours:", output_in_hours)
print("Print hourly_rate:", hourly_rate)
print("Print bonus:", bonus)
print(payroll)
