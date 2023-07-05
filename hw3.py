
# 3 Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

BACKPACK_MAX_WHEIGHT: int = 15

items = {'axe': 2,
         'water botel': 2,
         'food': 5,
         'sleeping bag': 3,
         'flashlight': 1,
         'untensils': 1,
         'knife': 1,
         'soap': 1,
         'tent': 5,
         }
packed_items: dict = dict()
backpack_filled_weight: int = 0

for key, item in items.items():
    if (backpack_filled_weight + item) < BACKPACK_MAX_WHEIGHT:
        packed_items[key] = item
        backpack_filled_weight += item

print(f'{packed_items = }')
print(f'{backpack_filled_weight}')
