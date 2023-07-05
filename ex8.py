# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
#   словарь, где ключ — имя друга, а значение —
#   кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
#   и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
#   с множествами. Код должен расширяться
#   на любое большее количество друзей.


friends: dict = {'Kenny': ('axe', 'boots', 'father'),
                 'Stan': ('axe', 'money', 'father', 'meat'),
                 'Cartman': ('axe', 'money', 'bow','meat'),
                 'Kyle': ('axe', 'money', 'father', 'meat')}

for friend, items in friends.items():
    print(f'Friend {friend}, items {items}')

for friend, items in friends.items():
    common_set = set()
    for friend_1, items_1 in friends.items():
        if friend != friend_1:
            common_set = set(items) - set(items_1)
    print(f'Friend {friend}, unique items {common_set}')

missing_items: dict = dict()
common_set = set()
for friend, items in friends.items():
    for friend_1, items_1 in friends.items():
        if friend != friend_1:
            if len(common_set) > 0:
                common_set.intersection_update(set(items_1))
            else:
                common_set = set(items_1)
    missing_items[friend] = common_set - set(items)
    common_set = set()

print(f'{missing_items = }')
