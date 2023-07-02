# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


list_1 = [1, 1, 2, 3, 5, 3, 4, 2, 3, 4, 5, 5, 23, 23, 58, 92, 29, 96, 45]
list_ans_1 = list()
list_ans_2 = list()
print(list_1)

for item in list_1:
    if item not in list_ans_1:
        list_ans_1.append(item)

for i in range(len(list_1)):
    is_in_list = False
    for j in range(len(list_ans_2)):
        if list_1[i] == list_ans_2[j]:
            is_in_list = True
    if not is_in_list:
        list_ans_2.append(list_1[i])

print(f'Short solution: {list_ans_1}')
print(f'Long solution: {list_ans_2}')
