from Vehicle import Vehicle

class Motorcycle(Vehicle):
    __jenisMotor = ""
    __kapasitasTangki = ""

    def __init__(self, platNomor="", merk="", tahunProduksi="", warna="", jenisMotor ="", kapasitasTangki =""):
        super().__init__(platNomor, merk, tahunProduksi, warna)
        self. __jenisMotor = jenisMotor
        self.__kapasitasTangki = kapasitasTangki

    def getJenisMotor(self):
        return self.__jenisMotor
    
    def setJenisMotor(self, jenisMotor):
        self.__jenisMotor = jenisMotor
    
    def getKapasitasTangki(self):
        return self.__kapasitasTangki
    
    def setKapasitasTangki(self, kapasitasTangki):
        self.__kapasitasTangki = kapasitasTangki