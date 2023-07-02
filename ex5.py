# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.


elements = [1, 2, 3, 4, 5, 6, 38, 83, 89, 7, 8, 8, 6, 5, 4, 4, 3, 3, 2, 1, 35]
odd_elements = []

for index in range(len(elements)):
    if (elements[index] % 2) == 1:
        odd_elements.append(index + 1)

print(elements)
print(odd_elements)
