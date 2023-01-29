# # Функции
# def hello_world():
#     print("hello_world")
#
#
#
# #-----------------------------------------------------------------
#
# hello_world() # Вызов функции


# def is_sorted(list1):
#     clown_l = sorted(list1) # сортированный
#     if clown_l == list1:
#         return True
#
# l = [0, 1, 2, 3, 4, 5]
#
# if is_sorted(l):
#     print("принтанул")
# else:
#     print("не принтанул")


# def find_longest(word1):
#     count1 = []
#     for i in word1:
#         count1.append(len(i))
#     ind=count1.index(max(count1))
#     return word1[ind], count1[ind]
#
# word = ["back", "rageee", "elitnie", "varvarii", "brawl"]
# print(find_longest(word))


# def min_max(qwe):
#     mini = qwe[0]
#     maxi = qwe[0]
#     for i in qwe:
#         if i > maxi:
#             maxi = i
#         elif i < mini:
#             mini = i
#     return mini, maxi
# qwe = [5, 3, 7, 2, 9]
# print(min_max(qwe))
