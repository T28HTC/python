# cvet1 = input("Введите первый основной цвет: ").lower().strip()
# cvet2 = input("Введите второй основной цвет: ").lower().strip()
# c = ("красный", "синий", "желтый")
#
# while True:
#     if cvet1 and cvet2 not in c:
#         print("You so typaya dura")
#         break
#
#     elif (cvet1 == c[0] and cvet2 == c[1]) or (cvet1 == c[1] and cvet2 == c[0]):
#         print('фиолетовый')
#
#     elif (cvet1 == c[1] and cvet2 == c[2]) or (cvet1 == c[2] and cvet2 == c[1]):
#         print("оранжевый")
#
#     elif (cvet1 == c[0] and cvet2 == c[2]) or (cvet1 == c[2] and cvet2 == c[0]):
#         print("Зелёный")
#
#     break

nachalo = input("Начaло урока: ")
dlitelnost = int(input("Длительность урока: "))
peremena = int(input("Длительность перемены: "))
n = int(input("Кол-во уроков: "))

h, m = nachalo.split(":")
h,m = int(h), int(m)
time = h*60+m

for i in range(n):
    print(f"Урок {i+1} - ", end="")
    h = time//60
    m = time % 60
    print(f"{str(h).rjust(2,'0')}:{str(m).ljust(2, '0')}")
    time = time + dlitelnost
    h = time // 60
    m = time % 60
    print(f"{str(h).rjust(2, '0')}:{str(m).ljust(2, '0')}")
