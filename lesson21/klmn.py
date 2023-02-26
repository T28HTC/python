# Обработка ошибок
# 1
# try:
# #     a = int(input("Введите число: "))
# # except ValueError:
# #     print("бла-бла-бла")
# # except ZeroDivisionError:
# #     print("На ноль делить нельзя")
# #
# # # 2
# # try:
# #     a = int(input("Введите число: "))
# # except (ValueError, ZeroDivisionError):
# #     print("бла-бла-бла")
# #
# #
# # # 3
# # try:
# #     a = int(input("Введите число: "))
# # except ValueError:
# #     print("бла-бла-бла")
# # except ZeroDivisionError:
# #     print("На ноль делить нельзя")
# # except Exception:
# #     pass
# # else:
# #     print("ass")
# # finally:              # в любом случае
# #     print("Я устал")
# #
# # # 4
# # x = int(input("Введи имя друга: "))
# # try:
# #     if x == "Антон":
# #         raise NameError("Гай 👩🏿‍🦱")
# # except NameError as pelmen:
# #     print("Леее брат", pelmen)

#1-задача
# def succ():
#     s = 0
#     k = 0
#     for numb in content:
#         try:
#             s+=int(numb)
#         except ValueError:
#             print("Найдено не число", numb)
#         else:
#             k+=1
#         if k == 0:
#             return  "Чисел нет"
#     return round(s / k, 2)
#
# try:
#     f = open("drug.txt", "r", encoding='utf-8')
# except:
#     print("Файла нет")
#     quit()
# content = f.read().split()
# print(content)
#
#
# print(succ())


#2-задача
try:
    f = open("drug.txt", "r", encoding='utf-8')
except:
    print("Файла нет")
    quit()
content = f.readlines()
if content ==[]:
    print("Файл пустой")
    exit()
print(content)

for i, student in enumerate(content):
    content[i] = student.split()

maxi = -1
fst = ""
scd = ""
for student in content:
    try:
        if int(student[3]) > maxi:
            maxi = int(student[3])
            fst = student[1]
            scd = student[2]
    except ValueError:
        print("Запсиь неккоректна: ", student)
    except IndexError:
        print("Число отсутсвует")
print(maxi)