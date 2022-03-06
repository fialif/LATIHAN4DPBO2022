from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

print("** Data Kendaraan **")
v1 = Vehicle()
v1.setVehicle("Biofuel", 1000, "Laut")
v1.printVehicle()
# 2
v1.setVehicle("Liquid Fuel", 2, "Darat")
v1.printVehicle()
# 3
v1.setVehicle("Liquid fuel", 50, "Darat")
v1.printVehicle()
# 4
v1.setVehicle("Liquid fuel", 8, "Darat")
v1.printVehicle()
# 5
v1.setVehicle("Fuel Gas", 100, "Udara")
v1.printVehicle()

print("** Data Kapal **")
s1 = Ship()
s1.setShip("Biofuel", 1000, "Laut", 20, "Kargo", "Indonesia")
s1.printShip()
# 2
s2 = Ship()
s2.setShip("Biofuel", 100, "Laut", 50, "Steamboat", "Jerman")
s2.printShip()
# 3
s3 = Ship()
s3.setShip("Biofuel", 100, "Laut", 50, "Oil tanker", "Indonesia")
s3.printShip()
# 4
s4 = Ship()
s4.setShip("Biofuel", 130, "Laut", 40, "Steamboat", "Jerman")
s4.printShip()
# 5
s5 = Ship()
s5.setShip("Biofuel", 160, "Laut", 50, "Amphibious transport dock", "Jerman")
s5.printShip()

print("** Data Pesawat **")
a1 = Airplane()
a1.setAirplane("Fuel Gas", 100, "Udara", 5, "Airbus A330", 15)
a1.printAirplane()

# 2
a2 = Airplane()
a2.setAirplane("Fuel Gas", 215, "Udara", 6, "Boeing 737", 18)
a2.printAirplane()
# 3
a3 = Airplane()
a3.setAirplane("Fuel Gas", 230, "Udara", 3, "Airbus A320", 15)
a3.printAirplane()
# 4
a4 = Airplane()
a4.setAirplane("Fuel Gas", 78, "Udara", 5, "ATR 72", 17)
a4.printAirplane()
# 5
a5 = Airplane()
a5.setAirplane("Fuel Gas", 390, "Udara", 7, "Boeing 777", 19)
a5.printAirplane()