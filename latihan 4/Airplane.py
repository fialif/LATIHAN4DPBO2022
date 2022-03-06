from Vehicle import Vehicle

class Airplane(Vehicle):
    def __init__(self):
        super().__init__()
        self.__age = "<NO age>"
        self.__type = "<NO Airplane type>"
        self.__wingsLength = "<NO country>"

    def setAirplane(self, ft, mp, vt, a, t, c):
        self.setVehicle(ft, mp, vt)
        self.__age = a
        self.__type = t
        self.__wingsLength = c

    def setAge(self, a):
        self.__age = a
    def getAge(self):
        return self.__age

    def setType(self, t):
        self.__type = t
    def getType(self):
        return self.__type

    def setWingsLength(self, a):
        self.__wingsLength = a
    def getWingsLength(self):
        return self.__wingsLength

    def printAirplane(self):
        self.printVeh()
        print("Umur(tahun): ", self.__age)
        print("Tipe: ", self.__type)
        print("Panjang sayap(m): ", self.__wingsLength)
        print("-------------------")
