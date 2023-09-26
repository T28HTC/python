# def fds(x: int = "ы") -> int:  # type hint
#     """
#     Функция
#     :param x: ы или Ы
#     :return: эхо функция
#     """
#     return x
#
# p = fds()

# def aoa(z, *args, **kwags):
#     # args - позиционный аргумент
#     # kwargs - keywords arguments, ключ и значение
#     print(kwags)
#     print(args)
#
#
# print(aoa(1, 2, 3, a=32, soroka="e"))

# 1

# def bobik(**kwargs):
#     for i in kwargs:
#         print(i.ljust(20) + str(kwargs[i]).rjust(10))
#
#     total = sum(kwargs.values())
#     print(total)
#
# bobik(apple=105, banane=230, tude=132)

#2

# def abobus(stroka:str)-> str:
#     a = ''
#     for i in stroka:
#         if i.isupper():
#             a+= "_" + i.lower()
#         else:
#             a += i
# print(abobus("word"))
# print(abobus("OutworldDestroy"))


#ООП, снова
# Оъектно-ориентированное программирование
class Human:

    def say(self, gh): #метод публичный
        self.__dhoh()  #вызов привата
        return "o" + gh
    def __dhoh(self): #метод приватный
        print("вдох*")

    def __init__(self):
        self.age = 5 # atribute dinamic


petr = Human()
print(petr.say("Ghb"))
igor = Human()
print(petr.age)