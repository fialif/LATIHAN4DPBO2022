from Job import Job

class Driver(Job):
    def __init__(self):
        super().__init__()
        self.__lisenceID = "<NO lisence ID>"
        self.__activeUntil = "<NO actived>"
        self.__vehicleType = "<NO type>"

    def setDriver(self, nik, name, gender, nip, companyName, position, lisenceID, activeUntil, vehicleType):
        self.setJob(nik, name, gender, nip, companyName, position)
        self.__lisenceID = lisenceID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def setLisenceID(self, lID):
        self.__lisenceID = lID
    def getLisenceID(self):
        return self.__lisenceID

    def setActiveUntil(self, aU):
        self.__activeUntil = aU
    def getActiveUntil(self):
        return self.__activeUntil

    def setVehicleType(self, vt):
        self.__vehicleType = vt
    def getVehicleType(self):
        return self.__vehicleType

    def printDriver(self):
        self.printJob()
        print("No SIM         : ", self.__lisenceID)
        print("aktif sampai   : ", self.__activeUntil)
        print("tipe kendaraan : ", self.__vehicleType)
