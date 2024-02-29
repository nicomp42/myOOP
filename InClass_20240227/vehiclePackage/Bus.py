from vehiclePackage.vehicleClass import Vehicle;
class Bus(Vehicle):
    def __init__(self, type_of_vehicle, make, model,size):
        self.make = make;
        self.model = model;
        self.size = size;
        Vehicle.__init__(self, type_of_vehicle);
        
    def printSize(self):
        print(self.size);
    