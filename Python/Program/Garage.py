from Car import Car
from Motorcycle import Motorcycle
from Vehicle import Vehicle

class Garage:
    __namaGarasi = ""
    __luasGarasi = ""
    __daftarKendaraan = ""

    def __init__(self, namaGarasi = "", luasGarasi = "", daftarKendaraan = "", car = [], motorcycle = []):
        self.__namaGarasi = namaGarasi
        self.__luasGarasi = luasGarasi
        self.__daftarKendaraan = daftarKendaraan
        self.__car = car
        self.__motorcycle = motorcycle

    def getNamaGarasi(self):
        return self.__namaGarasi
    
    def setNamaGarasi(self, namaGarasi):
        self.__namaGarasi = namaGarasi

    def getLuasGarasi(self):
        return self.__luasGarasi

    def setLuasGarasi(self, luasGarasi):
        self.__luasGarasi = luasGarasi

    def getDaftarKendaraan(self):
        return self.__daftarKendaraan
    
    def setDaftarKendaraan(self, daftarKendaraan):
        self.__daftarKendaraan = daftarKendaraan

    def getCar(self):
        return self.__car
    
    def setCar(self, car):
        self.__car = car

    def getMotorcycle(self):
        return self.__motorcycle
    
    def setMotorcycle(self, motorcycle):
        self.__motorcycle = motorcycle
        