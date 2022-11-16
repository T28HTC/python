# import turtle
# import random
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(7)
# colors = ["red","orange","yellow","green","light blue","blue","puprle"]
#
# side = int(input("Ведите кол-во сторон:"))
# x = 80
# for i in range(0, side):
#     t.pencolor(random.choice(colors))
#     t.fd(x)
#     t.rt(360/side)
# screen.exitonclick()

# word = input("Введите слово: ")
# while word:
#     print(word, end=" ")
#     word = word[:-1]

# x = float(input("Введите число: "))
# step=0
# while x != 1:
#     step+=1
#     if x % 2 == 0:
#         x = x // 2
#         print(x)
#     else:
#         x = 3 * x + 1
#     print(x)
# print(f"Шаги - {step}")
