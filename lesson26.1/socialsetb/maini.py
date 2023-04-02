import requests

class User:
    def __init__(self, usnm = "", fam = "", im = "", pas = ""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.imya = self.__data["FirstName"] if not im else im
        self.familiya = self.__data["LastName"] if not fam else fam
        self.username = self.__data["Login"] if not usnm else usnm
        self.__password = self.__data["Password"] if not pas else pas

    def log_in(self, l, p):
        if self.username == l and self.__password == p:
            return True


