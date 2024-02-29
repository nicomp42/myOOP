from vehiclePackage.vehicleClass import *;            # This works but Eclipse flags an error in the editor.

class plane(Vehicle):  # Hybrid  class inherits from Car class
    def __init__(self, type, make, model):
        self.make = make;
        self.model = model;
        Vehicle.__init__(self, type);

'''
if __name__ == "__main__":
    myPlane = plane("Plane", "Boeing", "787")
'''