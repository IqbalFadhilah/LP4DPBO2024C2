#pragma once

#include <bits/stdc++.h>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle {
private:
    int jumlah_kursi;
    int jumlah_pintu;

public:
    Car(){

    }

    Car(string plat_nomor, string merk, int tahun_produksi, string warna, int jumlah_kursi, int jumlah_pintu) : Vehicle(plat_nomor, merk, tahun_produksi, warna) {
        this->jumlah_kursi = jumlah_kursi;
        this->jumlah_pintu = jumlah_pintu;
    }



    // Getter
    int getJumlahKursi() { 
        return jumlah_kursi; 
    }
    int getJumlahPintu() { 
        return jumlah_pintu; 
    }

    // Setter
    void setJumlahKursi(int jumlah_kursi) { 
        this->jumlah_kursi = jumlah_kursi; 
    }
    void setJumlahPintu(int jumlah_pintu) { 
        this->jumlah_pintu = jumlah_pintu;
    }

    void DisplayDetails() const override {
        Vehicle::DisplayDetails();
        cout << "Jumlah Kursi: " << jumlah_kursi << endl;
        cout << "Jumlah Pintu: " << jumlah_pintu << endl;
        cout << "---------------------------------------------" << endl;
    }
    
    ~Car(){
        
    }
};