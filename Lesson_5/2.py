# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

from itertools import count

count = 0
with open("2.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print("The count of symbols in", count+1, "string is", len(line.split()))
        count += 1

print("The count of strings is", count)


