from maini import User

    #"Инициализация"
u1 = User("Смирнов", "Антон", "абвгдейка", "01.02.1488")
u2 = User()

    #"Авторизация"
users = (u1, u2)
l = input("Логин: ")
p = input("Пароль: ")
for u in users:
    if u.log_in(l, p):
        print("Ты прошёл аутентификацию")
        current_user = u