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


friends: dict = {'Kenny': ('axe', 'boots', 'firewood'),
                 'Stan': ('axe', 'boots', 'water', 'meat'),
                 'Cartman': ('axe', 'boots', 'bow', 'meat')}

# for friend, items in friends.items():
#     print(f'Friend {friend}, items {items}')
#
# for friend, items in friends.items():
#     diff: set = set()
#     for friend_1, items_1 in friends.items():
#         if friend != friend_1:
#             diff.update(set(items_1))
#     intersection = set(items) - diff
#     print(f'Friend {friend}, unique items {intersection}')

unique_set: set = set()
for friend, items in friends.items():
    inter_set: set = set()
    for friend_1, items_1 in friends.items():
        if friend != friend_1:
            inter_set.update((set(items).intersection(set(items_1))))
    print(f'Friend {friend}, intersection items {inter_set}')
    same_items = set(items) - inter_set
    print(f'Friend {friend}, same items {same_items}')
