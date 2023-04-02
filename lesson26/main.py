from classs import MusicBox


pleer = MusicBox()

while True:
    pleer.play()
    guess = input("Что ты услышал: ")
    if guess == "":
        break
    print("Очки: ", pleer.get_score())
pleer.check(guess)
