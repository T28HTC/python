# print(1, 2, 3, sep="|", end="")
# # OOП
# # 1. Инкапсуляция: privat and public
# # 2. Наследование: родительский и дочерний класс, super
# # 3. Полиморфизм: магические методы
#
# class Urok:
#     bobik = 14  # статический Public атрибут
#     __secret = 123  # статический Public атрибут
#
#     def __init__(self, dlitelnost):
#         self.dlitelnost = dlitelnost  # динамический Public атрибут
#         self.__secret2 = 321 # динамический приватный атрибут
#
#     def get5(self):  # публичный
#         return 5
#
#
# matan = Urok(50)  # инициализация-> создание obj на основе класса
# print(matan.get5())
# print(matan.dlitelnost)
#
# fizica = Urok(10)
# print(fizica.bobik)  # вызов статического атрибута
#
# Urok.bobik = "abobus"
# print(matan.bobik)

"Полиморфизм"
# class Cls1:
#     def __call__(self, *args, **kwargs):
#         print(args)
#         print(kwargs)  # работа при вызове объекта класса
#         return "Gosha"
#
#     def __add__(self, other): # ПРИ СЛОЖЕНИИна входе операнды
#         return f"{self} + {other}"
#
#
# class Cls2:
#     def __str__(self):
#         return "tinker"
#
#
# c1 = Cls1()  # __init__
# c2 = Cls2()  # __init__
# print(c1(1, [""], key1={}))  # __call__
# print(c2)
# print(c1 + c2)
# print(c1.__add__(c2))  # строка выше - (46)

"Наследование"


class Cl1:
    def __init__(self):
        self.pensil = "pen"

    def say(self):
        print("прив")


class Cl2(Cl1):  # класс2 наследник класса1
    def __init__(self):
        super().__init__()  # вызов init из первого во второе
        self.pensilcase = "osel"


abj1 = Cl1()
print(abj1.pensil)
abj2 = Cl2()
print(abj2.pensil)

print(hasattr(abj2, "pensilcase"))
print(getattr(abj2, "pensilcase"))