from rental import Vehicle, Renter, ElectricCar, Motorbike

def main():
    print("=== Vehicle Testing ===")
    car = Vehicle("Toyota", "Yaris", "1AB234")
    print("Initial vehicle status:", car)

    #Rent the vehicle 
    car.rent()
    print("After rent:", car)

    #Return the vehicle
    car.return_vehicle()
    print("After return vehicle status:", car)

    print("\n=== Renter Testing ===")
    renter = Renter("Alice", 12345)
    print("Name:", renter.name)
    print("License:" , renter.license_no)
    print("Rented vehicles list:" , renter.rented)

    print("\n=== Invalid Renter Test ===")
    try:
        print("Testing empty name validation...")
        bad_renter = Renter("", 12345)
    except ValueError as err:
        print("Caught expected error:", err)
    
    # Zero license number should fail
    try:
        print("Testing zero license number validation...")
        bad_renter = Renter("Bob", 0)
    except ValueError as err:
        print("Caught ValueError (zero license):", err)
    
    #Negative license number should fail
    try:
        print("Testing negative license number validation...")
        bad_renter = Renter("Clore", -10)
    except ValueError as err:
        print("Caught ValueError (negative license):",err)

    print("\n=== Property Validation Test ===")
    renter.name = "David"
    print("Changed name:", renter.name)
    renter.license_no = 67890
    print("Changed license:", renter.license_no)

    # Invalid modification should raise ValueError
    try:
        renter.name = ""
    except ValueError as err:
        print("Caught ValueError (empty string assigned):", err)

    try:
        renter.license_no = -5
    except ValueError as err:
        print("Caught ValueError (negative number assigned):", err)

    try:
        print("Testing validation on later attribute modification...")
        valid_renter = Renter("Charlie", 9999)
        valid_renter.license_no = 0
    except ValueError as err:
        print("Caught expected error:", err)
    
    print("\n=== Inheritance Check ===")
    ev = ElectricCar("Tesla", "Model 3", "EV7890", 75)
    bike = Motorbike("Yamaha", "MT-07", "BK3341", 689)
    print("ElectricCar is Vehicle:", isinstance(ev, Vehicle))
    print("Motorbike is Vehicle:", isinstance(bike, Vehicle))

    print("\n=== Polymorphism Demonstration ===")
    vehicles = [
        Vehicle("Honda", "Civic", "9XY112"),
        ElectricCar("Tesla", "Model 3","EV7890", 75),
        Motorbike("Yamaha", "MT-07", "BK3341", 689)

    ]

    # One loop handling multiple different types
    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()