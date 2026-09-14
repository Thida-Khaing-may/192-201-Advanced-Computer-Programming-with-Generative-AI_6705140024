""" "CampusWheels" Vehicle-Rental Desk """
class Vehicle:
    def __init__(self, make, model, plate):
        self.make= make
        self.model = model
        self.plate = plate
        self.is_rented = False # Every new vehicle starts available
    
    def rent(self):
        self.is_rented = True
    
    def return_vehicle(self):
        self.is_rented = False

    def __str__(self):
        if self.is_rented:
            status ="rented"
        else:
            status = "available"
        
        return "{} {} ({}) [{}]".format(self.make,self.model, self.plate, status)

"""Showing a customer renting vehicles. """
class Renter:

    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no
        self.rented =[] #start with an empty list of rented vehicle
    #Getter for name
    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must not be empty.")
        self._name = value.strip()
    
   
    #Getter for license_no
    @property
    def license_no(self):
        return self._license_no
    
    @license_no.setter
    def license_no(self,value):
        if isinstance(value, bool) or not isinstance(value,(int,float)) or value <= 0:            
            raise ValueError("License number must be a positive number.")
        self._license_no = value 
    
#ElectricCar inherits from Vehicle 
class ElectricCar(Vehicle):
    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make,model,plate) # call the parent constructor to set make, model and plate
        self.battery_kwh =battery_kwh
        
    #Overrides __str__ to display battery details
    def __str__(self):
        if self.is_rented:
            status ="rented"
        else:
            status = "available"
                
        return "Electric Car: {} {} ({}) - {}kWh [{}]".format(self.make,self.model, self.plate,self.battery_kwh, status)

#Motorbike inherits from Vehicle
class Motorbike(Vehicle):
    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate) 
        self.engine_cc = engine_cc

    #Override to display engine size
    def __str__(self):
        if self.is_rented:
            status ="rented"
        else:
            status = "available"
                        
        return "Motorbike: {} {} ({}) - {}cc [{}]".format(self.make,self.model, self.plate,self.engine_cc, status)
