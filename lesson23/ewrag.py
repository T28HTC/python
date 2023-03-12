# class Person:
#     def __init__(self, imya, status):   # магия инициализации
#         self.mishurik = imya
#         self.status = status
#
#     def __str__(self):
#          return f"{self.mishurik}, {self.status}"
#
#     def common_method(self):
#         print("Вышел дима из аптеки, налетели гамасеки")
#
# chelovek = Person("gay", "wqe")
# print(chelovek.mishurik)
# print(chelovek)
# print(chelovek.common_method())



# 1-question


# class Person:
#     def __init__(self, imya, familiya, vozrast):
#         self.imya = imya
#         self.familya = familiya
#         self.vozrast = vozrast
#
#     def __str__(self):
#         return f"{self.imya}, {self.familya},{self.vozrast}"
#
#     def greet(self):
#         print(f"Hello! я {self.imya} {self.familya}, мне {self.vozrast}")
#
#
# vozrast = 19
# chelovek = Person("ZYbilo", "Zybilovich", vozrast)
# print(chelovek)
# print(chelovek.imya, chelovek.familya, chelovek.vozrast)
# chelovek.greet()


# 2-question

from random import randint
class Klass:

    def __init__(self, uchenick):
        self.uchenick = uchenick
        self.grades = [randint(2, 5) for i in range(randint(5, 10))]
        self.sb = sum(self.grades)/len(self.grades)

study = Klass("Jhon")
study1 = Klass("Jack")
study2 = Klass("Jhony")
study3 = Klass("Billy")

l = [study, study1, study2, study3]
d = {}
for student in l:
    d[student.uchenick] = student.sb

print(d)
sorted_tuple = dict(reversed(sorted(d.items(), key=lambda x: x[1])))
print("====", sorted_tuple)