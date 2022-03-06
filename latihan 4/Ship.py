from Vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self):
        super().__init__()
        self.__age = "<NO age>"
        self.__type = "<NO ship type>"
        self.__countryOfManufacture = "<NO country>"

    def setShip(self, ft, mp, vt, a, t, c):
        self.setVehicle(ft, mp, vt)
        self.__age = a
        self.__type = t
        self.__countryOfManufacture = c

    def setAge(self, a):
        self.__age = a
    def getAge(self):
        return self.__age

    def setType(self, t):
        self.__type = t
    def getType(self):
        return self.__type

    def setCountryOfManufacture(self, a):
        self.__countryOfManufacture = a
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    def printShip(self):
        self.printVeh()
        print("Umur(tahun): ", self.__age)
        print("Tipe: ", self.__type)
        print("Negara: ", self.__countryOfManufacture)
        print("-------------------")
