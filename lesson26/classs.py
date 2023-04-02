from random import choice
import playsound


class MusicBox:
    def __init__(self):
        self.__score = 0
        self.__variant = "abqrxz"
        self.__sequence = choice(self.__variant)

        print(self.__sequence)

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f"sound/{letter}.mp3")

    def __next(self):
        __lena = len(self.__sequence)
        self.__sequence = ""
        for _ in range(__lena):
            self.__sequence += choice(self.__variant)

    def check(self, predpologenie: str):
        if self.__sequence == predpologenie.lower():
            self.__score += 1
            playsound.playsound("sound/c.wav")
            self.__next()

        else:
            self.__score -= 0.5
            playsound.playsound("sound/i.wav")

    def get_score(self):
        return self.__score