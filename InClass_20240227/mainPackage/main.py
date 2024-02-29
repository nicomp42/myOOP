# main.py
# Add an import statement for Vehicle class
from vehiclePackage.vehicleClass import *
from vehiclePackage.hybridClass import Hybrid
from vehiclePackage.ElectricClass import Electric

if __name__ == "__main__":
    # Instantiate an object of type Hybrid
    myPrius = Hybrid("Electric", "Toyota", "Prius", 220)  # Invoke the Hybrid class constructor
    # Invoke the printType method using the HJybrid object we just created
    myPrius.printType()
    
    
    '''
    # Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120)  # Trigger a call to constructor
    myCorvette.printType()       # invoke the method on the object
    
    # Invoke the getter for maximum speed, store the return value in a variable
    #  print that to the console.
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # instantiate another Vehicle object. You can name it
    myCorolla = Vehicle("Car")   # myCorolla is an object of type Vehicle
    
    
    # I want a list of 3 Vehicles: Car, Boat, Space Ship
    # You can pick the names and properties
    # I want some friendly output to demo your work
    myVehicles = [  Vehicle("Toyota Camry", 150)
                  , Vehicle("sailboat", 20)
                  , Vehicle("Falcon Heavy", 4000)]
    # iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    '''
    