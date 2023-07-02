# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

elements_tuple = int(123), float(23.45), 'Hello World!'
dictionary = dict()
for item in elements_tuple:
    type_of_element = type(item)
    dictionary[type_of_element] = item
print(f'{elements_tuple = }')
print(f'{dictionary = }')
