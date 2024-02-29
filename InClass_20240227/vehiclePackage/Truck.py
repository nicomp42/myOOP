# Truck.py

from vehiclePackage.vehicleClass import Vehicle

class Truck(Vehicle):
    def __init__(self, vehicle_type, make, model, color, nickname, bed_length, max_speed=None):
        super().__init__(vehicle_type, max_speed)
        self.make = make
        self.model = model
        self.color = color
        self.nickname = nickname
        self.bed_length = bed_length
    
    def printMake(self):
        print(self.make)
        
    def printModel(self):
        print(self.model)
    
    def printBedLength(self):
        print(f"Bed Length: {self.bed_length} feet")
