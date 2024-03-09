from Vehicle import Vehicle

class Car(Vehicle):
    __jumlahKursi = ""
    __jumlahPintu = ""

    def __init__(self, platNomor="", merk="", tahunProduksi="", warna="", jumlahKursi ="", jumlahPintu =""):
        super().__init__(platNomor, merk, tahunProduksi, warna)
        self.__jumlahKursi = jumlahKursi
        self.__jumlahPintu = jumlahPintu

    def getJumlahKursi(self):
        return self.__jumlahKursi
    
    def setJumlahKursi(self, jumlahKursi):
        self.__jumlahKursi = jumlahKursi

    def getJumlahPintu(self):
        return self.__jumlahPintu

    def setJumlahPintu(self, jumlahPintu):
        self.__jumlahPintu = jumlahPintu