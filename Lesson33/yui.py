import random
#1
# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}
# a = []
# b = []
#
# for key in slovar:
#     a.append(key)
# print(a)
#
# for value in slovar:
#     b.append(slovar.get(value))
# print(b)



#2
# x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
#      "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
#      "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
#      "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]
#
# c = input().capitalize()
# x1 = 0
# for i in range(len(x)):
#     if c==x[i]:
#         x1+=1
# print(x1, c)
# print(x.count(c))

#4
# n = int(input())
# m = []
# bukva = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(n):
#     a = random.choice(bukva)
#     m.append(a)
# print(set(m))

#5
a = [1, 15, 2, 0, 1]
a.sort()
print(a[-1]*a[-2])

##import random
##a = []
##for i in range(10):
##    a.append(random.randint(0,15))
##
##k = set(a)
##print(sorted(k))


##x = "abcdefghijklmnopqrstuvw"
##abvgdeika = list(x)
##print(''.join(abvgdeika[-1:0:-2]))
##print(''.join(abvgdeika[-1:4:-2]))

while True:
    a = input()
    if a[:5] == "Суета":
        break
