# while True:
#     try:
#         a = int(input("Ярусов: "))
#         if a < 1:
#             raise Exception("Ты осёл")
#     except ValueError:
#         print("Глупый пёс")
#         continue
#     except Exception as error:
#         print("аут", error)
#     else:
#         break
#
# while True:
#     char = input("Символ: ").strip()
#     if len(char) != 1:
#         print("Введи один символ")
#     else:
#         break
# for i in range(1, a+1):
#     print(" " * (a - i), end="")
#     print(char * i, end="||")
#
#     print(char * i)

# x = int(input("Введи число: "))
# for i in range(0, 11):
#     print(x * i)


# secret_word = "огурец"
# attempts = 5
# user_chars = []
#
# print("Сыграем в игру - угадай слово!")
# print("При победе даётся огурец!")
#
# for i in range(len(secret_word)):
#     print("@", end=" ")
#
# while True:
#     user_char = input("Введите букву! ")
#
#     if user_char in secret_word:
#         print("Верно!")
#         user_chars.append(user_char)
#     else:
#         print("Нет такой буквы!")
#
#     if len(secret_word) == len(user_chars):
#         print("ПОБЕДА!! Вы получаете орурец в подарк!")
#         print("Это было слово: ", secret_word)
#         break
#
#     attempts -= 1
#     if attempts < 0:
#         print("Вы проиграли...")
#
#     for i in secret_word:
#         if i in user_chars:
#             print(i, end=" ")
#         else:
#             print("@", end=" ")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sh_end = False
while not sh_end:
    txt = input("Введите слово: ")



    cp_txt = ""
    for ltr in txt:
        if ltr == "":
            cp_txt += ltr
        else:
            pst = alphabet.index(ltr)
            if pst + shift > len(alphabet):
                nw_pst = pst + shift - len(alphabet)
            elif pst + shift <0:
                nw_pst = pst + shift + len(alphabet)
            else:
                nw_pst = pst + shift
            cp_txt += alphabet(nw_pst)