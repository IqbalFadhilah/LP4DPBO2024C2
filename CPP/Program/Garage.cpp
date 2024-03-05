#pragma once

#include <bits/stdc++.h>
#include <string>
#include <vector>
#include "Vehicle.cpp"

using namespace std;

class Garage {
private:
    string nama_garasi;
    int luas_garasi;
    string daftar_kendaraan;
    list<Vehicle*> kendaraan;  // Change this to a list of Vehicle pointers

public:
    Garage(){

    }

    Garage(string nama_garasi, int luas_garasi, string daftar_kendaraan, list<Vehicle*> kendaraan){
        this->nama_garasi = nama_garasi;
        this->luas_garasi = luas_garasi;
        this->daftar_kendaraan = daftar_kendaraan;
        this->kendaraan = kendaraan;
    }

    // Getter
    string getNamaGarasi() { 
        return nama_garasi; 
    }

    int getLuasGarasi() { 
        return luas_garasi; 
    }
    
    string getDaftarKendaraan() { 
        return daftar_kendaraan; 
    }

    const list<Vehicle*>& getKendaraan() const {  // Return a const reference to the list of Vehicle pointers
        return kendaraan; 
    }

    // Setter
    void setNamaGarasi(string nama_garasi) { 
        this->nama_garasi = nama_garasi; 
    }
    
    void setLuasGarasi(int luas_garasi) { 
        this->luas_garasi = luas_garasi;
    }

    void setDaftarKendaraan(string daftar_kendaraan) { 
        this->daftar_kendaraan = daftar_kendaraan; 
    }

    void setKendaraan(const list<Vehicle*>& kendaraan) { 
        this->kendaraan = kendaraan;
    }

    void DisplayGarage() const {
        cout << "Nama Garasi: " << nama_garasi << endl;
        cout << "Luas Garasi: " << luas_garasi << "meter persegi" << endl;
        cout << "Daftar Kendaraan: " << daftar_kendaraan << endl;

        // Display details of each vehicle in the garage
        for (const auto& vehicle : kendaraan) {
            vehicle->DisplayDetails();
        }
    }

    ~Garage(){
        
    }
};
