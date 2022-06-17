# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator, constants

with open("4.txt", 'r', encoding='utf-8') as f:
    content = f.read().splitlines()
    content = str(content)

translator = Translator()

translation = translator.translate(content, dest='ru')
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")