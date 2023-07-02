# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.


elements = [1, 2, 3, 4, 5, 6, 38, 83, 89, 7, 8, 8, 6, 5, 4, 4, 3, 3, 2, 1, 35]
index_to_remove = set()
print(elements)

for item in elements:
    for j in range(elements.index(item) + 1, len(elements)):
        if item == elements[j]:
            index_to_remove.add(elements.index(item))
            index_to_remove.add(j)
print(index_to_remove)
list_to_remove = (reversed(list(index_to_remove)))

for item in list_to_remove:
    del elements[item]
print(elements)
