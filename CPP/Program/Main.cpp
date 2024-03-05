#include <bits/stdc++.h>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie();

    // Create vehicles
    vector<Car*> daftar_mobil1;  // Change to pointers
    vector<Car*> daftar_mobil2;  // Change to pointers

    Car car1("B 1234 DA", "Tesla", 2020, "Merah", 4, 4);
    Car car2("D 1234 DA", "Hyundai", 2021, "Merah", 4, 4);
    Car car3("B 2234 FA", "Toyota", 2018, "Biru", 7, 4);
    Car car4("D 2234 JA", "Suzuki", 2020, "Silver", 4, 4);

    daftar_mobil1.push_back(new Car(car1));  // Push a copy of the car object
    daftar_mobil1.push_back(new Car(car2));  // Push a copy of the car object
    daftar_mobil2.push_back(new Car(car3));  // Push a copy of the car object
    daftar_mobil2.push_back(new Car(car4));  // Push a copy of the car object

    vector<Motorcycle*> daftar_motor1;  // Change to pointers
    vector<Motorcycle*> daftar_motor2;  // Change to pointers

    Motorcycle motor1("B 1234 DA", "Honda", 2020, "Merah", "Bebek", "25 Liter");
    Motorcycle motor2("D 1234 DA", "Kawasaki", 2021, "Merah", "Sport", "30 Liter");
    Motorcycle motor3("B 2234 FA", "Yamaha", 2018, "Biru", "Bebek", "20 Liter");
    Motorcycle motor4("D 2234 JA", "Suzuki", 2020, "Silver", "Sport", "35 Liter");

    daftar_motor1.push_back(new Motorcycle(motor1));  // Push a copy of the motorcycle object
    daftar_motor1.push_back(new Motorcycle(motor2));  // Push a copy of the motorcycle object
    daftar_motor2.push_back(new Motorcycle(motor3));  // Push a copy of the motorcycle object
    daftar_motor2.push_back(new Motorcycle(motor4));  // Push a copy of the motorcycle object

    // Create Garage instances
    list<Vehicle*> list_mobil1(daftar_mobil1.begin(), daftar_mobil1.end());
    Garage garasi1("Garasi A", 50, "Mobil", list_mobil1);

    list<Vehicle*> list_motor2(daftar_motor2.begin(), daftar_motor2.end());
    Garage garasi2("Garasi B", 60, "Motor", list_motor2);

    // Display Garage details
    cout << "Garage 1 Details:" << endl;
    garasi1.DisplayGarage();
    cout << endl;

    cout << "Garage 2 Details:" << endl;
    garasi2.DisplayGarage();
    cout << endl;

    ParkingLot parking_lot1(100, 4, list_mobil1);

    // Menampilkan informasi parking lot
    cout << "Parking Lot 1 Details:" << endl;
    parking_lot1.DisplayParkingLot();
    cout << endl;

    return 0;
}
