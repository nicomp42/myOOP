from vehiclePackage.Car import Car;  

class Sport(Car):
    def __init__(self, type, make, model):
        self.make = make;
        self.model = model;
        Sport.__init__(self, type);
        
    def printMake(self):
        print(self.make);
    
    def printModel(self):
        print(self.model);