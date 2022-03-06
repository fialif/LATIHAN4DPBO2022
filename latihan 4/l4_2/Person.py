class Person:
    def __init__(self):
        self.__nik = "<NO NIK>"
        self.__name = "<NO name>"
        self.__gender = "<NO gender>"

    def setPerson(self, nik, name, gender):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
    
    def sleep(self):
        print("Tidur 8 jam")

    def setNIK(self, nik):
        self.__nik = nik
    def getNIK(self):
        return self.__nik

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender
    def getGender(self):
        return self.__gender

    def printPerson(self):
        print("NIK            : ", self.__nik)
        print("Nama           : ", self.__name)
        print("Gender         : ", self.__gender)