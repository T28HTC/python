# lambda функции
# x = 10
# y = 5
# a1 = lambda x, y: x + y + 1
# print(a1(x, y))

# answer = "Д"
# result = lambda is_exit: True if is_exit == "Д" else False
# print(result(answer))


# # создание списков
# l = [ i for i in range(1, 6)]
# print(l)
#
# # 1. list comprehension всегда в []
# # 2. for i in... , обычный цикл -> столько и будет
# # 3. всёб что левее for -> элементы списка

# #Задачи
# c2f = lambda x: 9/5 * x + 32
# c2k = lambda x: x + 273.15
# k2c = lambda x: x - 273.15
# f2c = lambda x: (x - 32)*5/9
# print(c2f())

# from random import choice
# vvod = "https://www.google.com"
# slovar = {}
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
#
# code = [choice(choice(chars)) for i in range(6)]
# tvss = "".join(code)
# print(tvss)
# if vvod in slovar:
#     print(f"вот ссылка: {slovar[vvod]}")
# else:
#     slovar[vvod] = tvss
#     print(tvss)
