from Person import Person

class Job(Person):
    def __init__(self):
        super().__init__()
        self.__nip = "<NO nip>"
        self.__companyName = "<NO companyName>"
        self.__position = "<NO position>"

    def setJob(self, nik, name, gender, nip, companyName, position):
        self.setPerson(nik, name, gender)
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position
    
    def setNip(self, nip):
        self.__nip = nip
    def getNip(self):
        return self.__nip

    def setCompanyName(self, companyName):
        self.__companyName = companyName
    def getCompanyName(self):
        return self.__companyName

    def setPosition(self, position):
        self.__position = position
    def getPosition(self):
        return self.__position

    def printJob(self):
        self.printPerson()
        print("NIP            : ", self.__nip)
        print("Nama Perusahaan : ", self.__companyName)
        print("Posisi         : ", self.__position)