# # мутабильность
# # s = "Mavai"
# # s[1] = "0", так нельзя
#
# s = "Movavi"
# i = 0
# i += 1
#
# # списки - []
# lst = [1, 3, 54, "dfg"]
# lst.append(-3)  # добавить
# lst.remove(54)  # удалить по значению
# lst.pop(1)  # удалить по индексу
# lst1 = ["А", "Б"]
# lst.extend(lst1)  # расшираение списков
#
# print(lst)
#
# # кортеж - () || tuple
# tup = tuple(1,2,)
# tup_1 = 1,
# tup_2 = 1, 2, 3
# print(tup)
# print(type(tup))  # тип данных
#
# print(max(tup))  # максимальное значение кортежа
#
# # zip - ()
# list1 = [0, 1, 2, 3]
# list2 = ["А", "Б", "В", "Г"]
# couple = zip(list2, list1)
# print(couple)
#
#
# for element in couple:
#     print(element)
#
#
# # сравнение кортежей
# tup_a = 2*2,
# tup_b = 2*2*2,
# print(tup_b>tup_a) # True
#
# tup_c = "a",
# tup_z = "z",
# print(tup_c < tup_z)
#
# # при сравнении букв, лексикографический порядок
# tup_e = (42, "maximum")
# tup_f = (42, "minimum")
# print(tup_e < tup_f) # True
#
# # сравнение происходит до первого неравенстав
# tup_g = 999,
# print(tup_f < tup_g) # True
#
#
# tup_y = (30, 20, 10)
# tup_q = (30, 20)
# print(tup_y < tup_q)
