# Словарь
#
# empty_dictionary = {}
# empty_dictionary1 = dict()
#
# dict1 = {"key1": 15 ,
#          "key2": [1,2,3],
#          "key3": "балдёж",
#          "key4": {"Владик": True}}
#
# print(dict1["key3"])
#
# print(len(dict1))

# Множества
# 1. Повторения исключены
# 2. Неупорядочный тип данных
# 3. Элементы множества не изменяются
#
#
# set1 = {"Антон", "Антон", "Антон"} # Повторение исключено
# print(set1)
# set2 = {"A", "B", "C"} # Неупорядочный тип данных
# print(set2)
# # Неизменяемые: кортеж, float, int, str, bool
# set3 = {1, "Один", [1]}
#
# empty_set = set()

# Операция со множеством
# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2)) # или оператором |
# print(set1 | set2)
#
# # Пересечение
# print(set1.intersection(set2))
#
# # Разность
# print(set1.difference(set2))

# from random import randint
# lst = []
#
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst)
# print(f"len({unique}) шт.: {unique})")

from random import randint
size = randint(100, 1000)
r_start = 0
r_end = 10_000
