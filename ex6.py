# Задание №6

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text: str = input('Enter text: ')
text.replace('.', '').replace(',', '')
text_list: list = text.split(' ')
text_list.sort()
max_tab: int = int()

for item in text_list:
    if max_tab <= len(item):
        max_tab = len(item)
num: int = int()
for item in text_list:
    num += 1
    print(f'{num} {item:>{max_tab}}')
