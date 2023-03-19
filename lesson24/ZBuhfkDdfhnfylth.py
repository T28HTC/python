# class Machina:
#     def __init__(self, whell: int, doors: int, pdk: bool):
#         self.whells = whell
#         self.doors = doors
#         self.pdk = pdk
#         self.__runway = 350_000
#
#     def go_out(self):
#         if self.pdk == True:
#             self.pdk = False
#             return "Дяди Коли нет"
#         else:
#             return "Дяди коли не было"
#
#     def __obnulenie(self):
#         self.__runway = 0
#
#
#     def selling(self):    # в публином методе мы вызвали привытный метод
#         self.__obnulenie()
#
# car = Machina(4, 4, True)
#
# print(car.doors, car.whells, car.pdk, car.go_out())
# car.pdk = False                                    # можно изменять значение вне функции
# print(car.doors, car.whells, car.pdk, car.go_out())
#
#
# # print(car.__runway) # приват нельзя выводить
# car.__runway = 500    # китайская копия
# car.__runway = car.__runway + 500 # никак не изменить
# print(car.__runway)   # вывод китайской копии

# import string
#
# class Alphabet:
#     def __init__(self):
#         self.__lang = "eng"
#         self.__letters = string.ascii_lowercase
#
#
#     def print(self):
#         return self.__letters
#
#     def letters_num(self):
#         return len(self.__letters)
#
#
# print(Alphabet.print())



# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def pervi(self):
#         return "Автомобиль заведён"
#
#     def vtoroi(self):
#         return "Автомобиль заглушён"
#
#     def tri(self):
#         return self.color
#
#     def chetvertoe(self):
#         return self.type
#
#     def piatoe(self):
#         return self.color
#
#
# car1 = Car(color="green", type="Opel Blitz", year="1942")
#
#
# print(car1.pervi())
# print(car1.vtoroi())
# print(car1.tri())
# print(car1.chetvertoe())
# print(car1.piatoe())

import datetime

class Chasi:
    def __init__(self):
        self.ntime = datetime.datetime.now().strftime("H, M S")






