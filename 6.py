# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

i = 1
cargo = []
n = int(input("Enter main count of cargo:"))

for i in range(n):
    name = int(input("Enter name of cargo:"))
    price = int(input("Enter price of cargo:"))
    amount = int(input("Enter amount of cargo:"))
    unit = int(input("Enter units of cargo:"))
    cargo.append((i, {'Name': name,
                      'Price': price,
                      'Amount': amount,
                      'Un': unit}))
    i += 1
print(cargo)

cargo_dict = {'Name': [], 'Price': [], 'Amount': [], 'Un': []}

for product in cargo:
    cargo_dict['Name'].append(product[1]['Name'])
    cargo_dict['Price'].append(product[1]['Price'])
    cargo_dict['Amount'].append(product[1]['Amount'])
    cargo_dict['Un'].append(product[1]['Un'])
print(cargo_dict)
