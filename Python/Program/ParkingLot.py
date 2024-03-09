from Car import Car
from Motorcycle import Motorcycle

class ParkingLot:
    __kapasitas = ""
    __jumlahKendaraan = ""

    def __init__(self, kapasitas = "", jumlahKendaraan = "", car = [], motorcycle = []):
        self.__kapasitas = kapasitas
        self.__jumlahKendaraan = jumlahKendaraan
        self.__car = car
        self.__motorcycle = motorcycle

    def getKapasitas(self):
        return self.__kapasitas
    
    def setKapasitas(self, kapasitas):
        self.__kapasitas = kapasitas

    def getJumlahKendaraan(self):
        return self.__jumlahKendaraan

    def setJumlahKendaraan(self, jumlahKendaraan):
        self.__jumlahKendaraan = jumlahKendaraan

    def getCar(self):
        return self.__car
    
    def setCar(self, car):
        self.__car = car

    def getMotorcycle(self):
        return self.__motorcycle
    
    def setMotorcycle(self, motorcycle):
        self.__motorcycle = motorcycle
        