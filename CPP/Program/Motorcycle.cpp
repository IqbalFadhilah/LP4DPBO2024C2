#pragma once

#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle {
private:
    string jenis_motor;
    string kapasitas_tangki;

public:
    Motorcycle(){

    }

    Motorcycle(string plat_nomor, string merk, int tahun_produksi, string warna, string jenis_motor, string kapasitas_tangki) : Vehicle(plat_nomor, merk, tahun_produksi, warna){
        this->jenis_motor = jenis_motor;
        this->kapasitas_tangki = kapasitas_tangki;
    }

    // Getter
    string getJenisMotor() { 
        return jenis_motor; 
    }
    string getKapasitasTangki() { 
        return kapasitas_tangki; 
    }


    // Setter
    void setJenisMotor(string jenis_motor) { 
        this->jenis_motor = jenis_motor; 
    }
    void setKapasitasTangkik(string kapasitas_tangki) { 
        this->kapasitas_tangki = kapasitas_tangki;
    }

    void DisplayDetails() const override {
        Vehicle::DisplayDetails();
        cout << "Jenis Motor: " << jenis_motor << endl;
        cout << "Kapasitas Tangki: " << kapasitas_tangki << endl;
        cout << "---------------------------------------------" << endl;
    }

    ~Motorcycle(){
        
    }
};