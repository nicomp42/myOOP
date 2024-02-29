# electricClass.py
from vehiclePackage.Car import Car

class Electric(Car):
    def __init__(self, type, make, model, batteryMileage):
        self.batteryMileage = batteryMileage;
        Car.__init__(self, type, make, model);
    def printBatteryMileage(self):
        print(self.batteryMileage);
    