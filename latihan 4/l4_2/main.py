from Driver import Driver

print("** Data Driver **")
d1 = Driver()
d1.setDriver("317401", "Tigore", "Male", "29383", "BlueBird", "Karyawan Tetap", "34763", 2028, "Mobil")
d1.printDriver()
print("-------------------")
# 2
d2 = Driver()
d2.setDriver("317402", "Sisi", "Female", "29373", "BlueBird", "Karyawan Tetap", "34735", 2028, "Mobil")
d2.printDriver()
print("-------------------")
# 3
d3 = Driver()
d3.setDriver("317403", "Ryan", "Male", "29383", "BlueBird", "Karyawan Kontrak", "34363", 2025, "Mobil")
d3.printDriver()
print("-------------------")
# 4
d4 = Driver()
d4.setDriver("317404", "Anne", "Female", "29383", "BlueBird", "Karyawan Tetap", "34983", 2028, "Mobil")
d4.printDriver()
print("-------------------")
# 5
d5 = Driver()
d5.setDriver("317405", "Niall", "Male", "29383", "BlueBird", "Karyawan Tetap", "34564", 2027, "Mobil")
d5.printDriver()
print("-------------------")

from Job import Job
print("** Data Job **")
# print("===================")
j1 = Job()
j1.setJob("317401", "Tigore", "Male", "29383", "BlueBird", "Karyawan Tetap")
j1.printJob()
print("-------------------")
# 2
j2 = Job()
j2.setJob("317402", "Sisi", "Female", "29373", "BlueBird", "Karyawan Tetap")
j2.printJob()
print("-------------------")
# 3
j3 = Job()
j3.setJob("317403", "Ryan", "Male", "29383", "BlueBird", "Karyawan Kontrak")
j3.printJob()
print("-------------------")
# 4
j4 = Job()
j4.setJob("317404", "Anne", "Female", "29383", "BlueBird", "Karyawan Tetap")
j4.printJob()
print("-------------------")
# 5
j5 = Job()
j5.setJob("317405", "Niall", "Male", "29383", "BlueBird", "Karyawan Tetap")
j5.printJob()
print("-------------------")

from Person import Person

print("** Data Person **")
p1 = Person()
p1.setPerson("317401", "Tigore", "Male")
p1.printPerson()
print("-------------------")
# 2
p2 = Person()
p2.setPerson("317402", "Sisi", "Female")
p2.printPerson()
print("-------------------")
# 3
p3 = Person()
p3.setPerson("317403", "Ryan", "Male")
p3.printPerson()
print("-------------------")
# 4
p4 = Person()
p4.setPerson("317404", "Anne", "Female")
p4.printPerson()
print("-------------------")
# 5
p5 = Person()
p5.setPerson("317405", "Niall", "Male")
p5.printPerson()
print("-------------------")