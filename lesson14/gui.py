# phrase = "я всегда я, когда я есть я".lower()
# symbols = list("!@?/.,")
# phrase_cleared = ""
# for i in phrase:
#     if i not in symbols:
#         phrase_cleared += i
# print(phrase_cleared)
#
# l = phrase_cleared.split(" ")
# d = {}
#
# for element in l:
#     if element not in d:
#         d[element] = 1
#     else:
#         d[element] += 1
# print(d)


# pokupki =  {"Чипсы": 78,
#             "Кириешки": 13,
#             "Яйца": 78,
#             "Мегаантон": 999}
# s = 0
# # for i in pokupki: #перебор ключей
# for i in pokupki.values():
#     s +=i
# print(s)






phrase = "я всегда я, когда я есть я".lower()
symbols = list("!@?/.,")
phrase_cleared = ""
for i in phrase:
    if i not in symbols:
        phrase_cleared += i
print(phrase_cleared)

l = phrase_cleared.split(" ")
d = {}

for element in l:
    if element not in d:
        d[element] = 1
    else:
        d[element] += 1
print(d)
maxi = max(d.values())
print(maxi)

for (key, value) in d.items():
    if value == maxi:
        print(f" значение - {key}:{value}")



