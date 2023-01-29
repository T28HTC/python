fasol = 20
bery = 1
bery2 = 2
bery3 = 3
while True:
    if fasol > 1:
        ckolko_vozmesh1 = int(input("Сколько ты хочешь взять фасолин: "))
        while ckolko_vozmesh1 == 1 or ckolko_vozmesh1 == 2 or ckolko_vozmesh1 == 3:
            fasol1 = fasol - ckolko_vozmesh1
            print(f"Фасолей после хода 1-ого игрока: {fasol1}")
            while True:
                ckolko_vozmesh1 = int(input("Сколько ты хочешь взять фасолин: "))
                while ckolko_vozmesh1 == 1 or ckolko_vozmesh1 == 2 or ckolko_vozmesh1 == 3:
                    fasol2 = fasol1 - ckolko_vozmesh1
                    print(f"Фасолей после хода 2-ого игрока: {fasol2}")

