from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

daftarCar1 = []
daftarCar2 = []

car1 = Car("B 0123 FA", "Lamborghini", "2019", "Merah", "2", "2")
car2 = Car("D 0000 NI", "Bugatti", "2021", "Biru", "2", "2")
car3 = Car("B 9090 JI", "Porsche", "2020", "Putih", "2", "2")
car4 = Car("A 8123 BB", "Ferarri", "2022", "Hitam", "2", "2")

daftarCar1.append(car1)
daftarCar1.append(car3)
daftarCar2.append(car2)
daftarCar2.append(car4)

daftarMotor1 = []
daftarMotor2 = []

motor1 = Motorcycle("B 1234 DA", "Honda", "2020", "Merah", "Bebek", "25 Liter");
motor2 = Motorcycle("D 1234 DA", "Kawasaki", "2021", "Merah", "Sport", "30 Liter");
motor3 = Motorcycle("B 2234 FA", "Yamaha", "2018", "Biru", "Bebek", "20 Liter");
motor4 = Motorcycle("D 2234 JA", "Suzuki", "2020", "Silver", "Sport", "35 Liter");

daftarMotor1.append(motor1)
daftarMotor1.append(motor2)
daftarMotor2.append(motor3)
daftarMotor2.append(motor4)

daftarGarasi1 = []
daftarGarasi2 = []

garasi1 = Garage("Garasi 1", "200 m2", "Mobil & Motor", [car1, car2], [motor1, motor2])
garasi2 = Garage("Garasi 2", "250 m2", "Mobil & Motor", [car3, car4], [motor3, motor4])

daftarGarasi1.append(garasi1)
daftarGarasi2.append(garasi2)

daftarParkiran1 = []
daftarParkiran2 = []

parkiran1 = ParkingLot("100", "8", [car3, car4], [motor3, motor4])
parkiran2 = ParkingLot("150", "8", [car1, car2], [motor1, motor2])

daftarParkiran1.append(parkiran1)
daftarParkiran2.append(parkiran2)

print("========================================")
print("|                Garasi                |")
print("========================================")
for garasi in daftarGarasi1:
    print("Nama             : ", garasi.getNamaGarasi())
    print("Luas             : ", garasi.getLuasGarasi())
    print("Daftar Kendaraan : ", garasi.getDaftarKendaraan())
    for car in garasi.getCar():
        print("Detail Mobil")
        print("Plat Nomor     : ", car.getPlatNomor())
        print("Merk           : ", car.getMerk())
        print("Tahun Produksi : ", car.getTahunProduksi())
        print("Jumlah Pintu   : ", car.getJumlahPintu())
        print("Jumlah Kursi   : ", car.getJumlahKursi())
    for motor in garasi.getMotorcycle():
        print("Detail Motor")
        print("Plat Nomor       : ", motor.getPlatNomor())
        print("Merk             : ", motor.getMerk())
        print("Tahun Produksi   : ", motor.getTahunProduksi())
        print("Jenis Motor      : ", motor.getJenisMotor())
        print("Kapasitas Tangki : ", motor.getKapasitasTangki())
    print("----------------------------------------")
for garasi in daftarGarasi2:
    print("Nama             : ", garasi.getNamaGarasi())
    print("Luas             : ", garasi.getLuasGarasi())
    print("Daftar Kendaraan : ", garasi.getDaftarKendaraan())
    for car in garasi.getCar():
        print("Detail Mobil")
        print("Plat Nomor     : ", car.getPlatNomor())
        print("Merk           : ", car.getMerk())
        print("Tahun Produksi : ", car.getTahunProduksi())
        print("Jumlah Pintu   : ", car.getJumlahPintu())
        print("Jumlah Kursi   : ", car.getJumlahKursi())
    for motor in garasi.getMotorcycle():
        print("Detail Motor")
        print("Plat Nomor       : ", motor.getPlatNomor())
        print("Merk             : ", motor.getMerk())
        print("Tahun Produksi   : ", motor.getTahunProduksi())
        print("Jenis Motor      : ", motor.getJenisMotor())
        print("Kapasitas Tangki : ", motor.getKapasitasTangki())
print("========================================")
print("\n")

print("========================================")
print("|              Parking Lot             |")
print("========================================")
for parkingLot in daftarParkiran1:
    print("Kapasitas        : ", parkingLot.getKapasitas())
    print("Jumlah Kendaraan : ", parkingLot.getJumlahKendaraan())
    for car in parkingLot.getCar():
        print("Detail Mobil")
        print("Plat Nomor     : ", car.getPlatNomor())
        print("Merk           : ", car.getMerk())
        print("Tahun Produksi : ", car.getTahunProduksi())
        print("Jumlah Pintu   : ", car.getJumlahPintu())
        print("Jumlah Kursi   : ", car.getJumlahKursi())
    for motor in parkingLot.getMotorcycle():
        print("Detail Motor")
        print("Plat Nomor       : ", motor.getPlatNomor())
        print("Merk             : ", motor.getMerk())
        print("Tahun Produksi   : ", motor.getTahunProduksi())
        print("Jenis Motor      : ", motor.getJenisMotor())
        print("Kapasitas Tangki : ", motor.getKapasitasTangki())
    print("----------------------------------------")
for parkingLot in daftarParkiran2:
    print("Kapasitas        : ", parkingLot.getKapasitas())
    print("Jumlah Kendaraan : ", parkingLot.getJumlahKendaraan())
    for car in parkingLot.getCar():
        print("Detail Mobil")
        print("Plat Nomor     : ", car.getPlatNomor())
        print("Merk           : ", car.getMerk())
        print("Tahun Produksi : ", car.getTahunProduksi())
        print("Jumlah Pintu   : ", car.getJumlahPintu())
        print("Jumlah Kursi   : ", car.getJumlahKursi())
    for motor in parkingLot.getMotorcycle():
        print("Detail Motor")
        print("Plat Nomor       : ", motor.getPlatNomor())
        print("Merk             : ", motor.getMerk())
        print("Tahun Produksi   : ", motor.getTahunProduksi())
        print("Jenis Motor      : ", motor.getJenisMotor())
        print("Kapasitas Tangki : ", motor.getKapasitasTangki())
print("========================================")
print("\n")

