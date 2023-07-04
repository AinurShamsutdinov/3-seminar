# 1 Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не
# должно быть дубликатов.


list_with_duplicates = [1, 3, 4, 5, 6, 2, 3, 4, 5, 2, 92, 23, 92, 10, 31, 10, 94, 238]
dict_duplicates: dict = dict()
dict_originals: dict = dict()
list_originals: list = list()

for item in list_with_duplicates:
    if dict_duplicates.get(item) is None:
        dict_duplicates[item] = 1
    else:
        dict_duplicates[item] = dict_duplicates[item] + 1

for key, item in dict_duplicates.items():
    if item == 1:
        dict_originals[key] = item

list_originals = list(dict_originals.keys())
print(f'{list_originals = }')
