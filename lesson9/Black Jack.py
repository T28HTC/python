import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = "y"
while is_game == "y":
    comp = [random.choice(cards)]
    player = [random.choice(cards)]
    score = 0
    get_cards = "y"
    while get_cards == "y":
        player.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            """если туз в руке и сумма > 11"""
            for i in range(0, len(player)):
                if player[i] == 11:
                    player[i] = 1
                    break
        score = sum(player)
        print(f"Твоя рука: {player}, очков: {score}")
        print("Первая карта компьютера:", comp[0])
        if score > 21:
            get_cards = "h"
        else:
            get_cards = input("y - взять карту, n - остановится")

        while sum(comp) < 17:
            comp.append(random.choice(cards))
        if sum(comp) > 21 and 11 in comp:
            """если туз в руке и сумма > 11"""
            for i in range(0, len(player)):
                if comp[i] == 11:
                    comp[i] = 1
                    break
        score_comp = sum(comp)
        print("=" * 10)
        print((f"Твоя итоговая рука:{player}, очков:{score}"))
        print((f"Твоя итоговая рука:{comp}, очков:{score_comp}"))



        if score > 21 and score_comp > 21:
            print("Перелёт у обоих, ничья")
        elif score > 21:
            print("Твой перелёт, твоё поражение")
        elif score_comp > 21:
            print("Перелёт пк, победа")
        elif score == score_comp:
            print("Ничья")
        elif score > score_comp:
            print("Победа")
        else:
            print("Поражение")


