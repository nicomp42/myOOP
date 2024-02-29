
from vehiclePackage.Car import Car;  

class electic(Car):  # Hybrid  class inherits from Car class
    def __init__(self, type, make, model, batteryKVA, color):
        self.color = color;
        Car.__init__(self, type, make, model);
        
    def printBatterylife(self):
        print(self.color);

# electricClass.py
from vehiclePackage.Car import Car

class Electric(Car):
    def __init__(self, type, make, model, batteryMileage):
        self.batteryMileage = batteryMileage;
        Car.__init__(self, type, make, model);
    def printBatteryMileage(self):
        print(self.batteryMileage);
    
# electricClass.py

