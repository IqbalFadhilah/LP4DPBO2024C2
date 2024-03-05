#pragma once

#include <iostream>
#include <string>

using namespace std;



class Vehicle {
private:
    string plat_nomor;
    string merk;
    int tahun_produksi;
    string warna;
    
public:
    // Constructors
    Vehicle() {

    }

    Vehicle(string plat_nomor, string merk, int tahun_produksi, string warna) {
        this->plat_nomor = plat_nomor;
        this->merk = merk;
        this->tahun_produksi = tahun_produksi;
        this->warna = warna;
    }

    // Getter methods
    string getPlatNomor() { 
        return plat_nomor; 
    }

    string getMerk() { 
        return merk; 
    }

    int getTahunProduksi() { 
        return tahun_produksi; 
    }

    string getWarna() { 
        return warna; 
    }

    
    // Setter methods
    void setPlatNomor(string plat_nomor) { 
        this->plat_nomor = plat_nomor; 
    }

    void setMerk(string merk) { 
        this->merk = merk;
    }

    void setTahunProduksi(int tahun_produksi) { 
        this->tahun_produksi = tahun_produksi; 
    }

    void setWarna(string warna) { 
        this->warna = warna; 
    }

    virtual void DisplayDetails() const {
        cout << "Plat Nomor: " << plat_nomor << endl;
        cout << "Merk: " << merk << endl;
        cout << "Tahun Produksi: " << tahun_produksi << endl;
        cout << "Warna: " << warna << endl;
    }

    // Destructor
    ~Vehicle() {

    }
};
