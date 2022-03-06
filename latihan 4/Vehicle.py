# solid fuel, liquid fuel, fuel gas, fossil, bio fuel
class Vehicle:
    def __init__(self):
        self.__fuelType="<NO fuel type>"
        self.__maxPassengers="<NO maximum>"
        self.__vecType="<NO vechile type>" # darat, air, udara

    def setVehicle(self, ft, mp, vt):
        self.__fuelType = ft
        self.__maxPassengers = mp
        self.__vecType = vt
    
    def setFuelType(self, ft):
        self.__fuelType = ft
    def getFuelType(self):
        return self.__fuelType

    def setMaxPassengers(self, mp):
        self.__maxPassengers = mp
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    def setVecType(self, ft):
        self.__vecType = ft
    def getVecType(self):
        return self.__vecType

    def Move(self):
        print("Kendaraan berjalan maju")

    def printVehicle(self):
        print("Tipe kendaraan : ", self.__vecType)
        print("Jenis bahan bakar: ", self.__fuelType)
        print("Maksimum penumpang: ", self.__maxPassengers)
        print("-------------------")

    def printVeh(self):
        print("Tipe kendaraan : ", self.__vecType)
        print("Jenis bahan bakar: ", self.__fuelType)
        print("Maksimum penumpang: ", self.__maxPassengers)