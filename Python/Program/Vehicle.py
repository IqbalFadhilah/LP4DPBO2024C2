class Vehicle:
    __platNomor = ""
    __merk = ""
    __tahunProduksi = ""
    __warna = ""

    def __init__(self, platNomor = "", merk = "", tahunProduksi = "", warna = ""):
        self. __platNomor = platNomor
        self. __merk = merk
        self.__tahunProduksi = tahunProduksi
        self.__warna = warna

    def getPlatNomor(self):
        return self.__platNomor
    
    def setPlatNomor(self, platNomor):
        self.__platNomor = platNomor

    def getMerk(self):
        return self.__merk

    def setMerk(self, merk):
        self.__merk = merk

    def getTahunProduksi(self):
        return self.__tahunProduksi
    
    def setTahunProduksi(self, tahunProduksi):
        self.__tahunProduksi = tahunProduksi

    def getWarna(self):
        return self.__warna
    
    def setWarna(self, warna):
        self.__warna = warna