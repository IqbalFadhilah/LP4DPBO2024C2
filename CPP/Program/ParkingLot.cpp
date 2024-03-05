#pragma once

#include <bits/stdc++.h>
#include <string>
#include <vector>
#include "Vehicle.cpp"

using namespace std;

class ParkingLot {
private:
    int kapasitas;
    int jumlah_kendaraan;
    list<Vehicle*> parkiran_kendaraan; 

public:
    ParkingLot(){

    }

    ParkingLot(int kapasitas, int jumlah_kendaraan, list<Vehicle*> parkiran_kendaraan){
        this->kapasitas = kapasitas;
        this->jumlah_kendaraan = jumlah_kendaraan;
        this->parkiran_kendaraan = parkiran_kendaraan;
    }

    // Getter
    int getKapasitas() { 
        return kapasitas; 
    }

    int getJumlahKendaraan(){
        return jumlah_kendaraan;
    }
    
    const list<Vehicle*>& getKendaraan() const {  // Return a const reference to the list of Vehicle pointers
        return parkiran_kendaraan; 
    }

    // Setter
    void setKapasitas(int kapasitas) { 
        this->kapasitas = kapasitas; 
    }

    void setJumlahKendaraan(int jumlah_kendaraan) { 
        this->jumlah_kendaraan = jumlah_kendaraan; 
    }

    void setKendaraan(const list<Vehicle*>& parkiran_kendaraan) { 
        this->parkiran_kendaraan = parkiran_kendaraan;
    }

    void DisplayParkingLot() const {
        cout << "Kapasitas Parking Lot: " << kapasitas << " kendaraan" << endl;
        cout << "Jumlah Kendaraan Saat Ini: " << jumlah_kendaraan << " kendaraan" << endl;

        cout << "Daftar Kendaraan:" << endl;
        for (const auto& vehicle : parkiran_kendaraan) {
            vehicle->DisplayDetails();
    }
}

    ~ParkingLot(){

    }
};
